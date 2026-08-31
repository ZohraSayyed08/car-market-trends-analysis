"""
Car Market Trends Analysis - Car Dekho Dataset
 VOIS & Vodafone Idea Foundation Data Analytics Internship- DIY Project 4
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ---- Load data ----
df = pd.read_csv('Car_Dekho_Data.csv')  # original raw file

# ---- Step 1: Understand the data ----
print(df.shape)
print(df.info())
print(df.describe(include='all').T)

# ---- Step 2: Data Quality Checks ----
# 2a. Duplicates
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().copy()

# 2b. Missing values
print(df.isna().sum())

# 2c. Category label consistency
for col in ['Fuel_Type', 'Seller_Type', 'Transmission']:
    print(col, df[col].unique())

# 2d. Clean whitespace in text fields
for col in ['Car_Name', 'Fuel_Type', 'Seller_Type', 'Transmission']:
    df[col] = df[col].astype(str).str.strip()

# 2e. Impossible / outlier values
outliers = df[df['Kms_Driven'] > 400000]
print("Flagged outliers (kept, but excluded from km-based chart):")
print(outliers)

# ---- Step 3: Feature engineering ----
max_year = df['Year'].max()
df['Car_Age'] = (max_year + 1) - df['Year']

df.to_csv('cleaned_data.csv', index=False)

# ---- Step 4: Analysis & Visualization ----
# Chart 1: Avg selling price by fuel type
avg_price_fuel = df.groupby('Fuel_Type')['Selling_Price'].mean().sort_values(ascending=False)
avg_price_fuel.plot(kind='bar', title='Average Selling Price by Fuel Type')
plt.tight_layout(); plt.savefig('chart1_price_by_fuel.png'); plt.close()

# Chart 2: Transmission counts
df['Transmission'].value_counts().plot(kind='bar', title='Cars by Transmission Type')
plt.tight_layout(); plt.savefig('chart2_transmission_count.png'); plt.close()

# Chart 3: Present vs Selling price scatter
sns.scatterplot(data=df, x='Present_Price', y='Selling_Price', hue='Fuel_Type')
plt.title('Present Price vs Selling Price')
plt.tight_layout(); plt.savefig('chart3_price_scatter.png'); plt.close()

# Chart 4: Price trend by car age
df.groupby('Car_Age')['Selling_Price'].mean().sort_index().plot(kind='line', marker='o')
plt.title('Average Selling Price by Car Age')
plt.tight_layout(); plt.savefig('chart4_price_by_age.png'); plt.close()

# Chart 5: Price distribution by seller type
sns.boxplot(data=df, x='Seller_Type', y='Selling_Price')
plt.title('Selling Price Distribution by Seller Type')
plt.tight_layout(); plt.savefig('chart5_box_seller.png'); plt.close()

print("Analysis complete.")
