from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 建立 3 qubit + 3 classical bit 的量子電路
qc = QuantumCircuit(3, 3)

# Step 1: 疊加初始狀態
qc.h([0, 1, 2])

# Step 2: Oracle - 標記 |101⟩（qubit 2=1, 1=0, 0=1）
qc.x(1)
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x(1)

# Step 3: 擴散運算（Diffusion）
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])

# Step 4: 測量
qc.measure([0, 1, 2], [0, 1, 2])

# 執行模擬器
backend = AerSimulator()  # 直接使用 AerSimulator
result = backend.run(qc, shots=1024).result()  # 使用 run 方法运行电路
counts = result.get_counts(qc)  #

print("Grover 結果：", counts)
plot_histogram(counts)
plt.show()
