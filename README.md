# **Banking Risk & Loan Performance Dashboard**

This project is an end-to-end data analytics portfolio piece that combines Python for data preprocessing and Tableau for business visualization. It was designed as a personal project to explore strategic insights in the banking industry.

### Purpose

To explore **loan risk, performance, and lending patterns** across the U.S. banking system using a real-world public dataset. The goal was to identify trends in default rate, interest rate behavior, and lending purpose composition. This dashboard simulates the insights to inform strategy, credit risk, or customer behavior modeling.

### Tools Used

- **Python**: Preprocessing & transformation (Pandas, NumPy, datetime)
- **Tableau**: Dashboarding and interactivity
- **GitHub**: Hosting processed and raw datasets, dashboard snapshot, and notebook

## 📸 Dashboard Screenshot
![Banking Risk Loan Performance](<Banking_Risk_Loan_Performance.png">)

### Dataset Source

- **Source**: [LendingClub Loan Data (Kaggle)](https://www.kaggle.com/datasets/wordsforthewise/lending-club)
- **Size**: ~1.3 million loans, 145 columns
- Data Source too large to upload to repo, please see the above link for raw data

---


## 🧹 Data Preprocessing with Python

### Steps:
[Data Cleaning](./Banking_Data_Cleaning.py) 
- Read & Subset raw LendingClub dataset (~1.3M rows)
- Filtered for relevant years (2015–2018)
- Removed high-null columns
- Renamed key columns (e.g., `int_rate` → `Interest Rate %`, `dti` → `Debt-to-Income Ratio (DTI)`)
- Converted percentages and currency fields

**Calculated:**

- Default Flags (for classification)
- Aggregated Loan Amounts
- Default Rate %, Avg Interest by DTI, Grade, and Purpose


---

## 📊 Dashboard Highlights

Built in Tableau Public – [**See interactive dashboard:**] (https://public.tableau.com/views/BankingRiskandLoanPerformanceDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Key Visuals:

- **KPIs**: Total Loans, Total Loan \$, Total Interest, Avg Interest %, Default Rate %
- Grade vs Loan & Default Rate (Combo Chart)
- US Map of Default Rates
- Loan Purpose Tree Map (share of volume)
- Loan Status Funnel
- Monthly Trend (Loan Volume + Default %)
- DTI vs Interest Rate (scatter with trendline)

### Interactive Filters:

- Loan Purpose
- State

