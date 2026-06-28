# DS ML 学习笔记

我的数据科学与机器学习课程学习仓库，涵盖 NumPy、Pandas、Matplotlib/Seaborn、Machine Learning 四大模块。不只是笔记——每个 notebook 都包含数学推导的直观分析和代码逐行详解，适合边学边理解底层逻辑。

## 📖 在线阅读

所有 notebook 已自动部署为网页，无需本地环境即可浏览：

👉 **[ty1-210.github.io/learning-notes](https://ty1-210.github.io/learning-notes/)**

## 🗂 内容结构

### NumPy 学习
`numpy学习/` — 从零开始系统学习 NumPy：

- ndarray 的特性、属性与创建方式
- 数据类型、索引切片与运算
- 常用函数与综合练习

共 9 个 notebook + 1 个综合练习，覆盖从入门到实操的完整路径。

### Pandas 学习
`pandas学习/` — 数据处理核心技能：

- Series 与 DataFrame 的创建与操作
- 数据导入导出（CSV、JSON 等）
- 缺失值、重复值与数据类型转换处理
- 数据变形、分箱、时间序列
- 分组聚合与综合练习

共 13 个 notebook，由浅入深构建数据处理能力。

### 可视化练习
`可视化练习/` — Matplotlib 与 Seaborn 实战：

- 基础绘图、统计图与密度图
- 图例、颜色条与多子图布局
- 文本标注、刻度与样式配置
- 3D 绘图与 Seaborn 高级可视化

共 7 个 notebook，从基础 API 到复杂图表一应俱全。

### Machine Learning
`machine learning/` — 经典机器学习算法实现与分析：

- **NumPy 基础**：为 ML 做数值计算准备
- **数据操作**：用 PyTorch 处理数据集
- **PyTorch 基础**：Tensor 操作与自动求导
- **PCA 主成分分析**：完整数学推导 + 代码详解
- **Softmax 回归**：从线性打分到交叉熵的完整链路
- **逻辑回归**：二分类与多分类的 PyTorch 实现
- **LeNet 卷积网络**：CNN 经典架构从零实现
- **AutoEncoder 自编码器**：无监督特征学习
- **LSTM 长短期记忆网络**：序列建模实战

每个 notebook 均包含完整的数学推导和代码注释，侧重"为什么这么写"而不仅是"怎么写"。

### 附带数据
`data/` — 14 个练习用数据集（CSV、JSON、NPY、NPZ），涵盖员工信息、考试成绩、股票价格、天气数据、销售记录等，可直接用于 Pandas 和 NumPy 练习。

## 🔧 本地运行

```bash
git clone https://github.com/Ty1-210/learning-notes.git
cd learning-notes
pip install jupyter nbformat numpy pandas matplotlib seaborn torch torchvision
jupyter notebook
```

## 📦 自动部署

本仓库通过 GitHub Actions 自动将 `.ipynb` 文件转换为 HTML，部署到 GitHub Pages。推送即更新，无需手动构建。

---

> GitHub 自带的 notebook 渲染偶尔不稳定，如遇页面打不开，请使用上方的 Pages 链接。所有 `.ipynb` 文件均可直接下载。
