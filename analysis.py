import pandas as pd

# Load the dataset
sales = pd.read_csv("data/sales.csv")

# Convert date column to datetime
sales["date"] = pd.to_datetime(sales["date"])

# Calculate revenue for each order
sales["revenue"] = sales["price"] * sales["quantity"]

# Show the first 5 rows
print("First 5 rows:")
print(sales.head())

# Show basic information about the dataset
print("\nDataset information:")
print(sales.info())

# Show summary statistics
print("\nSummary statistics:")
print(sales.describe())

# Total revenue
total_revenue = sales["revenue"].sum()

print("\nTotal revenue:")
print(total_revenue)

# Total units sold
total_units = sales["quantity"].sum()

print("\nTotal units sold:")
print(total_units)

# Average order value
average_order_value = sales["revenue"].mean()

print("\nAverage order value:")
print(round(average_order_value, 2))

# Revenue by product
product_revenue = sales.groupby("product")["revenue"].sum()

print("\nRevenue by product:")
print(product_revenue)

# Best-performing product by revenue
best_product = product_revenue.idxmax()
best_revenue = product_revenue.max()

print("\nBest-performing product by revenue:")
print(best_product, "-", best_revenue)

# Units sold by product
product_quantity = sales.groupby("product")["quantity"].sum()

print("\nUnits sold by product:")
print(product_quantity)

# Best-selling product by quantity
top_selling_product = product_quantity.idxmax()
top_selling_quantity = product_quantity.max()

print("\nBest-selling product by quantity:")
print(top_selling_product, "-", top_selling_quantity)

# Revenue by category
category_revenue = sales.groupby("category")["revenue"].sum()

print("\nRevenue by category:")
print(category_revenue)

# Best-performing category
best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("\nBest-performing category:")
print(best_category, "-", best_category_revenue)

# Revenue by city
city_revenue = sales.groupby("city")["revenue"].sum()

print("\nRevenue by city:")
print(city_revenue)

# Best-performing city
best_city = city_revenue.idxmax()
best_city_revenue = city_revenue.max()

print("\nBest-performing city:")
print(best_city, "-", best_city_revenue)

# Create month column
sales["month"] = sales["date"].dt.to_period("M")

# Revenue by month
monthly_revenue = sales.groupby("month")["revenue"].sum()

print("\nRevenue by month:")
print(monthly_revenue)