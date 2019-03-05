#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
sheet=['Sheet1','Sheet2','Sheet3','Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9','Sheet10']
for i in range(len(sheet)) :
      df1=pd.read_excel("sort data2.xlsx", sheet_name=sheet[i])
      rice=df1['FULL RICE'].sum()+df1['3qrice'].sum()*(3/4)+df1['HALF RICE'].sum()*(1/2)+df1['1qrice'].sum()*(1/4)
      sambar=df1['Full CURRY'].sum()+df1['3qcurry'].sum()*(3/4)+df1['HALF CURRY'].sum()*(1/2)+df1['1qcurry'].sum()*(1/4)
      total=rice+sambar
      print(total)

      if total<=30:
            print("The Capacity of RICE and CURRY is less than 30 so we can assign JAZZE to it")
      elif total>30 and total<=45:
            print("The Capacity of RICE and CURRY is less than 45 so we can assign TATA ACE to it")
      else:
            print("The Capacity of RICE and CURRY is greater than 45 so we can assign BOLERO to it")
      

