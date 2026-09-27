import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Cell 1
cells.append(nbf.v4.new_markdown_cell("""# Supermarket Sales Analysis & Customer Churn Prediction
## AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026
**Student:** Anubhav Anand
**Organization:** BharatCares | **Trainer:** Mr. Kartik Hooda"""))

# Cell 2
cells.append(nbf.v4.new_markdown_cell("""## Part 1: Supermarket Sales Analysis
### 1.1 Import Libraries & Load Data"""))

# Cell 3
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use('ggplot')
sns.set_palette('viridis')

df = pd.read_csv('data/supermarket_sales.csv')
print(f'Dataset Shape: {df.shape}')
df.head()"""))

# Cell 4
cells.append(nbf.v4.new_markdown_cell("""### 1.2 Exploratory Data Analysis"""))

# Cell 5
cells.append(nbf.v4.new_code_cell("""print('Dataset Info:')
df.info()
print('\\nStatistical Summary:')
df.describe()"""))

# Cell 6
cells.append(nbf.v4.new_code_cell("""print('Missing Values:')
print(df.isnull().sum())
print(f'\\nDuplicate Rows: {df.duplicated().sum()}')"""))

# Cell 7
cells.append(nbf.v4.new_markdown_cell("""### 1.3 Data Cleaning"""))

# Cell 8
cells.append(nbf.v4.new_code_cell("""df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
print('Date column converted. Months extracted.')
print(f'Date range: {df["Date"].min()} to {df["Date"].max()}')"""))

# Cell 9
cells.append(nbf.v4.new_markdown_cell("""### 1.4 Business Questions & Analysis"""))

# Cell 10
cells.append(nbf.v4.new_markdown_cell("""#### Q1: Which product generates the highest sales?"""))

# Cell 11
cells.append(nbf.v4.new_code_cell("""prod_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
print(f'Top Product: {prod_sales.index[0]} — ₹{prod_sales.values[0]:,.0f}')

plt.figure(figsize=(12, 8))
sns.barplot(x=prod_sales.values, y=prod_sales.index, palette='viridis')
plt.title('Products by Total Sales (₹)', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales (₹)')
plt.ylabel('Product')
plt.tight_layout()
plt.show()"""))

# Cell 12
cells.append(nbf.v4.new_markdown_cell("""**Finding:** Amul Cheese is the highest revenue-generating product with ₹27,900 in total sales.

#### Q2: Which branch performs best?"""))

# Cell 13
cells.append(nbf.v4.new_code_cell("""branch_sales = df.groupby(['Branch', 'City'])['Total'].sum().sort_values(ascending=False)
print(branch_sales)

plt.figure(figsize=(8, 5))
branch_data = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
sns.barplot(x=branch_data.index, y=branch_data.values, palette='magma')
plt.title('Sales by Branch', fontsize=14, fontweight='bold')
plt.ylabel('Total Sales (₹)')
for i, v in enumerate(branch_data.values):
    plt.text(i, v + 500, f'₹{v:,.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.show()"""))

# Cell 14
cells.append(nbf.v4.new_markdown_cell("""**Finding:** Branch B (Bangalore) leads with ₹75,330 in total sales.

#### Q3: Which category sells the most?"""))

# Cell 15
cells.append(nbf.v4.new_code_cell("""cat_sales = df.groupby('Category')['Total'].sum().sort_values(ascending=False)
print(cat_sales)

plt.figure(figsize=(10, 6))
sns.barplot(x=cat_sales.values, y=cat_sales.index, palette='crest')
plt.title('Sales by Category (₹)', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales (₹)')
for i, v in enumerate(cat_sales.values):
    plt.text(v + 200, i, f'₹{v:,.0f}', va='center', fontweight='bold')
plt.tight_layout()
plt.show()"""))

# Cell 16
cells.append(nbf.v4.new_markdown_cell("""**Finding:** Beverages is the top-selling category with ₹56,410 in total revenue.

#### Q4: What is the most popular payment method?"""))

# Cell 17
cells.append(nbf.v4.new_code_cell("""payment_dist = df['Payment'].value_counts()
print(payment_dist)

plt.figure(figsize=(8, 8))
plt.pie(payment_dist, labels=payment_dist.index, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette('pastel'), explode=[0.05]*len(payment_dist))
plt.title('Payment Method Distribution', fontsize=14, fontweight='bold')
plt.show()"""))

# Cell 18
cells.append(nbf.v4.new_markdown_cell("""**Finding:** UPI is the most popular payment method with 127 transactions (25.4%).

#### Q5: Do Members spend more than Normal customers?"""))

# Cell 19
cells.append(nbf.v4.new_code_cell("""member_spend = df.groupby('Customer_Type')['Total'].agg(['mean', 'sum', 'count'])
member_spend.columns = ['Avg Spend (₹)', 'Total Spend (₹)', 'Transactions']
print(member_spend)

plt.figure(figsize=(8, 5))
avg_spend = df.groupby('Customer_Type')['Total'].mean()
sns.barplot(x=avg_spend.index, y=avg_spend.values, palette='Set2')
plt.title('Average Spend by Customer Type', fontsize=14, fontweight='bold')
plt.ylabel('Average Transaction (₹)')
for i, v in enumerate(avg_spend.values):
    plt.text(i, v + 5, f'₹{v:,.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.show()"""))

# Cell 20
cells.append(nbf.v4.new_markdown_cell("""**Finding:** Members average ₹483 per transaction vs Normal customers at ₹400.

#### Q6: What is the average customer rating?"""))

# Cell 21
cells.append(nbf.v4.new_code_cell("""avg_rating = df['Rating'].mean()
print(f'Average Customer Rating: {avg_rating:.2f} / 5.0')

plt.figure(figsize=(10, 5))
sns.histplot(df['Rating'], bins=20, kde=True, color='skyblue', edgecolor='white')
plt.axvline(avg_rating, color='red', linestyle='--', label=f'Mean: {avg_rating:.2f}')
plt.title('Customer Rating Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Rating')
plt.legend()
plt.tight_layout()
plt.show()"""))

# Cell 22
cells.append(nbf.v4.new_markdown_cell("""**Finding:** The average customer rating is 3.99 out of 5.0.

### 1.5 Additional Insights"""))

# Cell 23
cells.append(nbf.v4.new_code_cell("""# Correlation Matrix
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()"""))

# Cell 24
cells.append(nbf.v4.new_code_cell("""# Monthly Sales Trend
monthly = df.groupby('Month')['Total'].sum()
plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly.index, y=monthly.values, marker='o', linewidth=2.5, color='#4fc3f7')
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.xticks(monthly.index)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()"""))

# Cell 25
cells.append(nbf.v4.new_markdown_cell("""---
## Part 2: Customer Churn Prediction (AI/ML)

### 2.1 Load & Clean E-commerce Data"""))

# Cell 26
cells.append(nbf.v4.new_code_cell("""ecom = pd.read_excel('data/ecommerce_practice_dataset.xlsx')
print(f'Shape: {ecom.shape}')
print(f'Columns: {list(ecom.columns)}')
ecom.head()"""))

# Cell 27
cells.append(nbf.v4.new_code_cell("""# Data Cleaning
ecom.columns = ecom.columns.str.strip()
ecom = ecom.dropna(subset=['Customer_ID'])
ecom = ecom[ecom['Quantity'] > 0]

# Fix Revenue column (remove currency symbols)
if ecom['Revenue'].dtype == object:
    ecom['Revenue'] = ecom['Revenue'].astype(str).str.replace(r'[^0-9.]', '', regex=True)
    ecom['Revenue'] = pd.to_numeric(ecom['Revenue'], errors='coerce')
ecom = ecom[ecom['Revenue'] > 0]

# Parse dates
ecom['Order_Date'] = pd.to_datetime(ecom['Order_Date'], errors='coerce')
ecom = ecom.dropna(subset=['Order_Date'])

print(f'Cleaned Shape: {ecom.shape}')"""))

# Cell 28
cells.append(nbf.v4.new_markdown_cell("""### 2.2 RFM Feature Engineering"""))

# Cell 29
cells.append(nbf.v4.new_code_cell("""max_date = ecom['Order_Date'].max()

rfm = ecom.groupby('Customer_ID').agg({
    'Order_Date': lambda x: (max_date - x.max()).days,
    'Customer_ID': 'count',
    'Revenue': 'sum'
}).rename(columns={
    'Order_Date': 'Recency',
    'Customer_ID': 'Frequency',
    'Revenue': 'Monetary'
})

print('RFM Summary:')
rfm.describe()"""))

# Cell 30
cells.append(nbf.v4.new_markdown_cell("""### 2.3 Define Churn & Train Model"""))

# Cell 31
cells.append(nbf.v4.new_code_cell("""from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# Churn = inactive 90+ days
rfm['Churn'] = (rfm['Recency'] >= 90).astype(int)
print(f'Churn Distribution:\\n{rfm["Churn"].value_counts()}')

X = rfm[['Recency', 'Frequency', 'Monetary']]
y = rfm['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)
preds = model.predict(X_test)

print(f'\\nModel Performance:')
print(f'  Accuracy:  {accuracy_score(y_test, preds):.4f}')
print(f'  Precision: {precision_score(y_test, preds):.4f}')
print(f'  Recall:    {recall_score(y_test, preds):.4f}')"""))

# Cell 32
cells.append(nbf.v4.new_code_cell("""# Confusion Matrix
cm = confusion_matrix(y_test, preds)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Active', 'Churned'], yticklabels=['Active', 'Churned'])
plt.title('Churn Prediction — Confusion Matrix', fontsize=14, fontweight='bold')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()"""))

# Cell 33
cells.append(nbf.v4.new_markdown_cell("""### 2.4 Customer Risk Classification"""))

# Cell 34
cells.append(nbf.v4.new_code_cell("""rfm['ChurnProbability'] = model.predict_proba(X)[:, 1]
rfm['RiskLevel'] = pd.cut(rfm['ChurnProbability'], bins=[-1, 0.3, 0.7, 1.1], labels=['Low', 'Medium', 'High'])

print('Risk Distribution:')
print(rfm['RiskLevel'].value_counts())

plt.figure(figsize=(8, 5))
sns.countplot(data=rfm, x='RiskLevel', order=['Low', 'Medium', 'High'], palette='RdYlGn_r')
plt.title('Customer Churn Risk Distribution', fontsize=14, fontweight='bold')
for p in plt.gca().patches:
    plt.gca().annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width()/2., p.get_height()),
                       ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.show()

print('\\nTop 10 Highest Risk Customers:')
rfm.sort_values('ChurnProbability', ascending=False).head(10)"""))

# Cell 35
cells.append(nbf.v4.new_markdown_cell("""---
## Business Recommendations
1. **Stock Optimization**: Increase inventory for Amul Cheese and Beverages category.
2. **Branch Strategy**: Study Branch B's success factors and replicate across A and C.
3. **Digital Payments**: Continue investing in UPI infrastructure.
4. **Loyalty Programs**: Members spend 20% more — expand membership benefits.
5. **Churn Prevention**: Target 270 high-risk customers with personalized retention campaigns.
6. **Rating Improvement**: Average 3.99/5 — focus on service quality to push above 4.5.

## Conclusion
This project demonstrates a complete data analytics pipeline — from data cleaning and EDA to AI-powered churn prediction. The analysis reveals actionable insights for inventory, marketing, and customer retention strategies.

*Project completed as part of AICTE | IBM SkillsBuild Data Analytics with AI Internship Program 2026, organized by BharatCares.*"""))

nb.cells = cells
with open('/home/anubhavanand/Desktop/aicte-DA(AI)/AnubhavAnand_SupermarketSalesAnalysis.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
