import pandas as pd

def calculate_demographic_data(print_data=True):
    # read the CSV file into a DataFrame
    df = pd.read_csv("adult.data.csv")

    # count how many people belong to each race
    race_count = df['race'].value_counts()

    # filter for males, then get their average age
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # figure out how many people got a bachelor's degree
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # split data into higher ed (bachelors, masters, doctorate) vs lower
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_ed_df = df[df['education'].isin(advanced_education)]
    lower_ed_df = df[~df['education'].isin(advanced_education)]

    # from higher ed group, see who earns >50K
    higher_education_rich_count = len(higher_ed_df[higher_ed_df['salary'] == '>50K'])
    higher_education_rich = round((higher_education_rich_count / len(higher_ed_df)) * 100, 1)

    # same thing but for lower ed
    lower_education_rich_count = len(lower_ed_df[lower_ed_df['salary'] == '>50K'])
    lower_education_rich = round((lower_education_rich_count / len(lower_ed_df)) * 100, 1)

    # get the fewest hours anyone works
    min_work_hours = df['hours-per-week'].min()

    # out of those who work the least, check how many make >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((len(rich_min_workers) / len(min_workers)) * 100, 1)

    # check which country has the highest percent of high earners
    country_group = df.groupby('native-country')
    country_percentages = (country_group['salary']
                           .apply(lambda x: (x == '>50K').sum() / len(x) * 100))
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # in India, find the most common job for high earners
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high_earners['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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
