from __future__ import division
import numpy as np
import scipy
import pandas as pd
from scipy.signal import convolve, gaussian
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')


path = 'C:\\Users\\nate\\Desktop\\andyschoolgrades.csv'
real = True
normalized = True


def smoothe(x,y):
    """

    :param x:
    :param y:
    :return:
    """
    sorter = np.argsort(x)
    x = x[sorter]
    y = y[sorter]
    print(x, y)
    # first, make a function to linearly interpolate the data
    f = scipy.interpolate.interp1d(x, y)
    # resample with 1000 samples
    xx = np.linspace(min(student_percentile), max(student_percentile), 1000)
    # compute the function on this finer interval
    yy = f(xx)
    # make a gaussian window
    window = gaussian(200, 25)
    # convolve the arrays
    smoothed = convolve(yy, window / window.sum(), mode='same')
    return smoothed






valid_answers = ['a','b','c','d','No Answer']
if real == False:
    n_students, n_questions = 200,50
    data = np.vstack([np.random.choice(valid_answers,n_questions,replace=True) for s in range(n_students)])
    answer_key = np.random.choice(valid_answers[0:4],n_questions)
else:
    df = pd.read_csv(path)
    df.replace(np.nan,valid_answers[-1], regex=True,inplace=True)
    df.set_index(['Last Name'],inplace=True)
    answer_key = df.loc['answer key'].values
    df.drop(['answer key'],axis=0,inplace=True)
    print(df)
    data = df.values
    n_students, n_questions = data.shape
    print(n_students)
    print(n_questions)

# assume index 0 in correct answer

# Compute Percentiles of Students
student_scores = []
for s in data:
    score = 0
    for qi,answer in enumerate(s):
        if answer == answer_key[qi]:
            score += 1
    student_scores.append(score)
assert len(student_scores) == n_students


student_ranks = scipy.stats.rankdata(student_scores,method='max')
assert len(student_ranks) == n_students

student_percentile = np.array([scipy.stats.percentileofscore(student_scores,score) for score in student_scores])
print(max(student_percentile),min(student_percentile))



for qi in range(n_questions):
    plt.figure()

    color_set = ['#66ccff','#006699','#0000cc']
    c = 0

    for answer in valid_answers:
        if answer == answer_key[qi]:
            color = 'red'
            alpha = 1
        elif answer == valid_answers[-1]:
            color = 'black'
            alpha = 0.5
        else:
            color = color_set[c]
            alpha = 0.5
            c += 1


        if normalized:
            student_count = []
            for si, p in enumerate(student_percentile):
                if str(data[si, qi]) == answer:
                    student_count.append(p)

            if len(student_count) > 1:
                sns.distplot(np.array(student_count),rug=True,hist=False,norm_hist=False,bins=10,color=color,
                             label=answer,kde_kws={'kernel':'biw',
                                                   'bw':'scott','alpha':alpha,
                                                   })
        else:
            x = student_percentile
            y = np.array([1 if str(student_answer) == answer else 0 for student_answer in data[:, qi]])
            smoothed = smoothe(x, y)
            plt.plot(smoothed, label=answer, c=color,alpha=alpha)

    if normalized:
        sns.distplot(np.array(student_percentile), rug=True, hist=False,color='grey',norm_hist=False,
                     label='Any Answer', kde_kws={'kernel': 'biw',
                                                  'bw': 'scott',
                                                  'shade':True,
                                                  'alpha':0.1,

                                            })
    else:
        x = student_percentile
        y = np.ones(len(student_percentile))
        smoothed = smoothe(x, y)
        plt.plot(smoothed, label=answer, c='grey')


    plt.title('Question %d\nCorrect Answer: %s'%(qi+1,answer_key[qi]))
    plt.xlim((0,100))
    sns.despine()
    plt.xlabel('Percentile')
    plt.ylabel('Probablity of Student falling into a percentile\n GIVEN they answered the way they did')
    plt.legend()
    plt.show()









