# Daily price Change sorting activity

This repository contains a python program that create a plots based on how long it takes numpy sort to sort daily price change.

## 📁 Project Structure

```

├── mainCode.py
├── unitTest.py
├── requirements.txt
├── historicalData.csv
├── LICENSE
└── README.md
└── .circle.ci/
    └── config.yml

```

## 📊 Dataset

The dataset used was obtained from Nasdaq:
1. [MX Nordic 40 (OMXN40) Historical Data\](https://www.nasdaq.com/market-activity/index/omxn40/historical?page=25&rows_per_page=10&timeline=y1)
    * Data downloaded for the year 2025 on 20/10/2025


## 🛠️ Installation

Python 3.10 or newer to run python files

Python modules required:

* time – Time how long it takes numpy sort
* pandas – Reading and handling CSV files.
* matplotlib – Plotting graphs.
* numpy – Preforming numpy sort

You can install required packages with:

```
pip install time pandas matplotlib numpy

```


## 📄 License
This project is open source and available under the [MIT License](https://github.com/hafybufya/daily-price-change-sorting/blob/main/LICENSE).

