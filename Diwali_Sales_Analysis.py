#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


# import csv file
df = pd.read_csv(r'C:\Users\User\Desktop\Python Project\Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


#drop unreated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[8]:


df.info()


# In[9]:


pd.isnull(df)


# In[10]:


#check for nul values
pd.isnull(df).sum()


# In[11]:


df.shape


# In[12]:


# drop null values
df.dropna(inplace=True)


# In[13]:


df.shape


# In[14]:


# initialize list of lists
data_test = [['madhav', 11], ['Gopi',15], ['Keshav', ],['Lalita', 16]]

# Create the pandas Dataframe using list
df_test = pd.DataFrame(data_test, columns=['Name', 'Age'])

df_test


# In[15]:


df_test.dropna()


# In[16]:


df_test


# In[17]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[18]:


df['Amount'].dtypes


# In[19]:


df.columns


# In[20]:


#rename column
df.rename(columns = {'Marital_Status':'Shaadi'})


# In[22]:


# describe() method returns description of the data in the dataframe (i.e. count , mean, std, etc)
df.describe()


# In[23]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[24]:


df.columns


# In[25]:


ax = sns.countplot(x = 'Gender', data = df)


# In[26]:


ax = sns.countplot(x = 'Gender', data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater then man

# # Age

# In[31]:


df.columns


# In[32]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')


# In[33]:


ax = sns.countplot(data = df, x = 'Age Group')


# In[34]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[35]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[38]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(18,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[39]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[40]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[42]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[43]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[44]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[46]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[47]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




