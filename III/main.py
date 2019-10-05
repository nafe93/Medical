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
def draw_hist(data, num_bins, color, type='vertical', stacked=False, density=False, text_x='', text_y='', label=['']):
    plt.hist(data, num_bins, color=color, alpha=0.5, orientation=type, stacked=stacked, density=density,
             label=label)
    plt.legend(loc='upper right')
    plt.xlabel(text_x)
    plt.ylabel(text_y)
    # plt.ylim(0, 1)
    # plt.xlim(0, 1)
    plt.show()


# draw bar
def draw_bar(data, data_name, text_x='', text_y='', color='', text='', error=0):

    yerr_severe = error[0][1] - error[0][0]
    yerr_mild = error[1][1] - error[1][0]
    yerr_moderate = error[2][1] - error[2][0]

    plt.bar(data_name[0], data[0], color=color[0], alpha=0.5,  yerr=yerr_severe, label='severe')
    plt.bar(data_name[1], data[1], color=color[1], alpha=0.5, yerr=yerr_mild, label='mild')
    plt.bar(data_name[2], data[2], color=color[2], alpha=0.5, yerr=yerr_moderate, label='moderate')
    plt.legend(loc='upper right')
    plt.suptitle(text)
    plt.xlabel(text_x)
    plt.ylabel(text_y)

    # x_pos = -0.12
    # y_pos = 20
    # plt.text(x_pos, y_pos, "text on plot")

    plt.show()


# Piecharm graphics
def draw_pie(data_labels, data_sizes):
    explode = tuple([0.1] * len(data_labels))
    plt.pie(data_sizes, explode=explode, labels=data_labels, autopct='%.2f%%', shadow=True, startangle=90)
    # Равное соотношение сторон гарантирует, что пирог нарисован как круг.
    plt.axis('equal')
    plt.show()


# read from pdf
data_xl = pd.read_excel("dataset-1.xlsx")

# severity
data_severe = data_xl[(data_xl['severity'] == "severe")]
data_mild = data_xl[(data_xl['severity'] == "mild")]
data_moderate = data_xl[(data_xl["severity"] == "moderate")]

# draw_pie(data_xl["severity"].value_counts().index, data_xl["severity"].value_counts())
# print(data_xl["severity"].value_counts())


# add new table
disease_age_difference = data_xl['age (years)'] - data_xl['age of disease debute (years)']
data_xl['difference'] = disease_age_difference

# age
data_severe_age = data_severe['age (years)'].median()
data_mild_age = data_mild['age (years)'].median()
data_moderate_age = data_moderate['age (years)'].median()

# age of disease
data_severe_for_disease = data_xl[(data_xl['severity'] == "severe") & (data_xl['difference'] >= 0)]
data_mild_for_disease = data_xl[(data_xl['severity'] == "mild") & (data_xl['difference'] >= 0)]
data_moderate_for_disease = data_xl[(data_xl['severity'] == "moderate") & (data_xl['difference'] >= 0)]

disease_age_severe = data_severe_for_disease['age of disease debute (years)'].median()
disease_age_mild = data_mild_for_disease['age of disease debute (years)'].median()
disease_age_moderate = data_moderate_for_disease['age of disease debute (years)'].median()

# erythrocytes
# hemoglobin
# leukocytes
# neutrophils type 1
# neutrophils type 2
# lymphocytes
# eosinophils
# basophils
# monocytes
# erythrocytes sedimentation rate

#######################################
# just change name and give the result

name = 'erythrocytes sedimentation rate'
data_severe_error = mean_confidence_interval_scipy(data_severe[name])
data_mild_error = mean_confidence_interval_scipy(data_mild[name])
data_moderate_error = mean_confidence_interval_scipy(data_moderate[name])
# data_severe
print(data_severe[name].describe().to_string(header=None, index=None))
print(data_severe_error[0])
print(data_severe_error[1])
print("###########")
print(data_mild[name].describe().to_string(header=None, index=None))
print(data_mild_error[0])
print(data_mild_error[1])
print("###########")
print(data_moderate[name].describe().to_string(header=None, index=None))
print(data_moderate_error[0])
print(data_moderate_error[1])

# draw
num_bins = 10
color = ['red', 'blue', 'green']
names = label = ['severe', 'mild', 'moderate']
text_for_bar_y_name = 'Median'


# draw hist of age
data_age_view = [data_severe[name], data_mild[name], data_moderate[name]]
draw_hist(data_age_view, num_bins, color, text_x=name, text_y='Number', label=label)

# draw bar of age
values = [data_severe[name].median(),  data_mild[name].median(),  data_moderate[name].median()]
values_error = [mean_confidence_interval_scipy(data_severe[name]),
                    mean_confidence_interval_scipy(data_mild[name]),
                    mean_confidence_interval_scipy(data_moderate[name])]

draw_bar(values, names, text_y=text_for_bar_y_name, color=color, text=text_for_bar_y_name + ' of ' + name, error=values_error)




