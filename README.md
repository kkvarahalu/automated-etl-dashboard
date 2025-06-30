# Automated ETL + Dashboard System

##  Objective
Develop a user-friendly data science platform that allows users to:
- Upload raw datasets (CSV or Excel)
- Automatically handle missing values and outliers
- Generate summary statistics
- Create interactive dashboards with visualizations
- Export cleaned data and plots

---

## Dataset Used
- **Name:** Iris Dataset
- **File Format:** CSV
- **Rows:** 150
- **Columns:** sepal_length, sepal_width, petal_length, petal_width, species
---
## Features Implemented

1. **File Upload**
   - Supports `.csv` and `.xlsx`
   - Displays first 5 rows

2. **Missing Value Handling**
   - Drop rows/columns
   - Fill with mean, median, or mode

3. **Outlier Detection**
   - Z-score and IQR method
   - Boxplots and histograms
   - Option to remove outliers

4. **Summary Statistics**
   - Mean, median, mode
   - Std deviation, skewness, kurtosis
   - Value counts for categorical columns

5. **Data Visualizations**
   - Bar, Line, Pie, Box, Histogram, Scatter (using Plotly)
   - Plots saved as PNG

---

## Tech Stack

| Layer             | Tool                      |
|------------------ |---------------------------|
| UI & Interaction  | Streamlit (optional)      |
| Data Handling     | Pandas, NumPy             |
| Visualization     | Plotly, Matplotlib        |
| Report            | MS Word / PDF             |
| Hosting (optional)| Streamlit Cloud           |

---

##  Project Structure

automated-etl-dashboard/
├── app.py
├── requirements.txt
├── sample_data/
│ └── example.csv
├── assets/
│ └── plots.png
├── report/
│ └── Final_Report.pdf
└── README.md

---

## Learning Outcomes

- Data preprocessing with Pandas
- Missing value & outlier treatment
- Exploratory data analysis (EDA)
- Plotly chart creation and saving images
- Writing clean data science reports

---
## Author

**KALIMI KANAKAVARAHALU**  
**Internship:** Data Science Internship — June 2025