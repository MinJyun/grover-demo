from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# 建立一個量子電路
qc = QuantumCircuit(3, 3)

# 加上 gate：你可以改成 qc.x(0) 或 qc.h(0)
qc.h([0, 1, 2])
qc.x(1)
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x(1)
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)

# 取得狀態向量
state = Statevector.from_instruction(qc)

# 畫 Bloch Sphere
plot_bloch_multivector(state)
plt.show()
