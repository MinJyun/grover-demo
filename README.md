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

