# AICTE | IBM SkillsBuild - Data Analytics with AI Internship Project

**Student Name:** [Anubhav Anand]  
**College/University:** [Amity School of Engineering and Technology , Greater NOida ]  
**Project Track:** Data Analytics with AI  

## 1. Problem Statement
The retail and e-commerce industries accumulate vast amounts of transactional data. The main challenge is turning this raw data into actionable business intelligence. This project focuses on analyzing supermarket sales to uncover revenue-driving products, optimal branches, and customer behavior, alongside predicting customer churn in an e-commerce setting to proactively retain high-value customers.

## 2. Dataset Description
- **Supermarket Sales Dataset (`supermarket_sales.csv`)**: Contains transactional records of supermarket branches (Product line, Branch, Total, Payment method, Customer type, Rating, Date).
- **E-commerce Practice Dataset (`ecommerce_practice_dataset.xlsx`)**: Contains online retail transactions mapping customers to their orders (CustomerID, InvoiceDate, Quantity, UnitPrice).

## 3. Tools & Technologies Used
- Python 3
- Pandas, Numpy (Data Manipulation)
- Matplotlib, Seaborn (Data Visualization)
- Scikit-learn (Machine Learning - Logistic Regression)
- Openpyxl (Excel handling)

## 4. Project Structure
```
aicte-DA(AI)/
├── data/
│   ├── supermarket_sales.csv
│   └── ecommerce_practice_dataset.xlsx
├── src/
│   ├── supermarket_sales_analysis.py
│   └── customer_churn_prediction.py
├── visualizations/
│   ├── top_products_sales.png
│   ├── sales_by_branch.png
│   └── ... (other generated charts)
├── reports/
│   ├── project_report.md
│   └── customer_risk_table.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Key Findings
1. **Highest Sales Product:** Identified via grouping by Product Line, determining the category that brings maximum revenue.
2. **Best Performing Branch:** Branch level analysis highlighted the most profitable location.
3. **Most Sold Category:** Measured by quantity sold, showing pure volume drivers.
4. **Popular Payment Method:** Unveiled the preferred mode of payment among customers.
5. **Member vs Normal Spending:** Analyzed if loyalty program members spend significantly more than normal shoppers.
6. **Average Customer Rating:** Provided a macro view of customer satisfaction.

## 6. How to Run
1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run EDA script: `python src/supermarket_sales_analysis.py`
4. Run ML script: `python src/customer_churn_prediction.py`
5. Check `visualizations/` and `reports/` for outputs.

## 7. Business Recommendations
- Focus marketing and stock efforts on top-selling product categories and branches.
- Provide targeted discounts or incentives to high-risk churn customers identified in the Churn Prediction model.
- Leverage the most popular payment gateways to offer seamless checkout experiences.

## 8. Conclusion
The comprehensive analysis of both datasets yields clear operational directives for the supermarket and proactive retention strategies for the e-commerce platform.

## 9. Acknowledgements
Thank you to **AICTE**, **IBM SkillsBuild**, **BharatCares**, and **Mr. Kartik Hooda** for facilitating this internship and providing guidance throughout the learning process.
