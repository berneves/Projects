#!/usr/bin/env python
# coding: utf-8

# In[1]:


entries = ["2017-05-06", "2017-05-19", "2017-05-21", "2017-06-29", "2017-07-24", "2017-07-31", "2017-08-09", "2017-09-03", "2017-09-27", "2017-10-17", "2017-11-04", "2018-01-10", "2018-01-15", "2018-02-07", "2018-02-12", "2018-02-27", "2018-03-04", "2018-03-11", "2018-04-17", "2018-04-23", "2018-07-02", "2018-08-05", "2018-09-22", "2018-10-12", "2018-11-20", "2019-01-04"]


# In[2]:


exits = ["2017-05-15", "2017-05-19", "2017-06-25", "2017-07-22", "2017-07-28", "2017-08-05", "2017-08-23", "2017-09-18", "2017-10-07", "2017-10-30", "2017-12-23", "2018-01-13", "2018-01-30", "2018-02-08", "2018-02-21", "2018-03-02", "2018-03-09", "2018-04-09", "2018-04-21", "2018-07-26", "2018-07-26", "2018-08-24", "2018-09-27", "2018-10-17", "2018-11-25"]


# In[35]:


from datetime import datetime
date_format = "%Y-%m-%d"
for i in entries:
    a = datetime.strptime(i, date_format)
    for j in exits:
        b = datetime.strptime(j, date_format)
        delta = b - a
        if int(delta.days)<360:
            if int(delta.days)>180:
                print("dia de entrada: ",a.date(), "   dia de saída ",b.date(), "   Desqualificado")
            else:
                print ("dia de entrada: ",a.date(), "   dia de saída ",b.date(),"   Qualificado")
        else:
            print ("dia de entrada: ",a.date(), "   dia de saída ",b.date(),"   Qualificado") 
            


# In[ ]:




