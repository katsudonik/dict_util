#!/usr/bin/env python
# coding: utf-8

# # usage of dict_util

# ## loading libraries

# In[1]:


import json
import numpy as np
import pandas as pd
from dict_util.dict_util import DictUtil


# ## 1. initialize

# In[2]:


dict_util = DictUtil()


# ## 2. use functions

# ### dict_to_df
# 
# convert dict to df( pandas dataframe )

# In[3]:


en_l_dict = json.load(open( f'sample/en_left.json' , "r"))
en_l_df = dict_util.dict_to_df(en_l_dict)
en_l_df


# In[4]:


en_r_dict = json.load(open( f'sample/en_right.json' , "r"))
en_r_df = dict_util.dict_to_df(en_r_dict)
en_r_df


# In[5]:


en_r_df[en_r_df['key'] == 'message.descriptions.item_1']


# ### diff_df
# 
# compare two df ( result of `dict_to_df` ) to each other
# 
# - Nan: key is undefined
# 

# In[6]:


dict_util.diff_df(en_l_df, en_r_df)


# ### diff_by_df
# convert two dict to df ( with `dict_to_df` ) & compare them to each other ( with diff_df )
# 

# In[7]:


dict_util.diff_by_df(en_l_dict, en_r_dict)


# ### update_dict_df_val
# replace value with the other value
# 
# - undefined key is not merged

# In[8]:


new_en_r_df = dict_util.update_dict_df_val(en_r_df, en_l_df)
new_en_r_df


# ### df_to_dict
# convert df ( result of `dict_to_df` or `update_dict_df_val` ) to dict

# In[9]:


new_en_r_dict = dict_util.df_to_dict(new_en_r_df)
new_en_r_dict


# In[10]:


s = json.dumps(new_en_r_dict, ensure_ascii=False)
with open(f'sample/new_en_r.json', mode='w') as f:
    f.write(s)

