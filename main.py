import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from ydata_profiling import ProfileReport

# Load and clean data
df = pd.read_csv("data.csv")
df.drop(columns='Invoice ID', inplace=True)

# DateTime transformation
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%m/%d/%Y %H:%M')
df.drop(columns=['Date', 'Time'], inplace=True)

# Feature engineering
df['Month'] = df['DateTime'].dt.month
df['Weekday'] = df['DateTime'].dt.day_name()
df['Hour'] = df['DateTime'].dt.hour

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["savefig.dpi"] = 150

# Helper function to save plots
def save_plot(filename):
    plt.tight_layout()
    plt.savefig(filename)
    plt.clf()

# Rating distribution
sns.histplot(df["Rating"], kde=True)
plt.title("Rating Distribution")
save_plot("rating_distribution.png")

sns.kdeplot(df["Rating"], shade=True)
plt.title("Rating KDE")
save_plot("rating_kde_plot.png")

# Sales by branch
branch_sales = df.groupby('Branch')['Total'].sum().reset_index()
sns.barplot(x='Branch', y='Total', data=branch_sales)
plt.title("Total Sales by Branch")
save_plot("total_sales_by_branch.png")

sns.boxplot(x='Branch', y='Total', data=df)
plt.title("Sales Distribution by Branch")
save_plot("sales_distribution_by_branch.png")

# Monthly sales
monthly_sales = df.groupby(['Branch', 'Month'])['Total'].sum().reset_index()
sns.barplot(data=monthly_sales, x='Month', y='Total', hue='Branch')
plt.title("Monthly Sales by Branch")
save_plot("monthly_sales_by_branch.png")

# Payment method
df['Payment'].value_counts().plot.pie(autopct='%1.1f%%', label='', shadow=True)
plt.title("Payment Method Distribution")
save_plot("payment_distribution.png")

# Rating vs gross income
sns.scatterplot(x='Rating', y='gross income', data=df)
plt.title("Rating vs Gross Income")
save_plot("rating_vs_gross_income.png")

# Gross income by branch & gender
sns.boxplot(x='Branch', y='gross income', data=df)
plt.title("Gross Income by Branch")
save_plot("gross_income_by_branch.png")

sns.barplot(x='Gender', y='gross income', data=df)
plt.title("Gross Income by Gender")
save_plot("gross_income_by_gender.png")

# ANOVA test
female = df[df['Gender'] == 'Female']['gross income']
male = df[df['Gender'] == 'Male']['gross income']
stat, p = stats.f_oneway(female, male)
print(f"ANOVA Gender vs Gross Income: F={stat:.2f}, p={p:.4f}")

# Product line analysis
sns.barplot(x='Product line', y='gross income', data=df)
plt.title("Gross Income by Product Line")
plt.xticks(rotation=45)
save_plot("gross_income_by_product_line.png")

sns.boxplot(x='Quantity', y='Product line', data=df)
plt.title("Quantity by Product Line")
save_plot("quantity_by_product_line.png")

# Weekly sales
sns.countplot(x='Weekday', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title("Sales by Weekday")
save_plot("sales_by_weekday.png")

# Hourly sales
sns.lineplot(x='Hour', y='Quantity', data=df)
plt.title("Sales by Hour")
save_plot("sales_per_hour.png")

# City-wise income
sns.barplot(x='City', y='gross income', data=df)
plt.title("Gross Income by City")
save_plot("gross_income_by_city.png")

# Pairplot
sns.pairplot(df[['Total','gross income','Quantity','Rating']])
plt.suptitle("Pairwise Relationships", y=1.02)
plt.savefig("pairwise_plot.png")
plt.clf()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
save_plot("correlation_heatmap.png")

# 🔥 New Feature 1: Sales by gender & product line
avg_sales = df.groupby(['Gender', 'Product line'])['Total'].mean().unstack()
avg_sales.plot(kind='bar', stacked=True)
plt.title("Avg Sales by Gender & Product Line")
plt.ylabel("Average Total")
save_plot("avg_sales_by_gender_product.png")

# 🔥 New Feature 2: Top 5 hours by gross income
top_hours = df.groupby('Hour')['gross income'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=top_hours.index, y=top_hours.values)
plt.title("Top 5 Hours by Gross Income")
save_plot("top_hours_gross_income.png")

# 🔥 New Feature 3: Customer type vs total purchase
sns.boxplot(x='Customer type', y='Total', data=df)
plt.title("Customer Type vs Total Purchase")
save_plot("customer_type_total_purchase.png")

# Export files
report = ProfileReport(df, title='Supermarket Sales Report', explorative=True)
report.to_file("supermarket_data_report.html")
df.to_csv("enhanced_supermarket_data.csv", index=False)
