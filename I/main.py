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
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    plt.show()


# draw bar
def draw_bar(data, data_name, text_x='', text_y='', color='', text=''):
    plt.bar(data_name, data, color=color, alpha=0.5)
    plt.suptitle(text)
    plt.xlabel(text_x)
    plt.ylabel(text_y)

    # x_pos = -0.12
    # y_pos = 20
    # plt.text(x_pos, y_pos, "text on plot")

    plt.show()


# read from pdf
data_xl = pd.read_excel("dataset-1.xlsx")

# add new table
disease_age_difference = data_xl['age (years)'] - data_xl['age of disease debute (years)']
data_xl['difference'] = disease_age_difference

# sex
data_male = data_xl[(data_xl.sex == "male")]
data_female = data_xl[(data_xl.sex == "female")]

# age
age_male = count_age(data_male['age (years)'], data_male['sex'])
age_female = count_age(data_female['age (years)'], data_female['sex'])

# age of disease
data_male_for_disease = data_xl[(data_xl['sex'] == "male") & (data_xl['difference'] >= 0)]
data_female_for_disease = data_xl[(data_xl.sex == "female") & (data_xl['difference'] >= 0)]

disease_age_male = count_age(data_male_for_disease['age of disease debute (years)'], data_male_for_disease['sex'])
disease_age_female = count_age(data_female_for_disease['age of disease debute (years)'], data_female_for_disease['sex'])

# erythrocytes
erythrocytes_male = count_age(data_male['erythrocytes'], data_male['sex'])
erythrocytes_female = count_age(data_female['erythrocytes'], data_female['sex'])

# hemoglobin
hemoglobin_male = data_male['hemoglobin'].mean()
hemoglobin_female = data_female['hemoglobin'].mean()

# leukocytes
leukocytes_male = data_male['leukocytes'].mean()
leukocytes_female = data_female['leukocytes'].mean()

# neutrophils type 1
neutrophils_type_one_male = data_male['neutrophils type 1'].mean()
neutrophils_type_one_female = data_female['neutrophils type 1'].mean()

# neutrophils type 2
neutrophils_type_two_male = data_male['neutrophils type 2'].mean()
neutrophils_type_two_female = data_female['neutrophils type 2'].mean()

# lymphocytes
lymphocytes_male = data_male['lymphocytes'].mean()
lymphocytes_female = data_female['lymphocytes'].mean()

# eosinophils
eosinophils_male = data_male['eosinophils'].mean()
eosinophils_female = data_female['eosinophils'].mean()

# basophils
basophils_male = data_male["basophils"].mean()
basophils_female = data_female["basophils"].mean()

# monocytes
monocytes_male = data_male["monocytes"].mean()
monocytes_female = data_female["monocytes"].mean()

# erythrocytes sedimentation rate
erythrocytes_sedimentation_rate_male = data_male["erythrocytes sedimentation rate"].mean()
erythrocytes_sedimentation_rate_female = data_female["erythrocytes sedimentation rate"].mean()

########################################

# print age
print(f"Age of female is {round(age_female, 3)} and age of male is {round(age_male, 3)}")
print(f"Disease age of female is {round(disease_age_female, 3)} and Disease  age of male is {round(disease_age_male, 3)}")
print(f"Erythrocytes of female is {round(erythrocytes_female, 3)} and Erythrocytes of male is {round(erythrocytes_male, 3)}")
print(f"Hemoglobin of female is {round(hemoglobin_female, 3)} and Hemoglobin of male is {round(hemoglobin_male, 3)}")
print(f"Leukocytes of female is {round(leukocytes_female, 3)} and Leukocytes of male is {round(leukocytes_male, 3)}")
print(f"Neutrophils type 1 of female is {round(neutrophils_type_one_female, 3)} and Neutrophils type 1 of male is {round(neutrophils_type_one_male, 3)}")
print(f"Neutrophils type 2 of female is {round(neutrophils_type_two_female, 3)} and Neutrophils type 2 of male is {round(neutrophils_type_two_male, 3)}")
print(f"lymphocytes of female is {round(lymphocytes_female, 3)} and lymphocytes of male is {round(lymphocytes_male, 3)}")
print(f"eosinophils of female is {round(eosinophils_female, 3)} and eosinophils of male is {round(eosinophils_male, 3)}")
print(f"basophils of female is {round(basophils_female, 3)} and basophils of male is {round(basophils_male, 3)}")
print(f"monocytes of female is {round(monocytes_female, 3)} and monocytes of male is {round(monocytes_male, 3)}")
print(f"erythrocytes sedimentation rate of female is {round(erythrocytes_sedimentation_rate_female, 3)} and erythrocytes sedimentation rate of male is {round(erythrocytes_sedimentation_rate_male, 3)}")


############################################

# draw
num_bins = 5
color = ['red', 'blue']
names = ['male', 'female']

# draw hist of age
data_age_view = [data_male['age (years)'], data_female['age (years)']]
draw_hist(data_age_view, num_bins, color, text_x='Age', text_y='Number')

# draw hist of disease
data_disease_view = [data_male_for_disease['age of disease debute (years)'],
                     data_female_for_disease['age of disease debute (years)']]
draw_hist(data_disease_view, num_bins, color, text_x='age of disease debute (years)', text_y='Number')

# draw erythrocytes
data_erythrocytes_view = [data_male['erythrocytes'], data_female['erythrocytes']]
draw_hist(data_erythrocytes_view, num_bins, color, text_x='erythrocytes', text_y='Number')

# draw hemoglobin
data_hemoglobin_view = [data_male['hemoglobin'], [data_female['hemoglobin']]]
draw_hist(data_hemoglobin_view, num_bins, color, text_x='Hemoglobin', text_y='Number')

# draw Leukocytes
data_leukocytes_view = [data_male['leukocytes'], [data_female['leukocytes']]]
draw_hist(data_leukocytes_view, num_bins, color, text_x='Leukocytes', text_y='Number')

# draw neutrophils type 1
data_neutrophils_one_view = [data_male['neutrophils type 1'], [data_female['neutrophils type 1']]]
draw_hist(data_neutrophils_one_view, num_bins, color, text_x='neutrophils type 1', text_y='Number')

# draw neutrophils type 2
data_neutrophils_two_view = [data_male['neutrophils type 2'], [data_female['neutrophils type 2']]]
draw_hist(data_neutrophils_two_view, num_bins, color, text_x='neutrophils type 2', text_y='Number')

# draw lymphocytes
data_lymphocytes_view = [data_male['lymphocytes'], [data_female['lymphocytes']]]
draw_hist(data_lymphocytes_view, num_bins, color, text_x='lymphocytes', text_y='Number')

# draw eosinophils
data_eosinophils_view = [data_male['eosinophils'], [data_female['eosinophils']]]
draw_hist(data_eosinophils_view, num_bins, color, text_x='eosinophils', text_y='Number')

# draw basophils
data_basophils_view = [data_male['basophils'], [data_female['basophils']]]
draw_hist(data_basophils_view, num_bins, color, text_x='basophils', text_y='Number')

# draw monocytes
data_monocytes_view = [data_male['monocytes'], [data_female['monocytes']]]
draw_hist(data_monocytes_view, num_bins, color, text_x='monocytes', text_y='Number')

# draw erythrocytes_sedimentation_rate
data_erythrocytes_sedimentation_rate_view = [data_male["erythrocytes sedimentation rate"], data_female["erythrocytes sedimentation rate"]]
draw_hist(data_erythrocytes_sedimentation_rate_view, num_bins, color, text_x='erythrocytes sedimentation rate', text_y='Number')
########################################################################################################################

# draw bar of age
values_age = [age_male, age_female]
draw_bar(values_age, names, text_y='Average', color=color, text='Average of Age')

# draw bar of disease
values_disease = [disease_age_male, disease_age_female]
draw_bar(values_disease, names, text_y='Average', color=color, text='Average of disease')

# draw bar of erythrocytes
values_erythrocytes = [erythrocytes_male, erythrocytes_female]
draw_bar(values_erythrocytes, names, text_y='Average', color=color, text='Average of erythrocytes')

# draw bar of hemoglobin
values_hemoglobin = [hemoglobin_male, hemoglobin_female]
draw_bar(values_hemoglobin, names, text_y='Average', color=color, text='Average of hemoglobin')

# draw bar of Leukocytes
values_leukocytes = [leukocytes_male, leukocytes_female]
draw_bar(values_leukocytes, names, text_y='Average', color=color, text='Average of Leukocytes')

# draw bar of neutrophils type 1
values_neutrophils = [neutrophils_type_one_male, neutrophils_type_one_female]
draw_bar(values_neutrophils, names, text_y='Average', color=color, text='Average of neutrophils type 1')

# draw bar of neutrophils type 2
values_neutrophils_2 = [neutrophils_type_two_male, neutrophils_type_two_female]
draw_bar(values_neutrophils_2, names, text_y='Average', color=color, text='Average of neutrophils type 2')

# draw bar of lymphocytes
values_lymphocytes = [lymphocytes_male, lymphocytes_female]
draw_bar(values_lymphocytes, names, text_y='Average', color=color, text='Average of lymphocytes')

# draw bar of eosinophils
values_eosinophils = [eosinophils_male, eosinophils_female]
draw_bar(values_eosinophils, names, text_y='Average', color=color, text='Average of eosinophils')

# draw bar of basophils
values_basophils = [basophils_male, basophils_female]
draw_bar(values_basophils, names, text_y='Average', color=color, text='Average of basophils')

# draw bar of monocytes
values_basophils = [basophils_male, basophils_female]
draw_bar(values_basophils, names, text_y='Average', color=color, text='Average of lymphocytes')

# draw bar erythrocytes sedimentation rate
values_erythrocytes_sedimentation_rate = [erythrocytes_sedimentation_rate_male, erythrocytes_sedimentation_rate_female]
draw_bar(values_erythrocytes_sedimentation_rate, names, text_y='Average', color=color, text='Average erythrocytes sedimentation rate')