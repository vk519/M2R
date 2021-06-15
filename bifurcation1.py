#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


def map(r, x):
    return r * x * (1 - x)


t = 10000
r = np.linspace(0, 4.0, t)

iterations = 1000
last = 100

x = 1e-5 * np.ones(t)
twocycle= 3.0*np.ones(t)
fourcycle= 3.45*np.ones(t)



ax1 = plt.figure(1)
for i in range(iterations):
    x = map(r, x)
    if i >= (iterations - last):
        plt.plot(r, x, ',b', alpha=.25)
        plt.title("Bifurication Diagram")
        plt.xlim(0, 4)
    plt.plot(twocycle,x,',r')
    plt.plot(fourcycle,x,',g')


# In[4]:


t=1000


# In[ ]:




