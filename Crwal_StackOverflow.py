#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup

res= requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text,"html.parser")

questions = soup.select(".question-summary")
users = soup.find('a').text

for que in questions:
    q=que.select_one('.question-hyperlink').getText()
    user=que.select_one('.user-details').getText()

    print({user : q})


# In[ ]:





# In[ ]:




