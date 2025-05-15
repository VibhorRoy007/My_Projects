import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap
from pandas_profiling import ProfileReport
from fpdf import FPDF

# Load the dataset
sales_data = pd.read_csv('supermarket_sales.csv')

# Preprocessing
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data.set_index('Date', inplace=True)

# Add new features
sales_data['Month'] = sales_data.index.month
sales_data['Weekday'] = sales_data.index.day_name()
sales_data['Hour'] = pd.to_datetime(sales_data['Time']).dt.hour

# Descriptive statistics
print(sales_data.describe())

# Save visualizations as images
def save_plot(fig, filename):
    fig.savefig(filename)
    plt.close(fig)

# Distribution of Customer Ratings
fig = plt.figure()
sns.histplot(sales_data['Rating'], kde=True)
plt.axvline(np.mean(sales_data['Rating']), c='green', ls='--', label='Mean')
plt.axvline(np.percentile(sales_data['Rating'], 25), c='red', ls='--', label='25th-75th Percentile')
plt.axvline(np.percentile(sales_data['Rating'], 75), c='red', ls='--')
plt.title('Distribution of Customer Ratings')
plt.legend()
save_plot(fig, 'distribution_of_ratings.png')

# Histograms of All Numeric Features
fig = plt.figure(figsize=(12, 10))
sales_data.hist()
plt.suptitle('Histograms of All Numeric Features', fontsize=16)
save_plot(fig, 'histograms_of_numeric_features.png')

# Transactions by Branch
fig = plt.figure()
sns.countplot(x='Branch', data=sales_data)
plt.title('Transactions by Branch')
save_plot(fig, 'transactions_by_branch.png')

# Payment Method Usage
fig = plt.figure()
sns.countplot(x='Payment', data=sales_data)
plt.title('Payment Method Usage')
save_plot(fig, 'payment_method_usage.png')

# Gross Income by Gender
fig = plt.figure()
sns.boxplot(x='Gender', y='gross income', data=sales_data)
plt.title('Gross Income by Gender')
save_plot(fig, 'gross_income_by_gender.png')

# Gross Income Distribution per Branch
fig = plt.figure()
sns.boxplot(x='Branch', y='gross income', data=sales_data)
plt.title('Gross Income Distribution per Branch')
save_plot(fig, 'gross_income_per_branch.png')

# Customer Rating vs Gross Income
fig = plt.figure()
sns.regplot(x='Rating', y='gross income', data=sales_data)
plt.title('Customer Rating vs Gross Income')
save_plot(fig, 'rating_vs_income.png')

# Daily Gross Income
daily_income = sales_data['gross income'].resample('D').sum()
fig = plt.figure(figsize=(12, 5))
daily_income.plot()
plt.title('Daily Gross Income')
plt.ylabel('Gross Income')
save_plot(fig, 'daily_gross_income.png')

# Calendar Heatmap of Daily Gross Income
fig = plt.figure(figsize=(12, 8))
calmap.calendarplot(daily_income)
plt.title('Calendar Heatmap of Daily Gross Income')
save_plot(fig, 'calendar_heatmap.png')

# Average Daily Gross Income Over Time
avg_daily = sales_data.groupby(sales_data.index).mean()
fig = plt.figure()
sns.lineplot(x=avg_daily.index, y=avg_daily['gross income'])
plt.title('Average Daily Gross Income Over Time')
save_plot(fig, 'average_daily_income.png')

# Income Distribution by Weekday
fig = plt.figure()
sns.boxplot(x='Weekday', y='gross income', data=sales_data)
plt.xticks(rotation=45)
plt.title('Income Distribution by Weekday')
save_plot(fig, 'income_by_weekday.png')

# Income by Hour of the Day
fig = plt.figure()
sns.boxplot(x='Hour', y='gross income', data=sales_data)
plt.title('Income by Hour of the Day')
save_plot(fig, 'income_by_hour.png')

# Correlation Heatmap
fig = plt.figure()
sns.heatmap(np.round(sales_data.corr(), 2), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
save_plot(fig, 'correlation_heatmap.png')

# Pairwise Relationships
fig = plt.figure()
sns.pairplot(sales_data.select_dtypes(include=['float64', 'int64']))
plt.suptitle("Pairwise Relationships", y=1.02)
save_plot(fig, 'pairwise_relationships.png')

# Check for duplicates and missing values
duplicates_count = sales_data.duplicated().sum()
print(f'Duplicates in Data: {duplicates_count}')
sales_data.drop_duplicates(inplace=True)

missing_ratio = sales_data.isna().sum() / len(sales_data)
print(f'Missing Values (Ratio):\n{missing_ratio}')

# Heatmap of missing data
fig = plt.figure()
sns.heatmap(sales_data.isnull(), cbar=False)
plt.title("Missing Data Heatmap")
save_plot(fig, 'missing_data_heatmap.png')

# Impute missing values
sales_data.fillna(sales_data.mean(numeric_only=True), inplace=True)
sales_data.fillna(sales_data.mode().iloc[0], inplace=True)

# Heatmap after imputation
fig = plt.figure()
sns.heatmap(sales_data.isnull(), cbar=False)
plt.title("Post-Imputation Missing Data Heatmap")
save_plot(fig, 'post_imputation_heatmap.png')

# Save the cleaned data
sales_data.to_csv('cleaned_supermarket_sales.csv')

# Generate a pandas profiling report
original_data = pd.read_csv('supermarket_sales.csv')
profile = ProfileReport(original_data, title="Supermarket Sales Data Report")
profile.to_file("data_report.html")

# Additional Features
sales_data['Sales_per_Customer'] = sales_data['Total'] / sales_data['Quantity']
sales_data['Sales_per_Customer'].fillna(sales_data['Sales_per_Customer'].mean(), inplace=True)

# Sales per Customer Distribution
fig = plt.figure()
sns.histplot(sales_data['Sales_per_Customer'], kde=True)
plt.title('Sales per Customer Distribution')
save_plot(fig, 'sales_per_customer_distribution.png')

# High vs Low Income Distribution
sales_data['High_Income'] = np.where(sales_data['gross income'] > sales_data['gross income'].median(), 'High', 'Low')
fig = plt.figure()
sns.countplot(x='High_Income', data=sales_data)
plt.title('High vs Low Income Distribution')
save_plot(fig, 'high_vs_low_income.png')

# Total Gross Income by Branch
branch_sales = sales_data.groupby('Branch')['gross income'].sum().sort_values(ascending=False)
fig = plt.figure(figsize=(10, 6))
branch_sales.plot(kind='bar')
plt.title('Total Gross Income by Branch')
plt.ylabel('Gross Income')
save_plot(fig, 'gross_income_by_branch.png')

# Gross Income by Payment Method
payment_sales = sales_data.groupby('Payment')['gross income'].sum().sort_values(ascending=False)
fig = plt.figure(figsize=(8, 8))
payment_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Gross Income by Payment Method')
save_plot(fig, 'gross_income_by_payment.png')

# Gross Income by Hour of the Day
hourly_sales = sales_data.groupby('Hour')['gross income'].sum()
fig = plt.figure()
sns.lineplot(x=hourly_sales.index, y=hourly_sales.values)
plt.title('Gross Income by Hour of the Day')
plt.ylabel('Gross Income')
save_plot(fig, 'gross_income_by_hour.png')

# Sales per Customer by Weekday
fig = plt.figure()
sns.boxplot(x='Weekday', y='Sales_per_Customer', data=sales_data)
plt.title('Sales per Customer by Weekday')
save_plot(fig, 'sales_per_customer_by_weekday.png')

# Create PDF report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Supermarket Sales Data Analysis Report", ln=True, align='C')
pdf.ln(10)

# Add images to PDF
images = [
    'distribution_of_ratings.png',
    'histograms_of_numeric_features.png',
    'transactions_by_branch.png',
    'payment_method_usage.png',
    'gross_income_by_gender.png',
    'gross_income_per_branch.png',
    'rating_vs_income.png',
    'daily_gross_income.png',
    'calendar_heatmap.png',
    'average_daily_income.png',
    'income_by_weekday.png',
    'income_by_hour.png',
    'correlation_heatmap.png',
    'pairwise_relationships.png',
    'missing_data_heatmap.png',
    'post_imputation_heatmap.png',
    'sales_per_customer_distribution.png',
    'high_vs_low_income.png',
    'gross_income_by_branch.png',
    'gross_income_by_payment.png',
    'gross_income_by_hour.png',
    'sales_per_customer_by_weekday.png'
]

for image in images:
    pdf.add_page()
    pdf.image(image, x=10, y=10, w=180)
    pdf.ln(10)

# Output PDF
pdf.output('supermarket_sales_report.pdf')

print("Report has been saved as 'supermarket_sales_report.pdf'.")
