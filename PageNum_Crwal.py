#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup

res= requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text,"html.parser")

questions = soup.select(".question-summary")

page_num = int(soup.find('div', class_ ='s-pagination--item is-selected').getText())

page_limit = int(input('Enter no. of pages to crawl : '))
while page_num != page_limit:
    for que in questions:
        q=que.select_one('.question-hyperlink').getText()
        user=que.select_one('.user-details').getText()
        print({user : q})


# In[ ]:





# In[ ]:




