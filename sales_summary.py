import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# SQL query to get total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Load query results into pandas DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Print the sales summary
print("Sales Summary:")
print(df)

# Plot bar chart for revenue
plt.figure(figsize=(6, 4))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.ylabel("Revenue ($)")
plt.title("Revenue by Product")
plt.tight_layout()

# Save and show chart
plt.savefig("sales_chart.png")
plt.show()
