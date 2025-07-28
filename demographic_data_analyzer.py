import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    country_income = df[df['salary'] == '>50K']['native-country'].value_counts() / \
                     df['native-country'].value_counts()
    highest_earning_country = country_income.idxmax()
    highest_earning_country_percentage = round(country_income.max() * 100, 1)

    india_occupations = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts()
    top_IN_occupation = india_occupations.idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Rich percentage among min workers:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India for >50K earners:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
