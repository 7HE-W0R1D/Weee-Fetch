# Weee-Fetch 🛍️

[English Version](README_EN.md) | 中文版

**Weee-Fetch** 是一个用于抓取 Weee! 商品评价数据的 Python 工具包。本项目专为**数据分析**和**学习交流**而生，旨在研究 Web API 交互及数据持久化的实现方式。

> [!IMPORTANT]
> **声明：** 本项目仅限学习与研究使用，请勿用于任何商业用途或违反相关平台服务条款的行为。

---

## ✨ 核心功能
- **智能解析**：支持直接粘贴 Weee! 商品链接，自动提取商品名称与 ID。
- **多语言支持 (中/英)**：可自定义拉取评价的语言（原生中文或英文）。
- **灵活抓取**：可自定义抓取前 N 条评价，或全量抓取。
- **高清导出 & 排版**：Excel 导出版本支持将抓取到的高清评价图片直接嵌入到表格单元格内，自动调准行高列宽。
- **命令行 (CLI) 自动化**：支持通过参数自动运行脚本，适合批量和后台任务。
- **独立图片下载**：支持从已抓取的 JSON 文件中批量提取并下载所有高清原图。
- **交互友好**：全流程集成 `tqdm` 智能进度条，实时展示进度。

---

## 🚀 快速开始

### 1. 环境准备

推荐使用 Python 3.7 或更高版本。

安装必要依赖：
```bash
pip install requests openpyxl pillow tqdm argparse
```

### 2. 运行指南

项目包含以下几个主要脚本，可根据需求选择运行：

| 脚本名称 | 功能描述 |
| :--- | :--- |
| `Test-weee-excel.py` | **[推荐]** 抓取商品评价并保存为 JSON 及包含嵌入图片的 Excel。 |
| `Test-weee.py` | 抓取全部商品评价并保存为 JSON 及 CSV。 |
| `download_json_pictures.py` | 独立工具，用于从抓取的 JSON 数据中批量下载所有原始高清图片。 |
| `Test-weee-2p-excel.py` | 测试用脚本，仅抓取前 2 页并保存 Excel (含图片)。 |

#### 交互模式运行
直接运行脚本，按照提示输入商品链接或 ID：
```bash
python Test-weee-excel.py
```

#### Google Colab (云端运行)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/7HE-W0R1D/Weee-Fetch/blob/main/Weee_Fetch_Colab.ipynb)

如果您不想在本地安装 Python 环境，可以使用提供的 Jupyter Notebook 在 Google Colab 上运行：
1. 在 GitHub 或本地找到 `Weee_Fetch_Colab.ipynb`。
2. 上传至 [Google Colab](https://colab.research.google.com/)。
3. 按照单元格提示运行及下载数据。


#### 命令行 CLI 运行
使用参数自动运行，提高效率：
```bash
# 获取中文评价
python Test-weee-excel.py --product-id https://www.sayweee.com/zh/products/HADAY-Delicious-Light-Soy-Sauce/113281 --lang cn

# 获取英文评价
python Test-weee-excel.py --product-id 113281 --lang en
```

---

## 📂 数据结构说明

抓取的数据统一存放于项目根目录下的 `fetched-data/` 文件夹中。为了方便管理，每次抓取会基于 **商品名**、**ID**、**时间戳**、**评论数** 生成专属目录：

```text
fetched-data/
└── HADAY-Delicious-Light-Soy-Sauce_113281_20260403_122953_2/
    ├── HADAY-Delicious-Light-Soy-Sauce_113281...json    # 原始 JSON 数据
    ├── HADAY-Delicious-Light-Soy-Sauce_113281...xlsx    # Excel 版 (含图片)
    └── [该目录下的图片子文件夹]/                           # (可选) 独立图库导出存放处
```

---

## ⚖️ 免责声明
本项目仅供学习。代码作者不对因使用本程序而产生的任何直接或间接影响负责。
