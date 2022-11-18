#!/usr/bin/env python
# coding: utf-8

# # US Alcohol Sales

# In[1]:


#import all of your modules

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#read in local csv file and create dataframe; I've named it 'df' to keep it simple

df = pd.read_csv('Data-Table1.csv')

print(df)


# In[3]:


# run the pandas.DataFrame.head to get a quick idea of what it looks like

df.head()


# In[4]:


# looking at type verifies that we have indeed created a DataFrame

print(type(df))


# In[5]:


# Let's print the data types of the columns in the data set

print(df.dtypes)


# # Data Clean Up 

# In[6]:


# We can sort out the rows for the years that we want to focus on, 2019 - 2021, using the 
# pandas.DataFrame.isin method

df = df[~df['Year'].isin([2017, 2018])]
print(df)


# In[7]:


# the last two columns are mostly empty of data so they can be dropped using the pandas.DataFrame.drop method
# I've left most of the columns for future use just in case

to_drop = ['PerCapita3yr',
          'PctChange']

df.drop(to_drop, inplace=True, axis=1)
print(df.head())


# In[8]:


# some of the rows have null entries and can be dropped as well

df.dropna(inplace=True)
print(df)


# In[9]:


# Rename FIPS column to State, so that it's more clear. In the original file, FIPS is the Geographic ID code.

df.rename(columns={"FIPS" : "State"}, inplace=True)
print(df)


# In[10]:


# Let's convert Gallons into an integer, so it's easier to use that data in the future. The column was designated 
# as a float type since there were rows that had null entries

df['Gallons'] = df['Gallons'].round().astype('int64')
print(df.dtypes)


# In[11]:


# we also don't need the state or beverage as integers, so let's convert those to a string

df['State'] = df['State'].astype('str')

df['Beverage'] = df['Beverage'].astype('str')

print(df.dtypes)


# In[12]:


# These are lists for the State and Beverage columns, that are included in the Assets/ folder 
# in the Definitions.csv file

statelist = ['Alaska','Colorado','Connecticut','Delaware','Florida','Illinois','Kentucky',
             'Massachusetts','Minnesota','Missouri','North Dakota','Tennessee','Texas' ]
print(statelist)


# In[13]:


alclist = ['spirits','wine','beer']

print(alclist)


# In[14]:


#for ease of use, since we've changed those columns to strings, we can go ahead and also change the 
#data in those columns and replace the numbers

df['Beverage'] = df['Beverage'].replace(['1', '2', '3'], ['spirits', 'wine', 'beer'])
df['State'] = df['State'].replace(['2','8','9','10','12','17','21','25','27','29','38','47','48'], 
                                  ['Alaska','Colorado','Connecticut','Delaware','Florida','Illinois',
                                   'Kentucky','Massachusetts','Minnesota','Missouri','North Dakota',
                                   'Tennessee','Texas'])
df.head


# # Data Analysis 

# In[15]:


# function to see total amount of gallons sold between years of 2019 - 2021

totalgallons = df['Gallons'].sum()
print('The total gallons of alcohol sold between the years of 2019 - 2021 is', totalgallons)


# In[16]:


#function to see total amount of gallons sold, filtered by year
print('Enter year (2019 through 2021):')
useryear = int(input()) 
gallonsyear = df.loc[df['Year'] == useryear, 'Gallons'].sum()
print('The total gallons of alcohol sold in', useryear, 'is', gallonsyear)


# In[17]:


# function to see total amount of gallons sold, filtered by state
print(statelist)
print('Enter state:' )
userstate = input()
stategallons = df.loc[df['State'] == userstate, 'Gallons'].sum()
print('The total gallons of alcohol sold in this state is', stategallons)


# In[18]:


# function to see total amount of gallons sold, filtered by type of beverage
print(alclist)
print('Enter beverage:' )
userbev = input()
bevtotal = df.loc[df['Beverage'] == userbev, 'Gallons'].sum()
print('The total gallons of', userbev, 'sold is', bevtotal)


# In[19]:


# function to see total amount of gallons sold, filtered by year, state and type of beverage;
#please refer to statelist and alclist  

def alcsales():
    print('Enter year (2019 through 2021):')
    useryear2 = int(input())

    print('Enter state:')
    userstate2 = input()

    print('Enter beverage:')
    userbev2 = input()
    
    gallonsfilt = df.loc[(df['Year'] == useryear2) & (df['State'] == userstate2) & (df['Beverage'] == userbev2),
                    'Gallons'].sum()

    print(gallonsfilt)

alcsales()


# In[20]:


#function to find average gallons sold per year
 
gallonavg = df.groupby('Year')['Gallons'].mean()

print(gallonavg)


# In[24]:


#function to find average gallons sold per type of beverage

beverageavg = df.groupby('Beverage')['Gallons'].mean()

print(beverageavg)


# In[26]:


#function to find average gallons sold per state

stateavg = df.groupby('State')['Gallons'].mean()

print(stateavg)


# In[54]:


#expression for Gallons per capita

gallonpercap = df['Gallons'] * df['PerCapita']

print(gallonpercap)


# In[57]:


#expression for smallest value of Gallons

gallonmin = df['Gallons'].min()

print(gallonmin)


# In[56]:


#xpressions for median value of Gallons

gallonmedian = df['Gallons'].median()

print(gallonmedian)


# # Graphs 

# In[27]:


# bar graph for total gallons sold in each state

plt = df.groupby(['State'])['Gallons'].sum()
plt.plot(kind='bar', title='Total Gallons by State', ylabel='Gallons(in billion)',
         xlabel='State', figsize=(9, 6), color="green")

print(plt.plot)


# ### This graph shows that a large majority of gallons sold is in Texas, and Florida. This could partially be attributed to Texas's large size as a state; more people means more alcohol sold. Florida is also well known for partying and for having a large population. I'm sure analysis with the per capita rates would also showcase some interesting findings.  
# ### I found it interesting that Kentucky was so low in the list as well.

# In[22]:


# graph of total alcohol sales, by year
plt = df.groupby(['Year'])['Gallons'].sum()
plt.plot(kind='pie', title='Total Gallons by Year', ylabel='Gallons',
         xlabel='Year', figsize=(8, 5), autopct='%1.1f%%')

print(plt.plot)


# ### This pie chart shows the percentage of the total gallons sold each year; I felt this format showcased the difference between the years better than a bar or line graph could. Notice that 2019 and 2020 are at least 10% higher than 2021. Given that Covid struck mostly in 2020, I can understand why so many gallons were sold; I'm sure that drinking was at an all time high since people were stuck isolating for months. What I find odd about this data is that it went down so low in 2021 to 25.7%. I think that further analysis would lead to some interesting conclusions.

# In[38]:


#graph that shows the total gallons grouped by state and type of beverage

gallons_state_beverage = df.groupby(['State','Beverage']) .agg(totalgallons = ('Gallons', 'sum'))

print(gallons_state_beverage)

gallons_state_beverage.plot(kind='bar', title='Total Gallons by State', ylabel='Gallons(in billions)',
         xlabel='State', figsize=(14, 6), color='red')

print(gallons_state_beverage.plot)


# ### This bar graph shows the total gallons of each beverage type, filtered by state. I wanted to find the difference in sales between the beverage types because I felt like it would be illuminating. For example, in Florida and Texas, the two states that had the majority of the gallons in the earlier graph, we can see that most of that is beer sales. In most states, beer makes up the majority of sales, with spirits and wine tending to be about the same per state. The US is still a very beer-centric country.

# In[ ]:




