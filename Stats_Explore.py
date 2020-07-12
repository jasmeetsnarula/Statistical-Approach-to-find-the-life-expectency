#!/usr/bin/env python
# coding: utf-8

# In[157]:


import pandas as pd
import numpy as np
import math as mt
import datetime
import calendar
import time
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from matplotlib import cm
from matplotlib import animation
import warnings
warnings.filterwarnings('ignore')
print(sns.axes_style)


# In[158]:


df = pd.read_csv("Life Expectancy Data.csv")


# In[159]:


df.head()


# In[160]:


df.rename(columns={" BMI ":"BMI","Life expectancy ":"Life_Expectancy","Adult Mortality":"Adult_Mortality",
                   "infant deaths":"Infant_Deaths","percentage expenditure":"Percentage_Exp","Hepatitis B":"HepatitisB",
                  "Measles ":"Measles"," BMI ":"BMI","under-five deaths ":"Under_Five_Deaths","Diphtheria ":"Diphtheria",
                  " HIV/AIDS":"HIV_AIDS"," thinness  1-19 years":"thinness_1to19_years"," thinness 5-9 years":"thinness_5to9_years","Income composition of resources":"Income_Comp_Of_Resources",
                   "Total expenditure":"Tot_Exp"},inplace=True)


# In[161]:


df.isnull().sum()


# In[162]:


df.describe()


# In[172]:


new = df[['Life_Expectancy','Alcohol','BMI','Polio']].copy()


# In[173]:


plt.figure(figsize=(15,14))
sns.heatmap(df.corr(),cmap='RdYlBu',annot=True)
plt.show()


# In[174]:


new = new.dropna()
new


# In[176]:


sns.heatmap(new.corr(),annot=True,cmap='RdYlBu')


# In[177]:


l = new.columns.values
noOfRows = 5
noOfCols = 3

plt.figure(figsize=(25,20))
for i in range(0,len(l)):
    plt.subplot(noOfCols+1,noOfRows+1,i+2)
    sns.distplot(new[l[i]].astype(int))


# In[178]:


new.describe()


# In[ ]:




