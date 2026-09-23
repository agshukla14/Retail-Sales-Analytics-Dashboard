# 📊 Retail Sales Analytics Dashboard

An interactive **Retail Sales Analytics Dashboard** built to analyze sales performance, customer behavior, product categories, and regional trends.

The project transforms a retail sales dataset into an interactive Business Intelligence-style dashboard using **HTML, CSS, and Vanilla JavaScript**.

---

## 🚀 Live Dashboard

👉 [View Interactive Dashboard](https://agshukla14.github.io/Retail-Sales-Dashboard-Excel/)
---

## 📌 Project Overview

This dashboard provides an interactive way to explore retail sales data and answer important business questions such as:

- What is the total revenue generated?
- How many orders were placed?
- Which product category generates the most revenue?
- Which region performs best?
- How does revenue change over time?
- Which customer demographics contribute the most revenue?
- What is the relationship between price and quantity?
- Which orders generate the highest revenue?

---

## 📂 Dataset

The dataset contains **500 retail orders** with the following attributes:

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of the order |
| Customer_ID | Customer identifier |
| Gender | Customer gender |
| Age | Customer age |
| Region | Customer/order region |
| Product_Category | Product category |
| Price | Unit price |
| Quantity | Quantity purchased |

### Derived Metric

**Revenue = Price × Quantity**

---

## 📊 Dashboard Features

### KPI Cards

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value
- Average Selling Price
- Unique Customers
- Revenue per Customer
- Orders per Customer
- Average Quantity per Order

### 🔎 Interactive Filters

- Order Date
- Region
- Product Category
- Gender
- Age Bracket

The dashboard also includes a **Reset Filters** option.

### 📈 Sales Trend Analysis

Interactive analysis with:

- Daily
- Monthly
- Quarterly

Metrics:

- Revenue
- Quantity
- Orders

### 🛍️ Product Category Analysis

Analyze category performance using:

- Revenue
- Quantity
- Category-level summaries

### 🌎 Regional Analysis

Analyze:

- Revenue by Region
- Orders by Region
- Regional performance
- Average Order Value

### 👥 Customer Demographics

Analyze customer behavior by:

**Gender**
- Revenue
- Orders
- Quantity

**Age Brackets**
- Under 18
- 18–25
- 26–35
- 36–45
- 46–55
- 56+

### 📦 Price vs Quantity Analysis

Interactive scatter plot analyzing the relationship between:

**Price ↔ Quantity**

The visualization provides transaction-level information on hover.

### 🏆 Top Performers

The dashboard identifies:

- Top product categories by revenue
- Top regions by revenue
- Highest-value orders

The transaction table is sortable and responds to applied filters.

### 💡 Dynamic Business Insights

The dashboard automatically generates business insights based on the currently selected filters.

---

## 🛠️ Technologies Used

- HTML5
- CSS3
- JavaScript
- SVG
- Python
- Git
- GitHub

---

## 📁 Project Structure

```text
retail-sales-analytics-dashboard/
│
├── index.html
├── styles.css
├── app.js
├── data.js
├── retail_sales.csv
│
├── build_standalone.py
├── export_json.py
├── validate_data.py
├── test_dashboard.js
│
├── README.md
└── .gitignore