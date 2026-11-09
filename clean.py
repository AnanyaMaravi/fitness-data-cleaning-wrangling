
# WEEK 3: PYTHON & DATA WRANGLING

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the dataset
df = pd.read_csv("data.csv")

print("Original Dataset:")
print(df.head())

# 2. Check dataset information
print("\nDataset Information:")
df.info()

# 3. Check statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 4. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Remove duplicate records
print("\nDuplicate Records:", df.duplicated().sum())
df = df.drop_duplicates()

# 6. Clean the Date column
df['Date'] = (
    df['Date']
    .astype('string')
    .str.strip()
    .str.strip("'")
)

# Correct the date format 20201226
df['Date'] = df['Date'].str.replace(
    r'^(\d{4})(\d{2})(\d{2})$',
    r'\1/\2/\3',
    regex=True
)

# Convert Date into datetime format
df['Date'] = pd.to_datetime(
    df['Date'],
    format='%Y/%m/%d',
    errors='coerce'
)

# 7. Handle missing Calories
median_calories = df['Calories'].median()

df['Calories'] = df['Calories'].fillna(
    median_calories
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 8. Identify suspicious records
print("\nUnusual Duration Records:")
print(df[df['Duration'] > 120])

print("\nPulse greater than Maxpulse:")
print(df[df['Pulse'] > df['Maxpulse']])

# 9. Filter rows
high_calories = df[df['Calories'] > 300]

print("\nWorkouts with Calories above 300:")
print(high_calories)

# 10. Create new columns
df['Calories_Per_Minute'] = np.where(
    df['Duration'] > 0,
    df['Calories'] / df['Duration'],
    np.nan
)

df['Workout_Intensity'] = np.where(
    df['Pulse'] >= 120,
    'High',
    'Moderate'
)

# 11. Create a filtered dataset for analysis
# Exclude suspicious duration and pulse records
analysis_df = df[
    (df['Duration'] <= 120) &
    (df['Duration'] > 0) &
    (df['Pulse'] <= df['Maxpulse'])
].copy()

# 12. Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

print("\nAnalysis Dataset:")
print(analysis_df.head())

# 13. Save cleaned datasets
df.to_csv("cleaned_fitness.csv", index=False)
analysis_df.to_csv("fitness_analysis.csv", index=False)

print("\nData Cleaning Completed!")

# VISUALIZATION

# 1. Duration Distribution
plt.figure(figsize=(8, 5))
plt.hist(analysis_df['Duration'], bins=10)
plt.title("Workout Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Workouts")
plt.show()

# 2. Calories Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=analysis_df, x='Calories', kde=True)
plt.title("Calories Burned Distribution")
plt.xlabel("Calories")
plt.show()

# 3. Pulse vs Calories
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=analysis_df,
    x='Pulse',
    y='Calories'
)
plt.title("Pulse vs Calories")
plt.show()

# 4. Workout Duration vs Calories
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=analysis_df,
    x='Duration',
    y='Calories'
)
plt.title("Duration vs Calories")
plt.show()

# 5. Calories by Workout Intensity
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=analysis_df,
    x='Workout_Intensity',
    y='Calories'
)
plt.title("Calories by Workout Intensity")
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    analysis_df.select_dtypes(include='number').corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()
plt.savefig('calories.png')

print("All Visualizations Completed!")
