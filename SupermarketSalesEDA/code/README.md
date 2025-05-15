# Supermarket Sales Analysis and Reporting

Welcome to the Supermarket Sales Analysis and Reporting project.
In this project, we perform an in-depth Exploratory Data Analysis (EDA) on a supermarket sales dataset. We utilize Python libraries such as Pandas for data manipulation, NumPy for numerical operations, and Matplotlib & Seaborn for creating insightful data visualizations. Additionally, this project demonstrates feature engineering, handling of missing data, generation of an automated data profiling report, and culminates in the creation of a consolidated PDF report of findings.

# Dataset Used
Data link: [Link to data source: https://www.kaggle.com/aungpyaeap/supermarket-sales](https://www.kaggle.com/aungpyaeap/supermarket-sales)

This dataset contains sales transactions from three different supermarket branches over a period of three months.

# Project Objectives

This project aims to achieve the following:

1.  **Data Preprocessing & Feature Engineering**: Load, clean, and transform the raw sales data. Engineer new features from existing data (e.g., time-based features like 'Month', 'Weekday', 'Hour', and analytical features like 'Sales_per_Customer', 'High_Income') to enable deeper analysis.
2.  **Exploratory Data Analysis (EDA)**: Apply EDA techniques to understand the dataset's structure, uncover patterns, identify anomalies, and test hypotheses. This includes generating descriptive statistics.
3.  **Data Visualization**: Produce a wide array of static visualizations using Matplotlib and Seaborn to illustrate distributions, relationships between variables, and trends over time. This includes histograms, count plots, box plots, scatter plots, line plots, heatmaps, and calendar maps.
4.  **Missing Data and Duplicate Handling**: Implement strategies to identify and manage duplicate entries and missing values within the dataset to ensure data quality.
5.  **Correlation Analysis**: Investigate and visualize the correlations between different numerical features in the dataset.
6.  **Automated Reporting**: Generate an automated data profiling report using `pandas-profiling` for a quick overview of the dataset.
7.  **Consolidated PDF Report**: Compile key visualizations and findings into a structured PDF document using `FPDF` for easy sharing and review.

# Project Structure

The project is structured into the following key tasks:

**Task 1: Environment Setup and Data Loading**

1.  Import essential Python libraries: `pandas` for data manipulation, `numpy` for numerical computations, `matplotlib.pyplot` and `seaborn` for static visualizations, `calmap` for calendar heatmaps, `pandas_profiling` for automated EDA reports, and `fpdf` for PDF generation.
2.  Load the `supermarket_sales.csv` dataset into a pandas DataFrame.

**Task 2: Data Preprocessing and Feature Engineering**

1.  **Date Handling**: Convert the 'Date' column to datetime objects and set it as the DataFrame's index for time-series analysis.
2.  **Time-based Features**: Extract 'Month', 'Weekday' (name of the day), and 'Hour' from the timestamp to analyze sales patterns across different time granularities.
3.  **Calculated Features**:
    * Create 'Sales\_per\_Customer' by dividing 'Total' sales by 'Quantity'.
    * Create a binary 'High\_Income' feature based on whether the 'gross income' is above or below the median.

**Task 3: Initial Data Exploration and Automated Profiling**

1.  **Descriptive Statistics**: Calculate and print summary statistics (count, mean, std, min, max, quartiles) for numerical columns using `.describe()`.
2.  **Automated Data Report**: Generate a comprehensive HTML data profile report using `pandas_profiling.ProfileReport()` to get a quick overview of variable types, distributions, missing values, correlations, etc.

**Task 4: Univariate and Bivariate Analysis & Visualization**

1.  **Distribution Analysis**:
    * Plot the distribution of 'Customer Ratings' using `seaborn.histplot` with a KDE curve, overlaying mean and percentile lines.
    * Generate histograms for all numeric features using `pandas.DataFrame.hist()`.
    * Visualize the distribution of 'Sales\_per\_Customer'.
2.  **Categorical Variable Analysis**:
    * Use `seaborn.countplot` to show the frequency of transactions by 'Branch', 'Payment' method, and the distribution of 'High\_Income' vs 'Low\_Income' customers.
3.  **Relationship and Comparison Analysis**:
    * Employ `seaborn.boxplot` to compare 'gross income' distributions across 'Gender', 'Branch', 'Weekday', and 'Hour'.
    * Use `seaborn.regplot` to visualize the relationship between 'Customer Rating' and 'gross income'.
    * Analyze 'Sales\_per\_Customer' by 'Weekday' using box plots.
4.  **Time Series Analysis & Visualization**:
    * Resample 'gross income' daily (`.resample('D').sum()`) and plot it as a time series.
    * Create a calendar heatmap of daily gross income using `calmap.calendarplot`.
    * Plot the average daily gross income over time.
    * Analyze total 'gross income' by 'Branch' (bar plot), 'Payment' method (pie chart), and 'Hour' of the day (line plot).

**Task 5: Handling Duplicate Rows and Missing Values**

1.  **Duplicate Data**:
    * Identify and count duplicate rows in the dataset using `.duplicated().sum()`.
    * Remove duplicate rows using `.drop_duplicates()`.
2.  **Missing Data**:
    * Calculate and display the ratio of missing values for each column.
    * Visualize the presence of missing data before imputation using a `seaborn.heatmap`.
    * Impute missing numerical values with the mean of their respective columns and categorical (or object type) missing values with the mode.
    * Visualize the dataset again using a heatmap to confirm the absence of missing values post-imputation.
3.  **Saving Cleaned Data**: Export the cleaned and preprocessed DataFrame to a new CSV file (`cleaned_supermarket_sales.csv`).

**Task 6: Correlation Analysis**

1.  **Correlation Matrix**: Calculate the pairwise correlation between all numerical features using `.corr()`.
2.  **Heatmap Visualization**: Visualize the correlation matrix as a heatmap using `seaborn.heatmap` with annotations for easy interpretation.
3.  **Pairwise Relationships**: Generate `seaborn.pairplot` for a matrix of scatterplots between numerical variables, offering a visual way to spot relationships.

**Task 7: Report Generation**

1.  **Saving Visualizations**: Systematically save all generated plots as individual image files (e.g., `.png`).
2.  **PDF Report Creation**:
    * Initialize an `FPDF` object.
    * Add a title and introductory text to the PDF.
    * Iterate through the saved image files, adding each visualization to a new page in the PDF.
    * Save the final consolidated report as `supermarket_sales_report.pdf`.

# Libraries Used

* `pandas`: For data manipulation and analysis.
* `numpy`: For numerical operations.
* `matplotlib`: For creating static, animated, and interactive visualizations.
* `seaborn`: For making statistical graphics.
* `calmap`: For creating calendar heatmaps.
* `pandas-profiling`: For generating interactive EDA reports.
* `FPDF`: For creating PDF documents.

# Output Files

This project generates the following output files:

* `cleaned_supermarket_sales.csv`: The preprocessed and cleaned dataset.
* `data_report.html`: An interactive HTML report generated by pandas-profiling.
* `supermarket_sales_report.pdf`: A PDF document containing key visualizations from the analysis.
* Multiple `.png` image files for each generated plot, such as:
    * `distribution_of_ratings.png`
    * `histograms_of_numeric_features.png`
    * `transactions_by_branch.png`
    * `payment_method_usage.png`
    * `gross_income_by_gender.png`
    * `gross_income_per_branch.png`
    * `rating_vs_income.png`
    * `daily_gross_income.png`
    * `calendar_heatmap.png`
    * `average_daily_income.png`
    * `income_by_weekday.png`
    * `income_by_hour.png`
    * `correlation_heatmap.png`
    * `pairwise_relationships.png`
    * `missing_data_heatmap.png`
    * `post_imputation_heatmap.png`
    * `sales_per_customer_distribution.png`
    * `high_vs_low_income.png`
    * `gross_income_by_payment.png`
    * `sales_per_customer_by_weekday.png`
    * (and any other plots generated by your script)




