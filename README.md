# Grover's Algorithm Password Cracking Simulator

This is a Python project that simulates **Grover's Algorithm** using [Qiskit](https://qiskit.org/). Grover’s algorithm is a quantum search algorithm that finds a target item in an unsorted database in $\sqrt{N}$ time. This demo shows how it can be applied to "crack" a 3-bit quantum password.

---

## Project Highlights

- ✅ Simulates a quantum circuit that searches for a 3-qubit password `|101⟩`
- ✅ Full implementation of Oracle + Diffuser logic
- ✅ Visualization support (histogram and Bloch Sphere)
- ✅ Easily customizable target state

---

## Technologies Used

- Python 3.8+
- Qiskit
- matplotlib (for Bloch Sphere plotting)
- VS Code / Jupyter Notebook

---

## Installation & Execution

1. Install dependencies:

```bash
pip install "qiskit[all]"
```
2. Run the main program:
```bash
python Grover_3_Qubit.py
```
Or open Grover_3_Qubit.ipynb in Jupyter Notebook to walk through the quantum state step-by-step.

## 📂 Project Structure

grover-demo/

├── Grover_3_Qubit.py         # Main Grover search with 3 qubits

├── Bloch_sphere.py           # Bloch Sphere visualization demo

└── README.md                 # This documentation


## Sample Output
```bash
Measurement result（shots=1000）:
{'101': 967, '000': 11, '011': 7, '100': 8, '111': 7}
```

# Grover's Algorithm 密碼破解模擬器

這是一個使用 [Qiskit](https://qiskit.org/) 模擬 **Grover's Algorithm** 的 Python 專案。Grover 是一個量子搜尋演算法，可以在 $\sqrt{N}$ 的時間內搜尋資料庫，本專案用來展示如何「量子破解一個 3 位元密碼」。

---

## 專案亮點

- ✅ 模擬量子電路：3 qubit 查找密碼 `|101⟩`
- ✅ Oracle + 擴散器（Diffuser）的完整實作
- ✅ 結果可視化（histogram、Bloch Sphere）
- ✅ 支援自訂搜尋目標

---

## 使用技術

- Python 3.8+
- Qiskit
- matplotlib（畫 Bloch Sphere）
- VS Code / Jupyter Notebook

---

## 安裝與執行

1. 安裝必要套件：

```bash
pip install "qiskit[all]"
```

2. 執行主程式：
```bash
python Grover_3_Qubit.py
```
或在 Jupyter Notebook 中開啟 Grover_3_Qubit.ipynb 逐步觀察量子狀態變化。

## 📂 專案結構

grover-demo/

├── Grover_3_Qubit.py         # 主程式：3 qubit 的 Grover 搜尋

├── Bloch_sphere.py           # Bloch Sphere 可視化 demo

└── README.md                 # 本說明文件

## 執行輸出（範例）
```bash
測量結果（shots=1000）:
{'101': 967, '000': 11, '011': 7, '100': 8, '111': 7}
```

