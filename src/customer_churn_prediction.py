import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import os

DATA_PATH = "/home/anubhavanand/Desktop/aicte-DA(AI)/data/ecommerce_practice_dataset.xlsx"
VIS_DIR = "/home/anubhavanand/Desktop/aicte-DA(AI)/visualizations/"
REPORTS_DIR = "/home/anubhavanand/Desktop/aicte-DA(AI)/reports/"
os.makedirs(VIS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def main():
    print("Loading Ecommerce dataset from:", DATA_PATH)
    try:
        df = pd.read_excel(DATA_PATH)
    except Exception as e:
        print(f"Error loading Excel: {e}")
        return

    print("Initial Shape:", df.shape)

    # Clean data
    df.columns = df.columns.str.strip()
    
    # Using specific columns found
    cust_col = 'Customer_ID'
    date_col = 'Order_Date'
    qty_col = 'Quantity'
    rev_col = 'Revenue'

    # Cleaning
    print("Cleaning Data...")
    df = df.dropna(subset=[cust_col])
    
    if qty_col in df.columns:
        df = df[df[qty_col] > 0]
        
    if rev_col in df.columns:
        if df[rev_col].dtype == object:
            df[rev_col] = df[rev_col].astype(str).str.replace(r'[^0-9.]', '', regex=True)
            df[rev_col] = pd.to_numeric(df[rev_col], errors='coerce')
        df = df[df[rev_col] > 0]
        
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df = df.dropna(subset=[date_col])

    # Calculate RFM
    print("Calculating RFM features...")
    df['TotalSpend'] = df[rev_col]
    max_date = df[date_col].max()
    
    rfm = df.groupby(cust_col).agg({
        date_col: lambda x: (max_date - x.max()).days,
        cust_col: 'count',
        'TotalSpend': 'sum'
    }).rename(columns={
        date_col: 'Recency',
        cust_col: 'Frequency',
        'TotalSpend': 'Monetary'
    })

    # Define Churn: Inactive for 90+ days
    rfm['Churn'] = (rfm['Recency'] >= 90).astype(int)

    print("RFM Summary:\n", rfm.head())
    print(f"Churn Distribution:\n{rfm['Churn'].value_counts(normalize=True)*100}")

    # Model Training
    print("\nTraining Logistic Regression Model...")
    X = rfm[['Recency', 'Frequency', 'Monetary']]
    y = rfm['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    
    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds, zero_division=0)
    rec = recall_score(y_test, preds, zero_division=0)
    cm = confusion_matrix(y_test, preds)

    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    
    # Save confusion matrix plot
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Churn Prediction Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(VIS_DIR, 'confusion_matrix.png'))
    plt.close()

    # Customer Risk Table
    probs = model.predict_proba(X)[:, 1]
    rfm['ChurnProbability'] = probs
    
    # Map probability to Risk Levels
    rfm['RiskLevel'] = pd.cut(rfm['ChurnProbability'], bins=[-1, 0.3, 0.7, 1.1], labels=['Low', 'Medium', 'High'])
    
    print("\nCustomer Risk Table Summary:")
    print(rfm['RiskLevel'].value_counts())
    
    risk_table_path = os.path.join(REPORTS_DIR, 'customer_risk_table.csv')
    rfm.to_csv(risk_table_path)
    print(f"Saved risk table to {risk_table_path}")

    # Plot Risk Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(data=rfm, x='RiskLevel', order=['Low', 'Medium', 'High'], palette='Reds')
    plt.title('Customer Churn Risk Distribution')
    plt.savefig(os.path.join(VIS_DIR, 'risk_distribution.png'))
    plt.close()

    print("Customer Churn Prediction Complete!")

if __name__ == "__main__":
    main()
