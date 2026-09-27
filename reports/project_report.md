# Project Report: Data Analytics with AI

## 1. Problem Statement
The objective of this project is to analyze physical supermarket sales and online e-commerce transactions to extract meaningful business insights. Specifically, we aim to answer core business questions regarding product performance, branch profitability, and customer behavior. Furthermore, we seek to build a predictive model to identify customers at risk of churning, enabling proactive retention efforts.

## 2. Dataset Description
- **Supermarket Sales**: A structured CSV file containing attributes like Branch, Customer type, Product line, Unit price, Quantity, Total, Date, Payment, and Rating.
- **E-Commerce Dataset**: An Excel spreadsheet comprising transactional records, crucial for mapping Customer IDs, Invoice Dates, and spend amounts to compute Recency, Frequency, and Monetary (RFM) values.

## 3. Steps Used for Analysis
1. **Data Loading & Validation**: Checked shapes, data types, and missing values.
2. **Data Cleaning**: Stripped column names, formatted dates, handled negative quantities and missing IDs.
3. **Exploratory Data Analysis (EDA)**: Aggregated data to answer business queries.
4. **Visualization**: Created bar charts, pie charts, and heatmaps to represent findings visually.
5. **Feature Engineering (RFM)**: Transformed raw transactional data into customer-level RFM metrics.
6. **Machine Learning Modeling**: Trained and evaluated a Logistic Regression model for churn prediction.

## 4. Live Analysis (6 Key Questions)
*(Results are dynamically populated based on script execution)*
1. **Which product generates the highest sales?** Addressed by aggregating 'Total' over 'Product line'.
2. **Which branch performs best?** Addressed by summing 'Total' sales per 'Branch'.
3. **Which category sells the most?** Addressed by summing 'Quantity' per 'Product line'.
4. **What is the most popular payment method?** Addressed by analyzing value counts of the 'Payment' column.
5. **Do Members spend more than Normal customers?** Addressed by comparing the mean 'Total' spend between customer types.
6. **What is the average customer rating?** Calculated as the mean of the 'Rating' column.

## 5. AI/ML Component (Churn Prediction)
- **Features**: Recency (days since last purchase), Frequency (number of purchases), Monetary (total spend).
- **Definition of Churn**: Customers with zero activity in the last 90 days.
- **Model**: Logistic Regression.
- **Outcome**: A risk classification table dividing the customer base into Low, Medium, and High-risk segments, supplemented by a Confusion Matrix evaluating model accuracy.

## 6. Business Decisions
- Optimize inventory for top-selling product lines.
- Implement specialized retention campaigns for 'High' and 'Medium' risk customers.
- Expand loyalty programs if members prove to be significantly higher spenders.

## 7. Conclusion
Through structured data cleaning, EDA, and predictive modeling, we transitioned from raw data to actionable insights. The integration of Python-based visualization and ML pipelines demonstrates a robust approach to real-world retail analytics.
