#messing around wiht bootstrapping 

#loading in data
print "hello world"
import pandas as pd
import numpy as np
import bootstrapped.bootstrap as bs
import bootstrapped.compare_functions as bs_compare
import bootstrapped.stats_functions as bs_stats
import numpy.random as npr
import collections
import matplotlib as plt
import scipy
from numpy import genfromtxt

#data=pd.io.stata.read_stata('jt_all.dta')
data=pd.read_table('jt_all.dta')
jt=data.to_csv('jt_all.dta')

#https://www.bjs.gov/content/pub/ascii/Fssc00.txt
print(jt.head(5))
#print(jt['year'].head(5))
#jts=jt.sample(100)
year=np.matrix(jt['year'])
jt.dropna()
#if year.all>2004:
    #assuming normal, check with pop, sd seems large
age_sd=25.57
age_mean=32

syear=year[:10]
print(bs.bootstrap(syear, stat_func=bs_stats.age_mean))
print(bs.bootstrap(syear, stat_func=bs_stats.age_sd))


#np.std([samples], axis=1)
mean_res=bs.bootstrap(samples, stat_func=bs_stats.mean)
std_res=bs.bootstrap(samples, stat_function=bs_stat.std)
#print('Bootstrapped mean should be: {}'.format(mean))
#print('\t' + str(mean_results))
#print('')
#print('Bootstrapped stdev should be: {}'.format(stdev))
#print('\t' + str(stdev_results))
