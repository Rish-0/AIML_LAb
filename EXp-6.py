# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset, replace this with your own dataset
data = {
    'age': [25, 30, 35, np.nan, 45, 50, np.nan, 55],
    'salary': [50000, 54000, np.nan, 61000, 58000, 60000, 62000, np.nan],
    'gender': ['Male', 'Female', 'Male', 'Female', np.nan, 'Male', 'Female', 'Male'],
    'experience': [1, 3, 5, 6, 9, np.nan, 11, 12]
}

# Load the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Display the dataset with missing values
print("Original Dataset:")
print(df)

# 1. Handling Missing Values

# Option 1: Drop rows with missing values
df_dropped = df.dropna()
print("\nDataset after dropping missing values:")
print(df_dropped)

# Option 2: Impute missing values with the mean (for numerical columns)
df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
df['experience'].fillna(df['experience'].mean(), inplace=True)

# Impute missing values for categorical columns with the most frequent value
df['gender'].fillna(df['gender'].mode()[0], inplace=True)

print("\nDataset after imputing missing values:")
print(df)

# 2. Handling Outliers

# Let's visualize the data to identify outliers
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[['age', 'salary', 'experience']])
plt.title('Boxplot to Detect Outliers')
plt.show()

# Method 1: Removing outliers using the IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

# Apply outlier removal to the 'salary' column
df_no_outliers = remove_outliers(df, 'salary')

print("\nDataset after removing outliers in 'salary':")
print(df_no_outliers)

# Method 2: Capping outliers (limiting values to the 5th and 95th percentiles)
def cap_outliers(df, column):
    lower_cap = df[column].quantile(0.05)
    upper_cap = df[column].quantile(0.95)
    df[column] = np.where(df[column] < lower_cap, lower_cap, df[column])
    df[column] = np.where(df[column] > upper_cap, upper_cap, df[column])
    return df

# Apply capping to the 'age' column
df_capped = cap_outliers(df, 'age')

print("\nDataset after capping outliers in 'age':")
print(df_capped)

# Final dataset after preprocessing
print("\nFinal preprocessed dataset:")
print(df)
