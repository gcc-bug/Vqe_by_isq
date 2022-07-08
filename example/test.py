# %%
from isq import isq
@isq.qpu(backend="simulate", shots=100)
#theta:float,E_N=5
def H_2(theta,e_n):
    '''
    qbit q[2];
    X<q[1]>;

    Ry(1.57)<q[0]>;
    Rx(4.71)<q[1]>;
    CNOT<q[0],q[1]>;
    Rz(theta)<q[1]>;
    CNOT<q[0],q[1]>;
    Ry(4.71)<q[0]>;
    Rx(1.57)<q[1]>;

    if(e_n== 0){
        M<q[0]>;
    }
    if(e_n==1){
        M<q[1]>;
    }
    if(e_n==2){
        M<q[0,1]>;
    }
    if(e_n==3){
        Rx(1.57)<q[0]>;
        Rx(1.57)<q[1]>;
        M<q[0,1]>;
    }
    if(e_n==4){
        H<q[0]>;
        H<q[1]>;
        M<q[0,1]>;
    }
    '''

# %%
def get_exception(theta)->float :
    '''
    thetas制备时角度
    e_n<= E_N，测量第n个能量e
    '''
    theta = float(theta)
    E_N=5
    exceptions = list()
    hs=[-0.4804,+0.3435,-0.4347,+0.5716,+0.0910,+0.0910]
    exceptions.append(hs[0])
    for e_n in range(E_N) :
        test_res=H_2(theta,e_n)
        exception = 0
        for measure_res in test_res :
            frequency = test_res[measure_res]/100
            #频率代替概率
            parity = (-1)**(measure_res.count('1')%2)
            #奇偶校验
            exception += parity*frequency
        exceptions.append(hs[e_n+1]*exception)
    return sum(exceptions)

# %%
H_2(0,3)

# %%
# nelder-mead optimization of a convex function
from scipy.optimize import minimize
from numpy.random import rand

# define range for theta
theta_min, theta_max = -3.14, 3.14
# define the starting point as a random sample from the domain
pt = theta_min + rand(1) * (theta_max - theta_min)

# %%
# perform the search
result = minimize(get_exception, pt, method='nelder-mead')
# summarize the result
print(f"Status : {result['message']}")
print(f"Total Evaluations: {result['nfev']}")
# evaluate solution
solution = result['x']
evaluation = get_exception(solution)
print(f"Solution: H_2({solution}) = {evaluation} Eh")


