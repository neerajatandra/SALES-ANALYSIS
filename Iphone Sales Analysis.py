#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


dataset = pd.read_csv('Order_details(masked).csv')


# In[4]:


dataset


# In[5]:


dataset.head()


# In[6]:


dataset.tail()


# In[18]:


#Here we taken Transaction
#data column
dataset['Time'] = pd.to_datetime(dataset['Transaction Date'])


# In[19]:


#After that we extracted hour
#From Transaction data column
dataset['Hour'] = (dataset['Time']).dt.hour


# In[22]:


# n =24 in this case, can be modified
# as per need to see top 'n' busiest hours
timemost1 = dataset['Hour'].value_counts().index.tolist()[:24] 

timemost2 = dataset['Hour'].value_counts().values.tolist()[:24]


# In[23]:


tmost = np.column_stack((timemost1,timemost2))

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))


# In[25]:


timemost = dataset['Hour'].value_counts()
timemost1 = []

for i in range(0,23):
    timemost1.append(i)
    
timemost2 = timemost.sort_index()
timemost2.tolist()
timemost2 = pd.DataFrame(timemost2)


# In[26]:


plt.figure(figsize=(20, 10))

plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
          fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)

plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.show()


# In[ ]:




