#!/usr/bin/env python
# coding: utf-8

# In[43]:


import random 
from tkinter import *


# In[45]:


def generate_list(emo, df_new):
    emo_list = df_new[df_new['emotion']  == emo]
    emo_list = emo_list['title'].tolist()
    sampling = random.choices(emo_list, k=4)

    master = Tk()

    listbox = Listbox(master)
    listbox.pack()
    listbox.insert(END, "Movie Recommendations")

    for item in sampling:
        listbox.insert(END, item)

    mainloop()


# In[ ]:




