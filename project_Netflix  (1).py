#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np  #library  for arrays &matrics
import pandas as pd
import seaborn as sas
sas.set(color_codes=True) # library use for graph 
import matplotlib.pyplot as plt  #FOR visualization
from matplotlib import style
import plotly.express as px # for data visualization


# In[39]:


df =pd.read_csv('C:\\Users\\DhamiPC\\Desktop\\git folder\\NETFLIX\\netflix_titles.csv')


# ### Data Understanding

# ##### top 2 records

# In[40]:


df.head(2)


#  #### bottom 2 records

# In[41]:


df.tail(2) 


# #### No. of rows and column

# In[42]:


df.shape


# #### Total no. of values

# In[43]:


df.size 


# ###### datatype of each column

# In[44]:


df.dtypes


# ###### info contains the number of columns

# In[45]:


df.info()


# In[46]:


df.isna()


# ###### No.of missing values in each row and column

# In[47]:


df.isna().sum()


# #### change data type from object to datetime64

# In[48]:


df['date_added'] = pd.to_datetime(df['date_added']) 


# In[49]:


df.dtypes


# # Missing values

#  ##### Nil values of director, rating ,cast , country will be replace by unavailable

# In[50]:


df.fillna({'director':'unavailable','rating':'unavailable','cast':'unavailable','country':'unavailable'}, inplace=True)
df.isna().sum()


# ##### shows the null values of data

# In[51]:


df[df.date_added.isnull()]  


# ###### replace blank date_added with most occuring date

# In[52]:


most_recent_entry_date=df['date_added'].max()
df.fillna({'date_added':most_recent_entry_date}, inplace =True)


# In[53]:


df[df.type == 'TV Show'] 


# #### shows all column in describe 

# In[54]:


df.describe() 


# #### here we can check all the catigories with heighest ,lowest and most occuring counts 

# In[55]:


df[(df['type']== 'Movie') | (df['rating']=='TV-PG')]   # we have use logical op (OR) 


# In[56]:


df[(df['type']=='Movies') +(df['rating']=='TV-PG')] #total  no of TV shows in US /WE ARE USING AND OPERATOR


# In[57]:


df[(df['rating']== 'TV-PG')].head()   # shown common rating (TV-PG)


# In[58]:


df[(df['country'] =='United States')]


# In[59]:


df['director'].value_counts() 


# ##### director with highest tv and movies

# In[60]:


df.describe()


# In[61]:


df.head(5)


# In[62]:


df['type'].value_counts()


# In[63]:


df.title.value_counts()


# In[64]:


df[df['cast']=='David Attenborough'].head(2)


# ###### highest no of user watching netflix in United States 

# In[65]:


df['country'].value_counts().head(10 )


# ###### In 2020 most progams were added 

# In[66]:


df['date_added'].value_counts().head(5)


# ##### IN 2018 most programs were released 

# In[67]:


df['release_year'].value_counts().head(5)


# In[68]:


df['duration'].value_counts()


# #### here we have 2 more columns 

# In[69]:


df['added_year'] = df['date_added'].dt.year
df['added_month'] = df['date_added'].dt.month


# In[70]:


df.head(2)


# #### max programs added in 12th month

# In[71]:


df['added_month'].max() 


# #### max programs added in 2020 year

# In[72]:


df['added_year'].max()


# #### Documentries are mostly watched on Netflix

# In[73]:


df['listed_in'].value_counts()


# # visualization

# ##### Here movies are mostly watched in netflix

# In[74]:


sas.countplot(x='type',data = df)     #shows type wrt count
plt.title('count vs Type of shows')


# ##### Here documentaries are the most popular genres on netflix

# In[75]:


plt.figure(figsize=(10,8))  
sas.countplot(y='listed_in',order = df['listed_in'].value_counts().index[0:10],data = df) #graph for genres
plt.title('top 10 genres content on netflix')


# In[76]:


plt.figure(figsize=(10,5)) #setting figure size 
sas.countplot(x='release_year',order = df['release_year'].value_counts().index[0:10],data = df) #graph for 'release_yea
plt.title('country wise content on ntflix')


#  ##### During end of the year(winters) most most of the Netflix Shows are released 

# In[77]:


plt.figure(figsize= (9,6))  
sas.countplot(x='rating',order = df['rating'].value_counts().index[0:10],data = df)
plt.title('rating of shows on netflix vs count')


#  TV-MA= mature audience 
#  TV-14=for <14
#  TV-PG=parental guidance 
#  U17 
#  R=U17 
#  PG-13=U13 
#  NR= unrated 
#  TV-Y7=Child for age7&more
#  TV-G = for all age 
#  TV-Y= for childr &all age

#  ###### Top 10 countries watching Netflix 

# In[78]:


plt.figure(figsize=(12,6)) #setting figure size 
sas.countplot(y='country',order = df['country'].value_counts().index[0:10],data = df)  #combine graph 📊 
plt.title('country wise content on ntflix')


# In[79]:



df_movies=df[df["type"]=="Movie"]
df_tvshows=df[df["type"]=="TV Show"]


# In[80]:


plt.figure(figsize=(12,6)) 
sas.countplot(y='country',order = df['country'].value_counts().index[0:10],data = df_movies)  
plt.title('Top 10 country producing movies on ntflix')


# # Top 10 country producing movies on ntflix

# In[81]:


plt.figure(figsize=(12,6)) 
sas.countplot(y='country',order = df['country'].value_counts().index[0:10],data =df_tvshows)  
plt.title('Top 10 country producing TVshows on ntflix')


# Top 10 country producing tv_shows on netflix

# In[82]:


plt.figure(figsize=(10,8))
df_tvshows.release_year.value_counts().head(20).plot(kind='bar',color='maroon')
plt.title('top 20 year in which tv_show are released')
#plt.xlable('')
#plt.ylable('')
plt.legend()
plt.show()


# In[83]:


plt.figure(figsize=(10,8))
df_movies.release_year.value_counts().head(20).plot(kind='bar',color='maroon')
plt.title("Top 20 years in which most movies are released")
plt.xlabel("Release year")
plt.ylabel("Counts")
plt.legend()
plt.show()


# ##### during winters/ end of the year most of the shows release
# 

# In[84]:


df['added_month'].value_counts().head(10).plot(kind='bar')
plt.title("Monthwise show release")
plt.legend()
plt.xlabel("Months")
plt.show()


# ###### In year heighest no of shows are released

# In[85]:


# In which month most of the shows release?
df['added_year'].value_counts().head(10).plot(kind='bar')
plt.title("Year wise show release")
plt.legend()
plt.xlabel("Days")
plt.show()


# In[86]:


plt.figure(figsize=(10,8))
sas.countplot(x='rating',hue='type',data=df)
plt.title("Plot of rating by type")
plt.show()


# ###### MEAN / MEDIAN & MODE

# In[87]:


mean=df.mean()
mean


# In[88]:


mode=df.mode()
mode


# In[89]:


mean1=df['added_year'].mean()


# In[90]:


mean1


# In[91]:


mode1=df['added_year'].mode()


# In[92]:


mode1


# In[93]:


median=df['added_year'].median()


# In[94]:


median


# ##### Describe Function

# In[95]:


df['release_year'].describe()


# ##### Scewness

# In[96]:


df.skew()


# ##### negative skew(left skew)

# In[97]:


sas.histplot(df.release_year, kde = True)


# In[98]:


#plt.figure(figsize=(2,2))
sas.histplot(df.show_id, kde = True) 


# In[99]:


mean=df.release_year.mean()
mean


# In[100]:


std_dev=df.release_year.std()
std_dev


# In[101]:


df.head()


# In[102]:


df['listed_in'].replace(['Movies','TV'],[' ',' '],inplace =True)


# In[103]:


df.head()


# In[104]:


df.iloc[1][2]


# In[105]:


df.shape


# In[106]:


z = df.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating', 
                  title=' Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()


# In[107]:


df['directors'].value_counts(5)


# In[ ]:


df['director']=df['director'].fillna('No Director Specified')
filtered_directors=pd.DataFrame()
filtered_directors=df['director'].str.split(',',expand=True).stack()
filtered_directors=filtered_directors.to_frame()
filtered_directors.columns=['Director']
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors=directors[directors.Director !='No Director Specified']
directors=directors.sort_values(by=['Total Content'],ascending=False)
directorsTop5=directors.head()
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()


# In[ ]:





# In[ ]:




