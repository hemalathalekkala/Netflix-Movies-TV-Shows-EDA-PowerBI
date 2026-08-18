#!/usr/bin/env python
# coding: utf-8

# # Load Netflix Movies and Tv Shows Dataset

# In[2]:


import pandas as pd
df = pd.read_csv("Netflix_movies_tv.csv")
df


# # Identify the Columns

# In[3]:


df.columns


# # Cleaning Process

# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.shape


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[9]:


dataset=df.fillna(0)
dataset


# In[10]:


dataset.isnull().sum()


# # Droping Unnessary Columns

# In[11]:


dataset=dataset.drop('show_id',axis=1)
dataset


# In[12]:


dataset=dataset.drop('cast',axis=1)
dataset


# In[13]:


dataset=dataset.drop('description',axis=1)
dataset


# In[14]:


dataset=dataset.drop_duplicates()
dataset


# In[15]:


dataset.duplicated().sum()


# In[16]:


dataset['director'] = dataset['director'].replace(0, 'Unknown')
dataset['country'] = dataset['country'].replace(0, 'Unknown')
dataset


# In[17]:


dataset['date_added'].head()


# In[18]:


dataset['date_added'] = pd.to_datetime(
    dataset['date_added'],
    errors='coerce'
)


# In[19]:


dataset['date_added'].head()


# In[20]:


dataset['year_added']=dataset['date_added'].dt.year.astype('Int64')
dataset['year_added'].head()


# In[21]:


dataset['month_added']=dataset['date_added'].dt.month_name()
dataset['month_added'].head()


# In[22]:


dataset[['date_added', 'year_added', 'month_added']].isnull().sum()


# In[23]:


dataset=dataset.dropna(subset=['date_added'])
dataset=dataset.dropna(subset=['year_added'])
dataset=dataset.dropna(subset=['month_added'])


# In[24]:


dataset.isnull().sum()


# In[25]:


dataset.shape


# In[26]:


dataset.duplicated().sum()


# In[27]:


dataset['type'].value_counts()


# In[28]:


dataset['year_added'].value_counts().sort_index()


# In[29]:


dataset['year_added'].value_counts().head(10)


# In[30]:


import matplotlib.pyplot as plt

dataset['year_added'].value_counts().sort_index().plot(kind='bar', figsize=(12,5))

plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.title('Netflix Content Added by Year')
plt.show()


# In[31]:


dataset['country'].value_counts().head(10)


# In[32]:


import matplotlib.pyplot as plt

dataset['country'].value_counts().head(10).plot(
    kind='bar',
    figsize=(10,5)
)

plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.title('Top 10 Countries by Netflix Content')
plt.xticks(rotation=45)
plt.show()


# In[33]:


dataset['listed_in'].value_counts().head(10)


# In[34]:


import matplotlib.pyplot as plt

dataset['listed_in'].value_counts().head(10).plot(
    kind='bar',color='orange',
    figsize=(12,5)
)

plt.xlabel('Genre')
plt.ylabel('Number of Titles')
plt.title('Top 10 Genres on Netflix')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[35]:


dataset['rating'].value_counts().head(10)


# In[36]:


import matplotlib.pyplot as plt

dataset['rating'].value_counts().head(10).plot(
    kind='bar',color='green',
    figsize=(10,5)
)

plt.xlabel('Rating')
plt.ylabel('Number of Titles')
plt.title('Top 10 Netflix Content Ratings')
plt.xticks(rotation=45)
plt.show()


# In[37]:


year_type = dataset.groupby(['year_added', 'type']).size().unstack(fill_value=0)

year_type


# In[38]:


year_type.plot(
    kind='line',
    figsize=(12,6)
)

plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.title('Movies vs TV Shows Added by Year')
plt.legend(title='Type')
plt.show()


# In[45]:


dataset.to_csv('netflix_cleaned.csv', index=False)


# In[46]:


dataset.to_csv(
    r'C:\Users\Hp\Downloads\netflix_cleaned.csv',
    index=False
)


# In[47]:


dataset.isnull().sum()


# In[50]:


dataset.iloc[6571]


# In[ ]:




