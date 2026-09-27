from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

title = doc.add_heading('Data Analytics with AI — Project Report', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_paragraph('AICTE | IBM SkillsBuild Internship Program 2026')
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle.runs[0].font.size = Pt(14)
subtitle.runs[0].font.bold = True

doc.add_paragraph('Student: Anubhav Anand')
doc.add_paragraph('Organization: BharatCares')

doc.add_heading('1. Problem Statement', level=1)
doc.add_paragraph('The goal of this project is to analyze supermarket sales data to uncover insights about product performance, branch profitability, and customer behavior, and to build an AI/ML model to predict customer churn in an e-commerce setting.')

doc.add_heading('2. Dataset Description', level=1)
doc.add_paragraph('The analysis uses two primary datasets:')
doc.add_paragraph('1. Supermarket Sales Dataset: Contains 500 transactions across 3 branches.', style='List Bullet')
doc.add_paragraph('2. E-commerce Dataset: Contains 2000 orders for churn prediction.', style='List Bullet')

doc.add_heading('3. Tools & Technologies', level=1)
doc.add_paragraph('The following tools and libraries were used:')
doc.add_paragraph('Python, pandas, numpy, matplotlib, seaborn, scikit-learn', style='List Bullet')

doc.add_heading('4. Steps Used for Analysis', level=1)
doc.add_paragraph('1. Data Loading and Cleaning', style='List Number')
doc.add_paragraph('2. Exploratory Data Analysis (EDA)', style='List Number')
doc.add_paragraph('3. Feature Engineering (RFM Metrics)', style='List Number')
doc.add_paragraph('4. Machine Learning Modeling (Logistic Regression)', style='List Number')
doc.add_paragraph('5. Visualization and Reporting', style='List Number')

doc.add_heading('5. Live Analysis', level=1)
table = doc.add_table(rows=1, cols=2)
table.style = 'Table Grid'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Question'
hdr_cells[1].text = 'Finding'

qa_data = [
    ('Q1: Which product generates the highest sales?', 'Amul Cheese ₹27,900'),
    ('Q2: Which branch performs best?', 'Branch B (Bangalore) ₹75,330'),
    ('Q3: Which category sells the most?', 'Beverages ₹56,410'),
    ('Q4: What is the most popular payment method?', 'UPI 127 transactions'),
    ('Q5: Do Members spend more than Normal customers?', 'Members avg ₹483 vs Normal avg ₹400'),
    ('Q6: What is the average customer rating?', 'Average rating 3.99')
]

for q, a in qa_data:
    row_cells = table.add_row().cells
    row_cells[0].text = q
    row_cells[1].text = a

doc.add_heading('6. AI/ML Component', level=1)
doc.add_paragraph('Methodology: RFM Analysis followed by Logistic Regression for Churn Prediction.')
doc.add_paragraph('Model Metrics:')
doc.add_paragraph('Accuracy: 88.62%', style='List Bullet')
doc.add_paragraph('Precision: 86.67%', style='List Bullet')
doc.add_paragraph('Recall: 97.50%', style='List Bullet')
doc.add_paragraph('Risk Classification: High (270), Medium (57), Low (82)')

doc.add_heading('7. Business Recommendations', level=1)
doc.add_paragraph('1. Increase inventory for Amul Cheese and Beverages category.', style='List Bullet')
doc.add_paragraph('2. Study Branch B\'s success factors and replicate across A and C.', style='List Bullet')
doc.add_paragraph('3. Continue investing in UPI infrastructure.', style='List Bullet')
doc.add_paragraph('4. Expand membership benefits as Members spend 20% more.', style='List Bullet')
doc.add_paragraph('5. Target 270 high-risk customers with personalized retention campaigns.', style='List Bullet')
doc.add_paragraph('6. Focus on service quality to push average rating above 4.5.', style='List Bullet')

doc.add_heading('8. Conclusion', level=1)
doc.add_paragraph('This project successfully demonstrates a complete data analytics pipeline, from data cleaning and EDA to AI-powered churn prediction. The actionable insights generated can help optimize inventory, improve marketing strategies, and increase customer retention.')

doc.add_heading('9. Acknowledgements', level=1)
doc.add_paragraph('Special thanks to AICTE, IBM SkillsBuild, BharatCares, and Trainer Mr. Kartik Hooda for their guidance and support throughout this internship program.')

doc.save('/home/anubhavanand/Desktop/aicte-DA(AI)/AnubhavAnand_ProjectReport.docx')
