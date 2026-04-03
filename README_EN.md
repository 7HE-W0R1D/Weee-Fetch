# Weee-Fetch 🛍️

English Version | [中文版](README.md)

**Weee-Fetch** is a Python toolkit designed to scrape product reviews from Weee!. This project is created strictly for **data analysis** and **educational purposes**, aiming to study Web API interaction and data persistence implementations.

> [!IMPORTANT]
> **Disclaimer:** This project is only for learning and research. Do not use it for commercial purposes or in any way that violates the platform's terms of service.

---

## ✨ Core Features
- **Smart Parsing**: Paste a Weee! product URL directly; the script automatically extracts the product name and ID for file naming.
- **Multilingual Support (EN/ZH)**: Choose to fetch reviews in English or Chinese by simulating specific request headers (`--lang en` or `--lang cn`).
- **Flexible Fetching**: Set a limit on the number of reviews to grab, or fetch them all.
- **High-Res Excel Export**: The Excel version automatically embeds review images directly into the spreadsheet cells, adjusting row and column sizes for the best visual layout.
- **CLI Automation**: Pass arguments via the command line for automated workflows and scheduled tasks.
- **Standalone Image Downloader**: Extract and save all high-res original images from a fetched JSON file.
- **User-Friendly UI**: Integrates `tqdm` smart progress bars for real-time status updates through the entire flow.

---

## 🚀 Quick Start

### 1. Environment Setup

Python 3.7 or higher is recommended.

Install the required dependencies:
```bash
pip install requests openpyxl pillow tqdm argparse
```

### 2. Usage Guide

The repository includes several main scripts. Choose the one that fits your needs:

| Script Name | Description |
| :--- | :--- |
| `Test-weee-excel.py` | **[Highly Recommended]** Fetches reviews and exports to JSON and Excel (with embedded images). |
| `Test-weee.py` | Fetches reviews and exports to JSON and CSV. |
| `download_json_pictures.py` | Standalone tool to bulk-download original images from fetched JSON data. |
| `Test-weee-2p-excel.py` | Quick test script: grabs only the first 2 review pages and exports to Excel. |

#### Interactive Mode
Run the script and follow the prompts to input your URL, language choice, and maximum review count:
```bash
python Test-weee-excel.py
```

#### Google Colab (Cloud Execution)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/7HE-W0R1D/Weee-Fetch/blob/main/Weee_Fetch_Colab.ipynb)

If you don't want to install Python locally, you can use the provided Jupyter Notebook on Google Colab:
1. Find `Weee_Fetch_Colab.ipynb` in the repo or on your computer.
2. Upload it to [Google Colab](https://colab.research.google.com/).
3. Follow the cell prompts to run and download your data.


#### CLI Mode
Run seamlessly via command line arguments:
```bash
# Fetch Chinese reviews from a URL
python Test-weee-excel.py --product-id https://www.sayweee.com/zh/products/HADAY-Delicious-Light-Soy-Sauce/113281 --lang cn

# Fetch English reviews using a direct Product ID
python Test-weee-excel.py --product-id 113281 --lang en
```

---

## 📂 Data Structure

Fetched data is stored in the `fetched-data/` folder at the project root. For better organization, a smart directory structure is generated based on **Product Name**, **ID**, **Timestamp**, and **Review Count**:

```text
fetched-data/
└── HADAY-Delicious-Light-Soy-Sauce_113281_20260403_122953_2/
    ├── HADAY-Delicious-Light-Soy-Sauce_113281...json    # Standard JSON Output
    ├── HADAY-Delicious-Light-Soy-Sauce_113281...xlsx    # Excel with Embedded Images
    └── [Folder with images output]/                     # (Optional) Bulk image folder
```

---

## ⚖️ Disclaimer
This project is for educational purposes only. The authors are not responsible for any direct or indirect consequences resulting from the use of this software.
