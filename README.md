# Demographic Data Analyzer

This project is part of the freeCodeCamp Data Analysis with Python certification. It analyzes a real-world dataset containing demographic information from the 1994 US Census database using the Python pandas library.

## Project Description

The goal of this project is to write a function named calculate_demographic_data that reads the dataset and returns a dictionary of various demographic statistics. These include counts, averages, percentages, and other relevant insights about income, education, work hours, and country-level statistics.

## Dataset

The data is taken from the UCI Machine Learning Repository and contains the following fields: age, workclass, education, marital status, occupation, relationship, race, sex, capital gain, capital loss, hours-per-week, native-country, and salary.

The dataset file is named adult.data.csv and must be placed in the same folder as the Python scripts.

## Files Included

- demographic_data_analyzer.py: The main script where the analysis function is written
- main.py: Used to manually run and test the function
- test_module.py: Contains unit tests to verify the correctness of the solution
- adult.data.csv: The dataset used for the analysis

## Instructions to Run

1. Make sure all files are in the same directory
2. Install pandas if not already installed using pip install pandas
3. Run the script by typing the following in your terminal:

   python3 main.py

4. To run tests and verify the results:

   python3 -m unittest test_module.py

## Output

The function calculates and returns the following values:

- Count of each race
- Average age of men
- Percentage of people with a Bachelors degree
- Percentage of people with higher education who earn more than 50K
- Percentage of people without higher education who earn more than 50K
- Minimum number of work hours per week
- Percentage of people earning more than 50K who work the minimum number of hours
- Country with the highest percentage of people earning more than 50K
- The most common occupation for those who earn more than 50K in India

## Purpose

This project demonstrates data wrangling, filtering, and statistical analysis skills using Python and pandas. It is meant for educational purposes as part of a certification program.
