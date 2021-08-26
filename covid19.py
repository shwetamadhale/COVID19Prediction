#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


covid = pd.read_csv('covid.csv')
#read the dataframe store in object


# In[5]:


covid.head()
#look at records


# In[6]:


covid.shape
#look at shape, no of columns and records


# In[7]:


covid.columns


# In[8]:


covid["location"].value_counts()


# In[14]:





# In[12]:


covid.isna().any()


# In[15]:


covid.isna().sum()


# In[16]:


india_case = covid[covid["location"] == "India"] #cases in india


# In[17]:


india_case.head()


# In[18]:


india_case.tail()


# In[19]:


import seaborn as sns
from matplotlib import pyplot as plt


# In[21]:


#line plot for total cases per day
sns.set(rc = {'figure.figsize': (15,10)})
sns.lineplot(x = "date", y = "total_cases", data = india_case)
plt.show()


# In[23]:


#df for last 5 days
india_last_5_days = india_case.tail()


# In[24]:


#line plot for total cases  for last 5 days
sns.set(rc = {'figure.figsize': (15,10)})
sns.lineplot(x = "date", y = "total_cases", data = india_last_5_days)
plt.show()


# In[28]:


#line plot for total tests per day
sns.set(rc = {'figure.figsize': (15,10)})
sns.lineplot(x = "date", y = "total_tests", data = india_case)
plt.show()


# In[29]:


#line plot for total tests per day for last 5 days
sns.set(rc = {'figure.figsize': (15,10)})
sns.lineplot(x = "date", y = "total_tests", data = india_last_5_days)
plt.show()


# In[31]:


#understanding cases of India, US, and Japan
india_us_japan = covid[(covid["location"] == "India")|(covid["location"] == "United States")|(covid["location"] == "Japan")]


# In[32]:


#line plot for cases across India, US and Japan
sns.set(rc = {'figure.figsize': (15,10)})
sns.lineplot(x = "location", y = "total_cases", data = india_us_japan, hue = "date")
plt.show()


# In[34]:


#latest data
last_day_cases = covid[covid["date"] == "2021-08-23"]
last_day_cases


# In[35]:


#sorting data accd to total cases
max_cases_country = last_day_cases.sort_values(by = "total_cases" ,ascending = False)


# In[36]:


#top 5 countries with max cases
max_cases_country[1:6]


# In[37]:


#plot a bar-plot for countries with max cases
sns.barplot(x = 'location', y = 'total_cases', data = max_cases_country[1:6], hue = "location")


# In[38]:


india_case.head()


# In[39]:


#linear regression
from sklearn.model_selection import train_test_split


# In[40]:


#convert string date to date-time
import datetime as dt
india_case['date'] = pd.to_datetime(india_case['date'])
india_case.head()


# In[41]:


# convert date-time to ordinal
india_case['date'] = india_case['date'].map(dt.datetime.toordinal)
india_case.head()


# In[42]:


#dependent and independent variable
x = india_case['date']#inde
y = india_case['total_cases']#depe


# In[43]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)#split data for training and testing


# In[44]:


from sklearn.linear_model import LinearRegression


# In[45]:


lr = LinearRegression()#creating instance


# In[46]:


#convert to 1D and fit 
import numpy as np
lr.fit(np.array(x_train).reshape(-1,1), np.array(y_train).reshape(-1,1))


# In[47]:


india_case.tail()


# In[48]:


y_pred = lr.predict(np.array(x_test).reshape(-1,1))


# In[49]:


from sklearn.metrics import mean_squared_error


# In[50]:


mean_squared_error(x_test , y_pred)


# In[52]:


lr.predict(np.array([[738026]]))


# In[53]:


lr.predict(np.array([[738030]]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




