#!/usr/bin/env python
# coding: utf-8

# # 1. Import Data

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import plotly.express as px


# In[2]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)
data = pd.read_csv("/Users/kathrynkopczenski/Documents/Personal DS Projects/ds_salaries.csv")
df = pd.DataFrame(data)


# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


df.duplicated().sum()


# In[6]:


df.drop_duplicates(inplace = True)


# In[7]:


df.isna().sum()


# In[8]:


remote_ratio = df["remote_ratio"]
salary = df["salary_in_usd"]

sns.barplot(x=remote_ratio, y=salary, data=df, color='purple')
plt.xlabel('Remote Ratio')
plt.ylabel('Salary')
plt.title('Relationship of People Who Work Remote and Salary')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[9]:


#Find the top five data science job titles
entry_counts = df['job_title'].value_counts()
most_common_jobs = entry_counts.head(5)  
print("\nMost Common Jobs:")
print(most_common_jobs)


# In[10]:


#Find the most common data science salaries
entry_counts = df['salary_in_usd'].value_counts()
most_common_sal = entry_counts.head(5)  
print("\nMost Common Salary:")
print(most_common_sal)


# In[11]:


#Find the mean salary for the top five data science job titles
mean_salary_by_job = df.groupby('job_title')['salary_in_usd'].mean()
top_five_jobs = mean_salary_by_job.nlargest(5)
top_five_jobs


# In[25]:


#Bar graph showing the mean salary trends for the top five data science job titles
plt.figure(figsize=(10, 6))
top_five_jobs.plot(kind='bar', color='skyblue')
plt.title('Top Five Job Titles by Mean Salary')
plt.xlabel('Job Title')
plt.ylabel('Mean Salary ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[19]:


fig=px.pie(df.groupby('experience_level',as_index=False)['salary_in_usd'].count().sort_values(by='salary_in_usd',ascending=False).head(10),names='experience_level',values='salary_in_usd',color='experience_level',hole=0.7,labels={'experience_level':'Experience level ','salary_in_usd':'count'},template='ggplot2',title='<b>Total Jobs Based on Experience Level')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))


# In[20]:


fig=px.pie(df.groupby('remote_ratio',as_index=False)['salary_in_usd'].count().sort_values(by='salary_in_usd',ascending=False).head(10),names='remote_ratio',values='salary_in_usd',color='remote_ratio',hole=0.7,labels={'remote_ratio':'remote ratio','salary_in_usd':'count'},template='plotly',title='<b> Remote Ratio')
fig.update_layout(title_x=0.5)


# In[22]:


px.histogram(df,x='salary_in_usd',template='seaborn',labels={'salary_in_usd':'Salary in USD'},title='<b> Salary Distribution')

