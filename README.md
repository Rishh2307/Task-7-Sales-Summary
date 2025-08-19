# Task-7-Sales-Summary
Basic sales summary using Python, SQLite, and Matplotlib (Data Analyst Internship Task 7)

# Sales Summary using Python and SQLite

## 📌 Project Overview
This project connects Python to a SQLite database (`sales_data.db`), runs SQL queries to calculate **total quantity sold** and **total revenue by product**, and visualizes the results with Matplotlib.  
It was completed as part of **Data Analyst Internship – Task 7**.

## 📂 Files in Repository
- `sales_summary.py` → Python script (SQL + visualization)  
- `sales_data.db` → SQLite database with sales table  
- `sales_chart.png` → Bar chart of revenue by product  
- `README.md` → Project documentation  
- `docs/TASK 7 DA.pdf` → Task instructions (optional)  

## 🛠️ Method
1. Connected to SQLite database using `sqlite3`  
2. Ran SQL query:  
   ```sql
   SELECT product, 
          SUM(quantity) AS total_qty, 
          SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;
