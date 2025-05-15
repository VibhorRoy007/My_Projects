# Exploratory Data Analysis of Supermarket Sales

This repository contains the code for an Exploratory Data Analysis (EDA) project on supermarket sales. The project leverages Python and its powerful data science libraries to import, clean, process, explore, and visualize supermarket sales data, aiming to uncover actionable insights. The analysis delves into various aspects of sales, including customer ratings, branch performance, payment methods, product lines, and temporal sales patterns.

# Dataset Used

The primary dataset used for this analysis is `data.csv`. It is assumed to contain transactional sales data including details like invoice ID, branch, city, customer type, gender, product line, unit price, quantity, total, date, time, payment method, cost of goods sold (cogs), gross margin percentage, gross income, and customer ratings.

# Project Objectives

The main objectives of this project are:

1.  **Data Ingestion and Preparation**: Load the raw sales data, perform necessary cleaning operations (e.g., dropping irrelevant columns), and transform data types (e.g., creating a unified 'DateTime' object).
2.  **Feature Engineering**: Create new, insightful features from existing data, such as extracting 'Month', 'Weekday', and 'Hour' from timestamps to facilitate time-based analysis.
3.  **Comprehensive EDA**: Conduct a thorough exploratory analysis to understand underlying patterns, distributions, and relationships within the data. This includes:
    * Analyzing customer ratings and sales distributions.
    * Comparing sales performance across different branches, months, weekdays, and hours.
    * Investigating payment method preferences.
    * Examining the relationship between variables like customer ratings and gross income.
    * Analyzing sales and income by product lines, customer demographics (gender), and city.
4.  **Statistical Analysis**: Apply statistical tests (e.g., ANOVA) to validate observations, such as differences in gross income between genders.
5.  **Targeted Insights Generation**: Explore specific business questions through custom analyses, such as average sales by gender and product line, identifying peak sales hours, and comparing purchase behavior of different customer types.
6.  **Data Visualization**: Create a wide range of clear and informative visualizations using Matplotlib and Seaborn to present findings effectively.
7.  **Automated Reporting and Data Export**: Generate an automated data profiling report using `ydata-profiling` for a quick and comprehensive overview of the dataset, and export the cleaned, enhanced dataset for future use.

# Project Structure

The project is implemented in Python and follows these key steps:

**Task 1: Setup and Initial Data Handling**
1.  Import necessary libraries: `pandas` for data manipulation, `matplotlib.pyplot` and `seaborn` for visualization, `scipy.stats` for statistical tests, and `ydata_profiling` for report generation.
2.  Load the dataset from `data.csv` into a pandas DataFrame.
3.  Perform initial cleaning: Drop the 'Invoice ID' column.

**Task 2: Data Transformation and Feature Engineering**
1.  **DateTime Conversion**: Combine 'Date' and 'Time' columns into a single 'DateTime' column (pandas datetime object) and drop the original 'Date' and 'Time' columns.
2.  **New Time-Based Features**: Extract 'Month', 'Weekday' (day name), and 'Hour' from the 'DateTime' column to enable granular temporal analysis.

**Task 3: Exploratory Data Analysis and Visualization**
*Global plot settings are configured using `seaborn.set()` and `matplotlib.rcParams` for consistent styling and image quality. A helper function `save_plot()` is defined to save figures.*

1.  **Rating Analysis**:
    * Visualize the distribution of 'Rating' using `sns.histplot` (with KDE) and a separate `sns.kdeplot`.
2.  **Sales by Branch**:
    * Calculate and plot total sales by 'Branch' using `sns.barplot`.
    * Display the sales distribution per 'Branch' using `sns.boxplot`.
3.  **Monthly Sales Analysis**:
    * Visualize 'Monthly Sales by Branch' using `sns.barplot`, grouping by 'Branch' and 'Month'.
4.  **Payment Method Insights**:
    * Plot the distribution of 'Payment' methods using a pie chart.
5.  **Relationship Analysis**:
    * Explore 'Rating vs Gross Income' using `sns.scatterplot`.
6.  **Income Analysis by Demographics and Location**:
    * Visualize 'Gross Income by Branch' using `sns.boxplot`.
    * Visualize 'Gross Income by Gender' using `sns.barplot`.
    * Conduct an ANOVA test to check for significant differences in 'gross income' between 'Female' and 'Male' customers.
    * Plot 'Gross Income by City' using `sns.barplot`.
7.  **Product Line Performance**:
    * Analyze 'Gross Income by Product line' using `sns.barplot`.
    * Visualize 'Quantity by Product line' using `sns.boxplot`.
8.  **Temporal Sales Patterns**:
    * Plot 'Sales by Weekday' (transaction counts) using `sns.countplot`.
    * Visualize 'Sales by Hour' (based on 'Quantity') using `sns.lineplot`.
9.  **Multivariate Analysis**:
    * Generate a `sns.pairplot` for key numerical columns: 'Total', 'gross income', 'Quantity', 'Rating'.
    * Create a 'Correlation Heatmap' for all numerical features using `sns.heatmap`.

**Task 4: Advanced Insights and Custom Analyses (🔥 New Features)**
1.  **Average Sales by Gender & Product Line**:
    * Calculate and visualize average 'Total' sales, grouped by 'Gender' and 'Product line', using a stacked bar chart.
2.  **Top 5 Hours by Gross Income**:
    * Identify and plot the top 5 hours generating the highest 'gross income'.
3.  **Customer Type vs Total Purchase**:
    * Compare 'Total' purchase amounts across different 'Customer type' categories using `sns.boxplot`.

**Task 5: Reporting and Data Export**
1.  **Automated Data Profiling**: Generate an HTML report using `ProfileReport` from `ydata-profiling` providing a comprehensive overview of the dataset. This is saved as `supermarket_data_report.html`.
2.  **Enhanced Data Export**: Save the processed and augmented DataFrame to a new CSV file named `enhanced_supermarket_data.csv`.
3.  All generated plots are saved as individual `.png` image files (e.g., `rating_distribution.png`, `total_sales_by_branch.png`, etc.).

# Libraries Used

* `pandas`: For data manipulation, cleaning, and analysis.
* `matplotlib.pyplot`: For creating static, interactive, and animated visualizations.
* `seaborn`: For making attractive and informative statistical graphics.
* `scipy.stats`: For statistical functions and tests (specifically ANOVA).
* `ydata-profiling`: For generating interactive EDA reports (formerly pandas-profiling).

# Output Files

This project generates the following key outputs:

* `enhanced_supermarket_data.csv`: The cleaned and feature-engineered dataset.
* `supermarket_data_report.html`: A comprehensive HTML data profiling report.
* **Image Files (`.png`) for Visualizations**:
    * `rating_distribution.png`
    * `rating_kde_plot.png`
    * `total_sales_by_branch.png`
    * `sales_distribution_by_branch.png`
    * `monthly_sales_by_branch.png`
    * `payment_distribution.png`
    * `rating_vs_gross_income.png`
    * `gross_income_by_branch.png`
    * `gross_income_by_gender.png`
    * `gross_income_by_product_line.png`
    * `quantity_by_product_line.png`
    * `sales_by_weekday.png`
    * `sales_per_hour.png`
    * `gross_income_by_city.png`
    * `pairwise_plot.png`
    * `correlation_heatmap.png`
    * `avg_sales_by_gender_product.png`
    * `top_hours_gross_income.png`
    * `customer_type_total_purchase.png`
    