#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd #For Data Analysis
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import googlemaps #For google location based distance calculation
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyCD1i7JMdH65zFPzA-7hNvQ2sClN2I5-as')
#Creating Excel Sheets in a List
sheet=['Sheet1','Sheet2','Sheet3','Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9','Sheet10']
#Creating Optained Clusters in a List
Cluster=['Cluster:0','Cluster:1','Cluster:2','Cluster:3','Cluster:4','Cluster:5','Cluster:6','Cluster:7','Cluster:8','Cluster:9']
for i in range(len(sheet)):
      df=pd.read_excel("sort data1.xlsx", sheet_name=sheet[i])
      data=list(df[Cluster[i]]+' chittor district'+' andhra pradesh')
      data.remove('school name chittor district andhra pradesh')
      data.remove('total chittor district andhra pradesh')
      updated_list=list(set(data))
      updated_list.remove(updated_list[0])
      #print(updated_list)
      print("\n")
      distancex=[]
      for i in range(len(updated_list)):
            x=updated_list[i]
            distancey=[]
            for j in range(len(updated_list)):
                  y=updated_list[j]
                  dist = gmaps.distance_matrix(x,y)['rows'][0]['elements'][0]['distance']['value']
                  
                  my_dist=dist/1000
                  distancey.append(my_dist)
            #print(distancey)
            
            distancex.append(distancey)
      print(distancex)

