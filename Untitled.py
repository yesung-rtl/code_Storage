#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df


# In[11]:


df.T 


# In[15]:


df.loc[dates[2], "C"], df.iloc[2, 2]


# In[ ]:


df[df > -1]

