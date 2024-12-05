#!/usr/bin/env python
# coding: utf-8

# In[183]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[182]:


df=pd.read_csv(r"C:\Users\greenz0ne\Downloads\exams.csv")
df


# In[184]:


df=df.rename(columns={"gender":"Gender",
                  "race/ethnicity":"Race/Ethnicity",
                  "lunch":"Lunch",
                  "math score":"Math score",
                  "reading score":"Reading score",
                  "writing score":"Writing score",
                  "test preparation course":"Test preparation course",
                  "parental level of education":"Parental level of education"})


# In[185]:


df["Test preparation course"].replace({"none":"not completed"},inplace=True)


# In[186]:


df.shape


# In[187]:


df.isnull().sum()


# In[188]:


df.duplicated().sum()


# In[189]:


df.info()


# In[190]:


df.dtypes


# In[191]:


df.nunique()


# In[192]:


df.describe()


# In[193]:


for feature in df.columns:
    if df[feature].dtype=="object":
        print(feature)
    


# In[194]:


numerical_column= [numeric for numeric in df.columns if df[numeric].dtype=="int64"]
categorical_column= [category for category in df.columns if df[category].dtype=="object"]


# In[195]:


categorical_column


# In[196]:


numerical_column


# In[197]:


df["Gender"].value_counts()


# In[198]:


df['Race/Ethnicity'].value_counts()


# In[199]:


df["Total_score"]=(df["Math score"]+df["Reading score"]+df["Writing score"])


# In[200]:


df["percentage"]=(df["Total_score"]/3)


# In[201]:


print(df['Total_score'].max())
print(df["percentage"].max())


# In[202]:


print(df['Total_score'].min())
print(df["percentage"].min())


# In[219]:


import seaborn as sns
figsize=(10,15)
sns.histplot(data=df,x="percentage",kde=True,color="green",bins=30)
plt.show()


# In[246]:


import seaborn as sns
plt.figure(figsize=(15, 7))
sns.histplot(data=df,x="percentage",kde=True,bins=60,hue="Gender")
plt.show()


# Female student tend to perform well than male students ^

# In[ ]:





# In[214]:


plt.subplots(1,3,figsize=(25,6))
plt.subplot(141,title="percentage")
sns.histplot(data=df,x='percentage',kde=True,hue='Lunch')
plt.subplot(142,title="Female")
sns.histplot(data=df[df.Gender=='female'],x='percentage',kde=True,hue='Lunch')
plt.subplot(143,title="Male")
sns.histplot(data=df[df.Gender=='male'],x='percentage',kde=True,hue='Lunch')


# Standard Lunch help students perform well in exams
# Standard lunch helps perform well in exams be it a male of female

# In[ ]:





# In[217]:


plt.subplots(1,3,figsize=(25,6))
plt.subplot(141)
sns.histplot(data=df,x='percentage',kde=True,hue='Parental level of education')
plt.subplot(142,title="Female")
sns.histplot(data=df[df.Gender=='female'],x='percentage',kde=True,hue='Parental level of education')
plt.subplot(143,title="Male")
sns.histplot(data=df[df.Gender=='male'],x='percentage',kde=True,hue='Parental level of education')


# In general parent's education don't help student perform well in exam.
# 3rd plot shows that parent's whose education is of associate's degree or master's degree their male child tend to perform well in exam
# 2nd plot we can see there is no effect of parent's education on female students

# In[243]:


plt.subplots(1,3,figsize=(25,6))
plt.subplot(141,title="Percentage")
sns.histplot(data=df,x='percentage',kde=True,hue='Race/Ethnicity')
plt.subplot(142,title="Female")
sns.histplot(data=df[df.Gender=='female'],x='percentage',kde=True,hue='Race/Ethnicity')
plt.subplot(143,title="Male")
sns.histplot(data=df[df.Gender=='male'],x='percentage',kde=True,hue='Race/Ethnicity')
plt.show()


# Students of group A and group B tends to perform poorly in exam.
# Students of group A and group B tends to perform poorly in exam irrespective of whether they are male or female

# In[ ]:





# In[ ]:





# In[ ]:




