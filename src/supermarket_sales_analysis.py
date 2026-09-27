import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = "/home/anubhavanand/Desktop/aicte-DA(AI)/data/supermarket_sales.csv"
VIS_DIR = "/home/anubhavanand/Desktop/aicte-DA(AI)/visualizations/"
os.makedirs(VIS_DIR, exist_ok=True)

def main():
    print("Loading data from:", DATA_PATH)
    try:
        df = pd.read_csv(DATA_PATH)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    print("\n--- EDA ---")
    print(f"Shape: {df.shape}")
    print("Info:")
    df.info()
    print("\nDescribe:\n", df.describe(include='all'))
    print("\nNull values:\n", df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())

    # Data Cleaning
    print("\n--- Data Cleaning ---")
    # Clean column names (strip whitespace)
    df.columns = df.columns.str.strip()
    
    # Try common Date columns
    date_col = next((col for col in df.columns if 'date' in col.lower()), None)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df['Month'] = df[date_col].dt.month
        print(f"Parsed Date column: {date_col}")

    # Identify columns
    prod_col = next((c for c in df.columns if 'product' in c.lower() and 'line' in c.lower()), 'Product line')
    if prod_col not in df.columns: prod_col = next((c for c in df.columns if 'product' in c.lower()), None)
    
    branch_col = next((c for c in df.columns if 'branch' in c.lower()), None)
    total_col = next((c for c in df.columns if 'total' in c.lower()), None)
    qty_col = next((c for c in df.columns if 'quantity' in c.lower()), None)
    payment_col = next((c for c in df.columns if 'payment' in c.lower()), None)
    cust_col = next((c for c in df.columns if 'customer' in c.lower() and 'type' in c.lower()), None)
    rating_col = next((c for c in df.columns if 'rating' in c.lower()), None)

    print("\n--- Analysis & Business Questions ---")
    
    # 1. Which product generates the highest sales?
    print("\n1. Which product generates the highest sales?")
    if prod_col and total_col:
        prod_sales = df.groupby(prod_col)[total_col].sum().sort_values(ascending=False)
        print("Top Products by Sales:\n", prod_sales.head())
        plt.figure(figsize=(10, 6))
        sns.barplot(x=prod_sales.values, y=prod_sales.index, palette='viridis')
        plt.title('Top Products by Sales')
        plt.tight_layout()
        plt.savefig(os.path.join(VIS_DIR, 'top_products_sales.png'))
        plt.close()

    # 2. Which branch performs best?
    print("\n2. Which branch performs best?")
    if branch_col and total_col:
        branch_sales = df.groupby(branch_col)[total_col].sum().sort_values(ascending=False)
        print("Branch Performance:\n", branch_sales)
        plt.figure(figsize=(8, 5))
        sns.barplot(x=branch_sales.index, y=branch_sales.values, palette='magma')
        plt.title('Sales by Branch')
        plt.savefig(os.path.join(VIS_DIR, 'sales_by_branch.png'))
        plt.close()

    # 3. Which category sells the most?
    print("\n3. Which category sells the most (by quantity)?")
    if prod_col and qty_col:
        cat_qty = df.groupby(prod_col)[qty_col].sum().sort_values(ascending=False)
        print("Category Sales by Quantity:\n", cat_qty.head())
        plt.figure(figsize=(10, 6))
        sns.barplot(x=cat_qty.values, y=cat_qty.index, palette='crest')
        plt.title('Quantity Sold by Category')
        plt.tight_layout()
        plt.savefig(os.path.join(VIS_DIR, 'category_sales.png'))
        plt.close()

    # 4. What is the most popular payment method?
    print("\n4. What is the most popular payment method?")
    if payment_col:
        payment_dist = df[payment_col].value_counts()
        print("Payment Method Dist:\n", payment_dist)
        plt.figure(figsize=(8, 8))
        plt.pie(payment_dist, labels=payment_dist.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
        plt.title('Payment Method Distribution')
        plt.savefig(os.path.join(VIS_DIR, 'payment_method_distribution.png'))
        plt.close()

    # 5. Do Members spend more than Normal customers?
    print("\n5. Do Members spend more than Normal customers?")
    if cust_col and total_col:
        member_spend = df.groupby(cust_col)[total_col].mean().sort_values(ascending=False)
        print("Average Spend by Customer Type:\n", member_spend)
        plt.figure(figsize=(6, 5))
        sns.barplot(x=member_spend.index, y=member_spend.values, palette='Set2')
        plt.title('Average Spend by Customer Type')
        plt.savefig(os.path.join(VIS_DIR, 'spend_by_customer_type.png'))
        plt.close()

    # 6. What is the average customer rating?
    print("\n6. What is the average customer rating?")
    if rating_col:
        avg_rating = df[rating_col].mean()
        print(f"Overall Average Rating: {avg_rating:.2f}")
        plt.figure(figsize=(8, 5))
        sns.histplot(df[rating_col], bins=20, kde=True, color='skyblue')
        plt.title('Rating Distribution')
        plt.savefig(os.path.join(VIS_DIR, 'rating_distribution.png'))
        plt.close()

    # Correlation Matrix
    print("\nGenerating Correlation Matrix...")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.savefig(os.path.join(VIS_DIR, 'correlation_matrix.png'))
        plt.close()

    # Monthly sales trend
    if 'Month' in df.columns and total_col:
        print("\nGenerating Monthly Sales Trend...")
        monthly_sales = df.groupby('Month')[total_col].sum()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', linewidth=2)
        plt.title('Monthly Sales Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(monthly_sales.index)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.savefig(os.path.join(VIS_DIR, 'monthly_sales_trend.png'))
        plt.close()
        
    print("\nSupermarket Sales Analysis Complete!")

if __name__ == "__main__":
    main()
