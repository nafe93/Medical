import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import scipy as sp
# for big number
from scipy import stats


# mean confidence interval Средний доверительтнй интервыл
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    # sem calculate the standard error of the mean
    # stats.t A Student’s t continuous random variable.
    # ppf Display the probability density function (pdf)
    m, se = np.mean(a), sp.stats.sem(a)
    h = se * sp.stats.t.ppf((1+confidence)/2., n-1)
    return m, m-h, m+h


def mean_confidence_interval_scipy(data, confidence=0.95):
    return stats.t.interval(confidence, len(data) - 1, loc=np.mean(data), scale=stats.sem(data))


# count age
def count_age(data_age, data_sex):
    age_sum = data_age.sum()
    count_sex = data_sex.count()
    return age_sum / count_sex


# draw plot
def draw_plot(male, female):

    ax = plt.gca()
    ax.cla()  # clear things for fresh plot

    # plt.plot([male.min(), male.mean()], [male.mean(), male.mean()], color='green')
    circle1 = plt.Circle((50, 60), 0.5, color='y')


    ax.add_artist(circle1)


    plt.scatter(male.mean(), male.mean(), s=300, color='red')
    plt.scatter(female.mean(), female.mean(), s=300, color='blue')

    plt.scatter(male, male.index.tolist(), s=10, color='red')
    plt.scatter(female, female.index.tolist(), s=10, color='blue')

    plt.title("example")
    plt.grid()

    # plt.savefig("scatter_points_order_01.png", bbox_inches='tight')
    plt.show()
    plt.close()


# draw hist
def draw_hist(data, num_bins, color, type='vertical', stacked=False, density=False, text_x='', text_y=''):
    plt.hist(data, num_bins, color=color, alpha=0.5, orientation=type, stacked=stacked, density=density,
             label=['male', 'female'])
    plt.legend(loc='upper right')
    plt.xlabel(text_x)
    plt.ylabel(text_y)
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    plt.show()


# draw bar
def draw_bar(data, data_name, text_x='', text_y='', color='', text='', error=0):

    yerr_male = error[0][1] - error[0][0]
    yerr_female = error[1][1] - error[1][0]

    plt.bar(data_name[0], data[0], color=color[0], alpha=0.5,  yerr=yerr_male, label='male')
    plt.bar(data_name[1], data[1], color=color[1], alpha=0.5, yerr=yerr_female, label='female')
    plt.legend(loc='upper right')
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
age_male = data_male['age (years)'].median()
age_female = data_female['age (years)'].median()

# age of disease
data_male_for_disease = data_xl[(data_xl['sex'] == "male") & (data_xl['difference'] >= 0)]
data_female_for_disease = data_xl[(data_xl.sex == "female") & (data_xl['difference'] >= 0)]

disease_age_male = data_male_for_disease['age of disease debute (years)'].median()
disease_age_female = data_female_for_disease['age of disease debute (years)'].median()

# erythrocytes
erythrocytes_male = data_male['erythrocytes'].median()
erythrocytes_female = data_female['erythrocytes'].median()

# hemoglobin
hemoglobin_male = data_male['hemoglobin'].median()
hemoglobin_female = data_female['hemoglobin'].median()

# leukocytes
leukocytes_male = data_male['leukocytes'].median()
leukocytes_female = data_female['leukocytes'].median()

# neutrophils type 1
neutrophils_type_one_male = data_male['neutrophils type 1'].median()
neutrophils_type_one_female = data_female['neutrophils type 1'].median()

# neutrophils type 2
neutrophils_type_two_male = data_male['neutrophils type 2'].median()
neutrophils_type_two_female = data_female['neutrophils type 2'].median()

# lymphocytes
lymphocytes_male = data_male['lymphocytes'].median()
lymphocytes_female = data_female['lymphocytes'].median()

# eosinophils
eosinophils_male = data_male['eosinophils'].median()
eosinophils_female = data_female['eosinophils'].median()

# basophils
basophils_male = data_male["basophils"].median()
basophils_female = data_female["basophils"].median()

# monocytes
monocytes_male = data_male["monocytes"].median()
monocytes_female = data_female["monocytes"].median()

# erythrocytes sedimentation rate
erythrocytes_sedimentation_rate_male = data_male["erythrocytes sedimentation rate"].median()
erythrocytes_sedimentation_rate_female = data_female["erythrocytes sedimentation rate"].median()

########################################


# print age
print(data_male['basophils'].describe(), data_female['basophils'].describe())
print("male: ", mean_confidence_interval_scipy(data_male['basophils']))
print("female", mean_confidence_interval_scipy(data_female['basophils']))
print()

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
draw_plot(data_male['age (years)'], data_female['age (years)'])

"""

############################################

# draw
num_bins = 10
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


text_for_bar_y_name = 'Median'

# draw bar of age
values_age = [age_male, age_female]
values_age_error = [mean_confidence_interval_scipy(data_male['age (years)']),
                    mean_confidence_interval_scipy(data_female['age (years)'])]
draw_bar(values_age, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of Age', error=values_age_error)

# draw bar of disease
values_disease = [disease_age_male, disease_age_female]
values_disease_error = [mean_confidence_interval_scipy(data_male_for_disease['age of disease debute (years)']),
                        mean_confidence_interval_scipy(data_female_for_disease['age of disease debute (years)'])]
draw_bar(values_disease, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of disease', error=values_disease_error)

# draw bar of erythrocytes
values_erythrocytes = [erythrocytes_male, erythrocytes_female]
values_erythrocytes_error = [mean_confidence_interval_scipy(data_male['erythrocytes']),
                    mean_confidence_interval_scipy(data_female['erythrocytes'])]
draw_bar(values_erythrocytes, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of erythrocytes', error=values_erythrocytes_error)

# draw bar of hemoglobin
values_hemoglobin = [hemoglobin_male, hemoglobin_female]
values_hemoglobin_error = [mean_confidence_interval_scipy(data_male['hemoglobin']),
                    mean_confidence_interval_scipy(data_female['hemoglobin'])]
draw_bar(values_hemoglobin, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of hemoglobin', error=values_hemoglobin_error)

# draw bar of Leukocytes
values_leukocytes = [leukocytes_male, leukocytes_female]
values_leukocytes_error = [mean_confidence_interval_scipy(data_male['leukocytes']),
                    mean_confidence_interval_scipy(data_female['leukocytes'])]
draw_bar(values_leukocytes, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of Leukocytes', error=values_leukocytes_error)

# draw bar of neutrophils type 1
values_neutrophils = [neutrophils_type_one_male, neutrophils_type_one_female]
values_neutrophils_error = [mean_confidence_interval_scipy(data_male['neutrophils type 1']),
                    mean_confidence_interval_scipy(data_female['neutrophils type 1'])]
draw_bar(values_neutrophils, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of neutrophils type 1', error=values_neutrophils_error)

# draw bar of neutrophils type 2
values_neutrophils_2 = [neutrophils_type_two_male, neutrophils_type_two_female]
values_neutrophils_error_2 = [mean_confidence_interval_scipy(data_male['neutrophils type 2']),
                    mean_confidence_interval_scipy(data_female['neutrophils type 2'])]
draw_bar(values_neutrophils_2, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of neutrophils type 2', error=values_neutrophils_error_2)

# draw bar of lymphocytes
values_lymphocytes = [lymphocytes_male, lymphocytes_female]
values_lymphocytes_error = [mean_confidence_interval_scipy(data_male['lymphocytes']),
                    mean_confidence_interval_scipy(data_female['lymphocytes'])]
draw_bar(values_lymphocytes, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of lymphocytes', error=values_lymphocytes_error)

# draw bar of eosinophils
values_eosinophils = [eosinophils_male, eosinophils_female]
values_eosinophils_error = [mean_confidence_interval_scipy(data_male['eosinophils']),
                    mean_confidence_interval_scipy(data_female['eosinophils'])]
draw_bar(values_eosinophils, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of eosinophils', error=values_eosinophils_error)

# draw bar of basophils
values_basophils = [basophils_male, basophils_female]
values_basophil_error =[mean_confidence_interval_scipy(data_male['basophils']),
                    mean_confidence_interval_scipy(data_female['basophils'])]
draw_bar(values_basophils, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of basophils', error=values_basophil_error)

# draw bar of monocytes
values_monocytes = [monocytes_male, monocytes_female]
values_monocytes_error =[mean_confidence_interval_scipy(data_male['basophils']),
                    mean_confidence_interval_scipy(data_female['basophils'])]
draw_bar(values_monocytes, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of monocytes', error=values_monocytes_error)

# draw bar erythrocytes sedimentation rate
values_erythrocytes_sedimentation_rate = [erythrocytes_sedimentation_rate_male, erythrocytes_sedimentation_rate_female]
values_erythrocytes_sedimentation_rate_error =[mean_confidence_interval_scipy(data_male['erythrocytes sedimentation rate']),
                    mean_confidence_interval_scipy(data_female['erythrocytes sedimentation rate'])]
draw_bar(values_erythrocytes_sedimentation_rate, names, text_y=text_for_bar_y_name, color=color,
         text=text_for_bar_y_name + ' erythrocytes sedimentation rate', error=values_erythrocytes_sedimentation_rate_error)

"""