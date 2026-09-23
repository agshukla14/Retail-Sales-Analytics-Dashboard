# 📊 Retail Sales Analytics Dashboard

An interactive web-based dashboard for analyzing retail sales performance across products, regions, customers, demographics, pricing, and order trends.

Built as a Data Analytics portfolio project using **HTML, CSS, JavaScript, and data-driven visualizations**.

---

## 🚀 Live Dashboard

👉 **[View Interactive Dashboard](https://agshukla14.github.io/Retail-Sales-Analytics-Dashboard/)**

---

## 📌 Project Overview

This project transforms a retail sales dataset of **500 orders** into an interactive Business Intelligence-style dashboard.

The dashboard enables users to explore:

- Revenue performance
- Sales trends over time
- Product category performance
- Regional performance
- Customer demographics
- Pricing and quantity relationships
- Top-performing transactions
- Dynamic business insights

Users can interact with the dashboard using multiple filters and instantly analyze the resulting metrics and visualizations.

---

## 📊 Dataset

The dataset contains **500 retail transactions** with the following attributes:

| Column | Description |
|---|---|
| `Order_ID` | Unique order identifier |
| `Order_Date` | Date of the transaction |
| `Customer_ID` | Customer identifier |
| `Gender` | Customer gender |
| `Age` | Customer age |
| `Region` | Sales region |
| `Product_Category` | Product category |
| `Price` | Selling price per unit |
| `Quantity` | Quantity purchased |

### Derived Metric

**Revenue = Price × Quantity**

---

## 📈 Dashboard Features

### KPI Overview

The dashboard provides key performance indicators including:

- 💰 Total Revenue
- 🧾 Total Orders
- 📦 Total Quantity Sold
- 💵 Average Order Value
- 🏷️ Average Selling Price
- 👥 Unique Customers

Additional customer and pricing metrics are also available.

### Interactive Filters

Users can dynamically filter the dashboard by:

- 📅 Date Range
- 🌎 Region
- 🛍️ Product Category
- 👤 Gender
- 🎂 Age Bracket

All dashboard metrics and visualizations update based on the selected filters.

### Visual Analysis

The dashboard includes:

- 📈 Sales Trend Analysis
- 🛍️ Product Category Analysis
- 🌎 Regional Performance
- 👥 Gender Distribution
- 🎂 Age Group Analysis
- 💰 Price vs Quantity Analysis
- 🏆 Top Performers
- 📋 Transaction-Level Data
- 💡 Dynamic Key Insights

---

## 🔍 Key Analytical Questions

The dashboard is designed to answer questions such as:

1. What is the overall revenue generated?
2. How does revenue change over time?
3. Which product categories generate the most revenue?
4. Which regions contribute the most sales?
5. How does purchasing behavior differ across customer demographics?
6. What is the relationship between product price and quantity sold?
7. Which transactions contribute the most revenue?
8. How do the KPIs change when different customer or product filters are applied?

---

## 🛠️ Technologies Used

- **HTML5** — Dashboard structure
- **CSS3** — Responsive styling and UI
- **JavaScript** — Data processing and dashboard interactions
- **SVG** — Data visualizations
- **CSV** — Source dataset
- **Git & GitHub** — Version control
- **GitHub Pages** — Dashboard deployment

---

## 📁 Project Structure

```text
Retail-Sales-Analytics-Dashboard/
│
├── index.html              # Dashboard interface
├── styles.css              # Dashboard styling
├── app.js                  # Dashboard logic and interactions
├── data.js                 # Processed dataset
├── retail_sales.csv        # Original dataset
│
├── export_json.py          # Data export utility
├── build_standalone.py     # Standalone build utility
├── validate_data.py        # Dataset validation
├── test_dashboard.js       # Dashboard testing
│
└── README.md               # Project documentation