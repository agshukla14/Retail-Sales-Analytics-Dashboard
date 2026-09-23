import pandas as pd
import numpy as np

df = pd.read_csv("retail_sales.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Price'] = pd.to_numeric(df['Price'])
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Age'] = pd.to_numeric(df['Age'])
df['Revenue'] = df['Price'] * df['Quantity']

print(f"Age min: {df['Age'].min()}, max: {df['Age'].max()}")

def get_age_group(age):
    if age < 18:
        return 'Under 18'
    elif 18 <= age <= 25:
        return '18-25'
    elif 26 <= age <= 35:
        return '26-35'
    elif 36 <= age <= 45:
        return '36-45'
    elif 46 <= age <= 55:
        return '46-55'
    else:
        return '56+'

df['Age_Group'] = df['Age'].apply(get_age_group)
age_summary = df.groupby('Age_Group').agg(
    Revenue=('Revenue', 'sum'),
    Orders=('Order_ID', 'nunique')
).reindex(['Under 18', '18-25', '26-35', '36-45', '46-55', '56+'], fill_value=0)
total_rev = df['Revenue'].sum()
age_summary['Rev_Share_Pct'] = (age_summary['Revenue'] / total_rev) * 100
print("\n=== AGE GROUP SUMMARY ===")
print(age_summary)

print("\n=== MONTHLY REVENUE ===")
df['Month'] = df['Order_Date'].dt.to_period('M')
month_summary = df.groupby('Month').agg(
    Revenue=('Revenue', 'sum'),
    Orders=('Order_ID', 'nunique'),
    Quantity=('Quantity', 'sum')
)
print(month_summary)
print("\nPeak Month:", month_summary['Revenue'].idxmax(), f"${month_summary['Revenue'].max():,.2f}")
print("Lowest Month:", month_summary['Revenue'].idxmin(), f"${month_summary['Revenue'].min():,.2f}")

print("\n=== QUARTERLY REVENUE ===")
df['Quarter'] = df['Order_Date'].dt.to_period('Q')
quarter_summary = df.groupby('Quarter').agg(
    Revenue=('Revenue', 'sum'),
    Orders=('Order_ID', 'nunique'),
    Quantity=('Quantity', 'sum')
)
print(quarter_summary)

print("\n=== TOP 10 ORDERS BY REVENUE ===")
top10 = df.sort_values('Revenue', ascending=False).head(10)[
    ['Order_ID', 'Order_Date', 'Product_Category', 'Region', 'Price', 'Quantity', 'Revenue']
]
print(top10.to_string(index=False))

print("\n=== TOP 5 CATEGORIES BY REVENUE ===")
cat_summary = df.groupby('Product_Category').agg(
    Revenue=('Revenue', 'sum'),
    Quantity=('Quantity', 'sum'),
    Orders=('Order_ID', 'nunique')
).sort_values('Revenue', ascending=False)
print(cat_summary)

print("\n=== TOP 5 REGIONS BY REVENUE ===")
reg_summary = df.groupby('Region').agg(
    Revenue=('Revenue', 'sum'),
    Quantity=('Quantity', 'sum'),
    Orders=('Order_ID', 'nunique')
).sort_values('Revenue', ascending=False)
print(reg_summary)
