#messing around wiht bootstrapping 

#loading in data
import pandas as pd
import numpy as np
import bootstrapped.bootstrap as bs
import bootstrapped.compare_functions as bs_compare
import bootstrapped.stats_functions as bs_stats
import numpy.random as npr
from scipy import stats
from numpy import genfromtxt

"""
###with pandas, run out of space
jt=pd.read_csv('jt_sample.csv')
year=jt['year']
jt.dropna()
ages=jt['age'].astype(str)
new_age=ages.replace("Under 1 year", "1")

nage=[int(x) for x in new_age]
age=np.array(nage)
age_sd=25.57
age_mean=32
mean_res=bs.bootstrap(age, stat_func=bs_stats.mean)
std_res=bs.bootstrap(age, stat_function=bs_stat.std)
"""

jt=open('jt_sample.csv', 'r').readlines()

year=np.array(jt['year'])
year=jt['year'].astype(str)
year=[int(x) for x in new_age]

#year=np.array(jt['year'])


#https://www.bjs.gov/content/pub/ascii/Fssc00.txt
age_sd=25.57
age_mean=32
    
syear=year[:10]
print(bs.bootstrap(syear, stat_func=bs_stats.age_mean))
print(bs.bootstrap(syear, stat_func=bs_stats.age_sd))

mean_res=bs.bootstrap(samples, stat_func=bs_stats.mean)
std_res=bs.bootstrap(samples, stat_function=bs_stat.std)

