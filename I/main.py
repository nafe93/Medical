import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates


# count age
def count_age(data_age, data_sex):
    age_sum = data_age.sum()
    count_sex = data_sex.count()
    return age_sum / count_sex


# draw hist
def draw_hist(data, num_bins, color, type='vertical', stacked=False, density=False, text_x='', text_y=''):
    plt.hist(data, num_bins, color=color, alpha=0.5, orientation=type, stacked=stacked, density=density)
    plt.xlabel(text_x)
    plt.ylabel(text_y)
    plt.show()


# draw bar
def draw_bar(data, data_name, text_x='', text_y=''):
    plt.bar(data_name, data, color=color, alpha=0.5)
    plt.suptitle('Average of Age')
    plt.xlabel(text_x)
    plt.ylabel(text_y)

    # x_pos = -0.12
    # y_pos = 20
    # plt.text(x_pos, y_pos, "text on plot")

    plt.show()


# read from pdf
data_xl = pd.read_excel("dataset-1.xlsx")

# sex
data_male = data_xl[(data_xl.sex == "male")]
data_female = data_xl[(data_xl.sex == "female")]

# age
age_male = count_age(data_male['age (years)'], data_male['sex'])
age_female = count_age(data_female['age (years)'], data_female['sex'])

# age of disease
disease_age_male = count_age(data_male['age of disease debute (years)'], data_male['sex'])
disease_age_female = count_age(data_female['age of disease debute (years)'], data_female['sex'])

# erythrocytes
erythrocytes_male = count_age(data_male['erythrocytes'], data_male['sex'])
erythrocytes_female = count_age(data_female['erythrocytes'], data_female['sex'])

# test
print(erythrocytes_male)
print(data_xl['erythrocytes'].value_counts())

# print age
print(f"Age of female is {round(age_female, 3)} and age of male is {round(age_male, 3)}")

# draw
num_bins = 5
color = ['red', 'blue']
names = ['male', 'femala']

# draw hist of age
data_age_view = [data_male['age (years)'], data_female['age (years)']]
draw_hist(data_age_view, num_bins, color, text_x='Age', text_y='Number')

# draw hist of disease
data_disease_view = [data_male['age of disease debute (years)'], data_female['age of disease debute (years)']]
draw_hist(data_disease_view, num_bins, color, text_x='Age', text_y='Number')

# draw erythrocytes
data_erythrocytes_view = [data_male['erythrocytes'], data_female['erythrocytes']]
draw_hist(data_erythrocytes_view, num_bins, color, text_x='erythrocytes', text_y='Number')

# draw bar of age
values_age = [age_male, age_female]
draw_bar(values_age, names, text_y='Average')

# draw bar of disease
values_disease = [disease_age_male, disease_age_female]
draw_bar(values_disease, names, text_y='Average')

# draw bar of erythrocytes
values_erythrocytes = [erythrocytes_male, erythrocytes_female]
draw_bar(values_erythrocytes, names, text_y='Average')




