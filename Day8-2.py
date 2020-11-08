#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 詢問使用者心情分數1~10分，並依據分數給出建議，若是大於(含)6就給予「吃日本料理」，若是小於6就給予「吃義大利麵」
today_mood = int(input('今天心情1~10分:'))
type(today_mood)

if today_mood >= 6:
    print('吃義大利麵')
elif today_mood < 6:
    print('吃日本料理')


# In[ ]:




