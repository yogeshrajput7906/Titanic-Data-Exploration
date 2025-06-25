# Titanic Dataset - Exploratory Data Analysis (EDA)

This repository is part of **Task 2** for the **AI & ML Internship at Elevate Labs**.  
The objective was to explore and understand the Titanic dataset using EDA techniques.

---

## ✅ Objective

To analyze patterns, distributions, and correlations in the dataset using statistical summaries and visualizations.

---

## 🧪 Dataset Used
- `Cleaned_Titanic_Dataset.csv` (carried forward from Task 1)

---

## 🔍 Summary of Steps

1. **Summary Statistics**
   - Used `df.describe()` and `df.info()` to get an overview of data ranges, types, and missing values.

2. **Histograms**
   - Visualized distributions of numerical features.
   - Observed:
     - `Fare` is highly skewed (many low-fare passengers, few high).
     - Most passengers were in 3rd class.
     - `Age` concentrated between 20–40 years.

3. **Boxplots**
   - Used for `Age` and `Fare`.
   - Outliers clearly visible in `Fare`.
   - Slight outliers in `Age`.

4. **Correlation Heatmap**
   - Correlation matrix showed:
     - Strong inverse relation between `Pclass` and `Fare`.
     - Weak positive relation between `Fare` and `Survived`.

5. **Key Inferences**
   - 1st class passengers (lower `Pclass`) had better survival chances.
   - Females and children had higher survival rates.
   - High `Fare` somewhat correlated with survival.

---

## 📊 Libraries Used

- `pandas`
- `matplotlib`
- `seaborn`

---

## 📁 Files

- `task2_EDA.py` or `.ipynb` – Python script/notebook with EDA code
- `Cleaned_Titanic_Dataset.csv` – Input dataset
- `README.md` – Project overview

---

Created by [Yogesh Rajput]
