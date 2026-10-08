import os
import pandas as pd
import matplotlib.pyplot as plt

# Create images folder if it does not exist
os.makedirs("images", exist_ok=True)

# Load the dataset
sales = pd.read_csv("data/sales.csv")

# Convert date column to datetime
sales["date"] = pd.to_datetime(sales["date"])

# Calculate revenue
sales["revenue"] = sales["price"] * sales["quantity"]

# Prepare grouped data
city_revenue = sales.groupby("city")["revenue"].sum()
product_revenue = sales.groupby("product")["revenue"].sum()
category_revenue = sales.groupby("category")["revenue"].sum()
product_quantity = sales.groupby("product")["quantity"].sum()

sales["month"] = sales["date"].dt.to_period("M")
monthly_revenue = sales.groupby("month")["revenue"].sum()

# Revenue by city
city_revenue.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue (AED)")
plt.tight_layout()
plt.savefig("images/revenue_by_city.png")
plt.close()

# Revenue by product
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (AED)")
plt.tight_layout()
plt.savefig("images/revenue_by_product.png")
plt.close()

# Revenue by category
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (AED)")
plt.tight_layout()
plt.savefig("images/revenue_by_category.png")
plt.close()

# Units sold by product
product_quantity.plot(kind="bar")
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig("images/units_sold_by_product.png")
plt.close()

# Monthly revenue trend
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (AED)")
plt.tight_layout()
plt.savefig("images/monthly_revenue_trend.png")
plt.close()

print("Charts saved successfully in the images folder.")