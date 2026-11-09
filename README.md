# fitness-data-cleaning-wrangling
Data Cleaning and Wrangling using Python Pandas | Handling missing values, removing duplicates, filtering data, feature creation, and data visualization using Matplotlib and Seaborn.

## Project Overview
This project focuses on cleaning, processing, and analyzing a fitness dataset using Python. It demonstrates essential data wrangling techniques with Pandas and data visualization using Matplotlib and Seaborn.

The dataset contains workout-related information, including exercise duration, date, pulse rate, maximum pulse rate, and calories burned.

## Dataset Information

**Dataset Name:** data.csv

**Columns:**
- `Duration`: Duration of exercise in minutes.
- `Date`: Date of the workout.
- `Pulse`: Average pulse rate.
- `Maxpulse`: Maximum pulse rate.
- `Calories`: Calories burned during exercise.

## Objectives
- Understand Python data structures and functions.
- Load and explore CSV datasets using Pandas.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Correct inconsistent date formats.
- Filter rows based on specific conditions.
- Create new columns using Pandas and NumPy.
- Visualize data using Matplotlib and Seaborn.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

## Data Cleaning and Wrangling
The following operations were performed:

1. Imported the dataset using Pandas.
2. Explored dataset structure using `head()`, `info()`, and `describe()`.
3. Identified missing values using `isnull()`.
4. Replaced missing calorie values using median imputation.
5. Removed duplicate records using `drop_duplicates()`.
6. Converted the Date column into datetime format.
7. Identified unusual duration and pulse values.
8. Filtered records based on calorie and workout conditions.
9. Created additional columns:
   - Calories_Per_Minute
   - Workout_Intensity

## Data Visualization
The following visualizations were created:

- Workout Duration Distribution (Histogram)
- Calories Burned Distribution (Histogram)
- Pulse vs Calories (Scatter Plot)
- Workout Duration vs Calories (Scatter Plot)
- Calories by Workout Intensity (Box Plot)
- Correlation Heatmap

## Project Structure

```text
Fitness-Data-Wrangling/
│
├── data.csv
├── data_wrangling.py
├── cleaned_fitness.csv
├── fitness_analysis.csv
└── README.md
```

## How to Run the Project

1. Clone or download this repository.
2. Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

3. Keep `data.csv` in the project folder.
4. Run the Python script:

```bash
python data_wrangling.py
```

5. View the cleaned datasets and generated visualizations.

## Conclusion

This project demonstrates the practical application of Python for data cleaning, manipulation, and visualization. It provides an understanding of how raw datasets can be processed into structured and meaningful information for further analysis.

---

**Project Category:** Python & Data Wrangling  
**Week:** 3  
**Domain:** Data Analytics
