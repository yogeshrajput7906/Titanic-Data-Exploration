# Re-import after file upload
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the newly uploaded dataset
file_path = "Cleaned_Titanic_Dataset.csv"
df = pd.read_csv(file_path)

# Generate summary statistics
print(df.describe())
print(df.info())

# Histograms for numeric features
df.hist(bins=20, edgecolor='black', figsize=(12, 8), grid=False)
plt.tight_layout()
plt.show()


# Boxplots for Age and Fare
boxplot_fig, boxplot_ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df[['Age', 'Fare']], ax=boxplot_ax)
plt.title('Boxplots of Age and Fare')
plt.show()

# Correlation matrix heatmap
corr = df.corr(numeric_only=True)
heatmap_fig, heatmap_ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=heatmap_ax)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Pairplot
pairplot_fig = sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass']].dropna(), hue='Survived')
plt.show()

# Save the dataset used for EDA
eda_output_path = "Cleaned_Titanic_Dataset.csv"
df.to_csv(eda_output_path, index=False)

eda_output_path
