#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import json
from nltk.stem.porter import PorterStemmer 


# In[3]:


movies  = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")


# In[4]:


movies.info()
#id 
#keywords
#overview
#title
#genres


# In[5]:


credits.info()


# In[6]:


movies = pd.merge(movies , credits , on="title")


# In[7]:


movies = movies[["movie_id","title","genres","keywords","overview","cast","crew"]].copy()


# In[8]:


movies.shape


# In[9]:


movies=movies.dropna()


# In[10]:


movies.head(2)                    


# In[11]:


movies.iloc[0,2]


# In[12]:


ps = PorterStemmer()
def extract_genres(s):
    try:
        data = json.loads(s)
        names = [item["name"] for item in data]
        names = " ".join(names)
        return names
    except:
        return ""

def extract_cast(s):
    try:
        data = json.loads(s)
        names = [item["name"] for item in data]
        names = " ".join(names[0:3])
        return names
    except:
        return ""
def extract_director(s):
    try:
        data = json.loads(s)
        for item in data:
            if item["job"] == "Director":
                return item["name"]
    except:
        return ""
def stem_word(s):
    try :
        l=[]
        for i in s.split():
            l.append(ps.stem(i))
        return " ".join(l)
    except:
        return ""


# In[13]:


movies["genres"] = movies["genres"].apply(extract_genres)


# In[14]:


movies["keywords"] = movies["keywords"].apply(extract_genres)


# In[15]:


movies["cast"] = movies["cast"].apply(extract_cast)


# In[16]:


movies["crew"] = movies["crew"].apply(extract_director)


# In[17]:


movies["overview"] = movies["genres"] + " " + movies["keywords"] + " " + movies["overview"] + " " + movies["cast"] + " " + movies["crew"]


# In[18]:


movies = movies[["movie_id","title","overview"]].copy()


# In[19]:


movies["overview"]=movies["overview"].apply(stem_word)


# In[20]:


movies["title"] = movies["title"].str.lower()


# In[21]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000 , stop_words="english")


# In[22]:


vector = cv.fit_transform(movies["overview"]).toarray()


# In[23]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vector)


# In[24]:


def recommend(movie):
    try:
        idx = movies[movies["title"]==movie].index[0]
        row = similarity[idx]
        row = list(enumerate(row))
        row.sort(reverse=True , key = lambda x :x[1])
        l = []
        for i in range(1,6):
            l.append(movies["title"][row[i][0]])
        return l
    except:
        return ""
    
       


# In[25]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




