#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[18]:


import requests
from bs4 import BeautifulSoup


# In[52]:


page = requests.get("https://www.wikipedia.org/wiki/Main_page")


# In[53]:


page


# In[54]:


url = "https://www.wikipedia.org/wiki/Main_page"

page = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')


# In[55]:


header_tags = soup.find_all(['h1','h2','h3','h4','h5','h6'])


# In[58]:


for tag in header_tags:
    print(tag.text.strip())


# In[ ]:





# In[61]:


import requests
from bs4 import BeautifulSoup
import pandas as pd



# In[76]:


page = requests.get('https://www.imdb.com/search/title/?sort=user_rating,desc&groups=top_100')


# In[77]:


page


# In[78]:


soup = BeautifulSoup(page.content)
soup


# In[79]:


first_title = soup.find('div',class_="ipc-title-link-wrapper")
first_title


# In[80]:


first_title


# In[ ]:





# In[ ]:





# In[82]:


movies_df = pd.DataFrame({'Name':names, 'Rating':ratings, 'Year':years})
    print(movies_df)


# In[ ]:





# In[3]:


import requests
from bs4 import BeautifulSoup


# In[30]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants")


# In[31]:


page


# In[33]:


soup = BeautifulSoup(page.content)
soup


# In[34]:


first_title = soup.find('div',class_="restnt-info cursor")

first_title


# In[35]:


first_title.text


# In[37]:


titles = [] # emplty list for store the

for i in soup.find_all('div',class_="restnt-info cursor"):
    titles.append(i.text)
    

titles


# In[38]:


sta = soup.find('span',class_="filter-component-wrap cuisine-wrap")


# In[44]:


sta.


# In[48]:


location =[]

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[49]:


rating =[]

for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating    


# In[50]:


cuisine =[]

for i in soup.find_all('div',class_="filter-component-wrap cuisine-wrap"):
    cuisine.append(i.text)
cuisine    


# In[51]:


images = []

for i in soup.find_all('img',class_='no-img'):
    images.append(i['data-src'])
images   


# In[ ]:





# In[83]:


import requests
from bs4 import BeautifulSoup
import pandas  as pd


# In[85]:


page = requests.get('https://presidentofindia.nic.in/former-presidents.htm ')


# In[86]:


page


# In[100]:


soup = BeautifulSoup(page.content)
soup


# In[107]:


first_title = soup.find('div',class_="president-listing")
first_title


# In[110]:


first_title


# In[105]:


titles = []

for i in soup.find_all('div',class_="president-listing"):
    titles.append(i.text)
    

titles


# In[ ]:





# In[125]:


import pandas as pd

# Sample data for former finance ministers
former_ministers_data = [
    {'Name': 'Manmohan Singh', 'Term of Office': '1991-1996'},
    {'Name': 'P. Chidambaram', 'Term of Office': '2004-2008'},
    {'Name': 'Arun Jaitley', 'Term of Office': '2014-2019'},
    # we can add more 
]

df = pd.DataFrame(former_ministers_data)

print(df)


# In[ ]:




