import pandas as pd
import numpy as np

census = pd.read_csv("adult.data.csv")

#################################################################################################################################################


# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

number_race = census['race']

number_race = list(number_race.groupby(number_race).size())
number_race.sort(reserve=True)

# [27816, 3124, 1039, 311, 271]

#################################################################################################################################################

# What is the average age of men?

avg_men = census[["age","sex"]]
print(avg_men[avg_men["sex"] == 'Male'].groupby("sex").agg({"age": "mean"}))

print(39.43)

# 39.43

#################################################################################################################################################

# What is the percentage of people who have a Bachelor's degree?

bs = census[['education']]
# bs_bachelors = (bs['education']=='Bachelors').sum()
# bs_total = bs['education'].count()

print(((bs['education']=='Bachelors').sum()) / (bs['education'].count()) * 100)

# 16.45

#################################################################################################################################################

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

salary = census[['education','salary']]

# count of bacherlors making >50K
salary_ba = salary[(salary['education'] == 'Bachelors') & (salary['salary']=='>50K')]
ba_count = salary_ba['education'].count()

# count of masters making >50k
salary_ma = salary[(salary['education'] == 'Masters') & (salary['salary']=='>50K')]
ma_count = salary_ma['education'].count()

# count of doctorate making >50k
salary_dr = salary[(salary['education'] == 'Doctorate') & (salary['salary']=='>50K')]
dr_count = salary_dr['education'].count()

# percentage of people with advanced degrees making >50K
print((ba_count + ma_count + dr_count) / (salary['education'].count()) * 100)

# 10.71

#################################################################################################################################################

# What percentage of people without advanced education make more than 50K?

salary_begin = salary[(salary['education'] != 'Bachelors') & (salary['education'] != 'Masters')
                      & (salary['education'] != 'Doctorate') & (salary['salary']==">50K")]

print(salary_begin['education'].count() / salary["education"].count() * 100)

# 13.37

#################################################################################################################################################

# What is the minimum number of hours a person works per week?

census['hours-per-week'].min()

# 1

#################################################################################################################################################

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

min = census[['hours-per-week','salary']]
min_1 = min['hours-per-week']==1
min_1.value_counts() # 20 people work 1 hour-per-week
min_1 = (min['hours-per-week']==1) & (min['salary']== '>50K')
min_1.value_counts() # 2 people work 1 hour-per-week and make >50K

print(2/20*100)

# 10.00

#################################################################################################################################################

# What country has the highest percentage of people that earn >50K and what is that percentage?

country = census[['native-country','salary']]
country_salary = country['salary'] == ">50K"
country[country_salary].value_counts() # United-States has the most people with 7171
country[country_salary].describe() # 7841 total people in countries that make >50K

print(7171/7841*100)

# 91.46

#################################################################################################################################################

# Identify the most popular occupation for those who earn >50K in India

country = census[['native-country','salary','occupation']]
country_india = (country['native-country'] == "India") & (country['salary'] == ">50K")
country[country_india].value_counts()

# most popular profession is "Prof-specialty