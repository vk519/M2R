#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image,ImageDraw
import numpy as np
def num_iter(c,max_iter=50):
    z=0
    i=0
    while i<max_iter and abs(z)<=2:
        z=z*z+c
        i+=1
    return i 


# In[7]:


# convert pixel into complex number
n=500
re_start=-2
re_end=1/2
im_start=-1.5
im_end=1.5

scale_x=(re_end-re_start)/n
scale_y=(im_end-im_start)/n
im = Image.new('RGB', (n, n), (0, 0, 0))
draw = ImageDraw.Draw(im)
for x in range(n):
    for y in range(n):
        c=complex(re_start+x*scale_x,im_start+y*scale_y)
        color = 255 - int(num_iter(c,max_iter=50)* 255 / 50)
        draw.point([x, y], (color, color, color))
im
    


# In[1]:


1+2+3+4


# In[2]:


print('傻逼')


# In[ ]:




