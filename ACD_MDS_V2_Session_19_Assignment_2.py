# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 05:09:22 2018

@author: Eliud Lelerai
"""

import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# performing a oneway analysis of variance using α=.05
  #Null Hypothesis(Ho): means of group1,2,and 3 are equal
  #Alternative Hypothesis(Ha): means of group1,2,and 3 are NOT equal
  
# Data organization

    #*******The Raw Data*****
     #[Group1: 51, 45, 33, 45, 67]
     #[Group2: 23, 43, 23, 43, 45]
     #[Group3: 56, 76, 74, 87, 56]

    #Creating data frame
df= pd.DataFrame({'group1':[51,45,33,45,67], 'group2' :[23,43,23,43,45],'group3' : [56,76,74,87,56]})

#  ONE WAY ANOVA TEST


stats.f_oneway(df['group1'],df['group2'],df['group3'])

# Analysis of variance test output:
    # f-value value=9.74
    # p-value=0.003
    

# Conclusion
   # p-value is approximately 0.03  which is below 0.05 significant level
   #  There is a significant difference between the groups means