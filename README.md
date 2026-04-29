# U.S. Job Market Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![BLS](https://img.shields.io/badge/Data-BLS%20API-red)

An end-to-end data analysis project exploring 10 years of U.S. labor market trends
using official Bureau of Labor Statistics (BLS) data.

## Live Charts
![Unemployment Rate](data/processed/chart1_unemployment.png)
![Monthly Job Gains](data/processed/chart2_payrolls.png)
![Labor Force Participation](data/processed/chart3_participation.png)
![Correlation Heatmap](data/processed/chart4_correlation.png)

## Key Insights

### COVID Impact
- Unemployment spiked from **3.5% to 14.8%** in just 2 months (Feb–Apr 2020)
  — the fastest job loss in U.S. history, with 22 million jobs wiped out
- The 2020 yearly average of 8.1% is misleading — January was 3.5% 
  and April was 14.8%, showing how averages can hide the real story

### Recovery
- Unemployment recovered to pre-COVID levels by 2022, faster than 
  most economists predicted, driven by $5 trillion in government stimulus
- Nonfarm payrolls hit an all-time high of 158,316 thousand in 2024, 
  surpassing pre-COVID levels

### Structural Changes
- Labor force participation **never fully recovered** to its pre-COVID 
  level of 63.3%, suggesting ~3 million Americans permanently left the workforce
- A **-0.9 correlation** between unemployment and participation confirms 
  that during downturns, workers stop looking entirely — meaning official 
  unemployment figures understate the true picture

### 2024 Warning Signal
- Unemployment crept up from 3.7% to 4.2% through 2024 — a trend 
  worth monitoring as a potential early signal of economic slowdown

## What I Learned
- Real-world government APIs require more cleaning than expected — 
  annual averages needed to be filtered out from monthly data
- Averages can be deeply misleading for volatile data — 
  the 2020 yearly average of 8.1% hides the true crisis magnitude
- Correlation alone doesn't tell the full story — the -0.9 figure 
  only makes sense when you understand the underlying human behavior

## Tech Stack
- **Python** — data collection, cleaning, analysis
- **Pandas** — data wrangling and transformation
- **Matplotlib & Seaborn** — data visualization
- **BLS Public API** — official U.S. government labor data
- **Jupyter Notebook** — interactive analysis environment
- **SQLite** — local data storage and SQL querying

## Project Structure
us-job-market-dashboard/
├── data/
│   ├── raw/          # BLS API responses
│   └── processed/    # cleaned CSVs and chart images
├── notebooks/
│   └── 01_data_collection.ipynb
├── src/
│   └── bls_fetcher.py
├── requirements.txt
└── README.md

## How to Run Locally
1. Clone the repo
```bash
   git clone https://github.com/Kamrul732/us-job-market-dashboard.git
   cd us-job-market-dashboard
```
2. Create a virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```
3. Add your BLS API key to a `.env` file
BLS_API_KEY=16c70740f37942d4b1eb87e52b955a66

4. Run the data fetcher
```bash
   python src/bls_fetcher.py
```
5. Open the notebook
```bash
   jupyter notebook notebooks/01_data_collection.ipynb
```

## Data Source
Bureau of Labor Statistics (BLS) Public API — [bls.gov/developers](https://bls.gov/developers)
Series used: LNS14000000, CES0000000001, LNS12300000