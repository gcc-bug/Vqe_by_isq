# Vqe_by_isq
 This project implements vqe with isq.
Isq is a software stack for quantum programming. It will be used to desgin quantum circuit in this project.
The syntax of isq is given in document [isq语言用户手册.pdf](references/isq%E8%AF%AD%E8%A8%80%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf)
## $H_2$ for attempt
The quantum circuit design in [H_vqe.ipynb](example/H_vqe.ipynb) refer to [Scalable Quantum Simulation of Molecular Energies](references/PhysRevX.6.031007.pdf)
In this attempt, Hamiltonian is mapped into qubits for implemention on a quantum device by Bravyi-Kitaev transformation.Thus the Hamiltion is :

$$H= f_{0} \mathbb{I}+f_{1} Z_{0}+f_{2} Z_{1}+f_{3} Z_{2}\\\\+f_{1} Z_{0} Z_{1} +f_{4} Z_{0} Z_{2}+f_{5} Z_{1} Z_{3}+f_{6} \boldsymbol{X}_{\mathbf{0}} Z_{1} \boldsymbol{X}_{\mathbf{2}}\\\\+f_{6} \boldsymbol{Y}_{\mathbf{0}} Z_{1} \boldsymbol{Y}_{\mathbf{2}} +f_{7} Z_{0} Z_{1} Z_{2}+f_{4} Z_{0} Z_{2} Z_{3}+f_{3} Z_{1} Z_{2} Z_{3} 
\\\\+f_{6} \boldsymbol{X}_{\mathbf{0}} Z_{1} \boldsymbol{X}_{\mathbf{2}} Z_{3}+f_{6} \boldsymbol{Y}_{\mathbf{0}} Z_{1} \boldsymbol{Y}_{\mathbf{2}} Z_{3}+f_{7} Z_{0} Z_{1} Z_{2} Z_{3}$$

This Hamiltonian acts off diagonally on only two qubits (the ones having tensor factors of 0 and 2).If we start our simulations in the Hartree-Fock state,the Hamiltonian stabilizes qubits 1 and 3 so that they are never flipped throughout the simulation.
So this project use the following effective Hamiltonian which acts only on two qubits:
$$\tilde{H}=g_{0} \mathbb{I}+g_{1} Z_{0}+g_{2} Z_{1}+g_{3} Z_{0} Z_{1}+g_{4} X_{0} X_{1}+g_{5} Y_{0} Y_{1}$$
In R=0.75A, $$g_0=−0.4804,g_1=0.3435,g_2=−0.4347,\\\\g_3=0.5716,g_4=0.0910,g_5=0.0910.$$
In this attempt, the anstaz is UCC. UCC predicts that the ground state can be expressed as:
$$|\phi(\theta)\rangle=e^{-i\theta X_0Y_1}|01\rangle$$
