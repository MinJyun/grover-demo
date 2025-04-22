from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
from math import pi

# 單一 qubit 實驗
qc = QuantumCircuit(2,2)

# 試著改成 h, x, x+h, h+x 等不同組合
# qc.h([0,1])
state = Statevector.from_instruction(qc)
print(state)