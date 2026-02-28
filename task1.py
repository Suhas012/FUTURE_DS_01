import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("sales_data.csv")

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# -----------------------------
# Data Cleaning & Feature Engineering
# -----------------------------
df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['TotalCost'] = df['Quantity'] * df['Cost']
df['Profit'] = df['Revenue'] - df['TotalCost']
df['Month'] = df['OrderDate'].dt.to_period('M')

# -----------------------------
# KPI Calculations
# -----------------------------
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
total_orders = df['OrderID'].nunique()
avg_order_value = total_revenue / total_orders
profit_margin = (total_profit / total_revenue) * 100

print("====== BUSINESS KPI SUMMARY ======")
print("Total Revenue: $", round(total_revenue,2))
print("Total Profit: $", round(total_profit,2))
print("Total Orders:", total_orders)
print("Average Order Value: $", round(avg_order_value,2))
print("Profit Margin: ", round(profit_margin,2), "%")

# -----------------------------
# 1️⃣ Revenue Trend
# -----------------------------
monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 2️⃣ Top Selling Products
# -----------------------------
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
top_products.plot(kind='bar')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# 3️⃣ Category Performance
# -----------------------------
category_performance = df.groupby('Category')[['Revenue','Profit']].sum()
print("\nCategory Performance:\n", category_performance)

category_performance.plot(kind='bar', figsize=(8,5))
plt.title("Category Revenue & Profit")
plt.show()

# -----------------------------
# 4️⃣ Regional Performance
# -----------------------------
region_performance = df.groupby('Region')[['Revenue','Profit']].sum()
print("\nRegional Performance:\n", region_performance)

region_performance.plot(kind='bar', figsize=(8,5))
plt.title("Regional Revenue & Profit")
plt.show()

# -----------------------------
# 5️⃣ Top 5 Profitable Products
# -----------------------------
top_profit_products = df.groupby('Product')['Profit'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Most Profitable Products:\n", top_profit_products)