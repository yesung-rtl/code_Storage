#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df


# In[11]:

# 1. df의 로우와 컬럼을 바꿔라
df.T 


# In[15]:

# 2. loc과 iloc을 각각 사용하여 0.772899의 값을 찾아 프린트해라
df.loc[dates[2], "C"], df.iloc[2, 2]


# In[ ]:

# 3. df 중 -1보다 큰 값만 선택해라
df[df > -1]

