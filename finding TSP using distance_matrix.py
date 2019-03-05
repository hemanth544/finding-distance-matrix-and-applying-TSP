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
      #print(distancex)
      
      
      # Distance callback
      def create_distance_callback(dist_matrix):
            # Create a callback to calculate distances between cities.
            def distance_callback(from_node, to_node):
                  return int(dist_matrix[from_node][to_node])
            return distance_callback

      def main():
            # Cities
            city_names =updated_list
            # Distance matrix
            dist_matrix =distancex
            tsp_size = len(city_names)
            num_routes = 1
            depot = 0
            # Create routing model
            if tsp_size > 0:
                  routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
                  search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
                  # Create the distance callback.
                  dist_callback = create_distance_callback(dist_matrix)
                  routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
                  # Solve the problem.
                  assignment = routing.SolveWithParameters(search_parameters)
                  if assignment:
                        # Solution distance.
                        print("Total distance: " + str(assignment.ObjectiveValue()) + " KiloMeters\n")
                        # Display the solution.
                        # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
                        route_number = 0
                        index = routing.Start(route_number) # Index of the variable for the starting node.
                        route = ''
                        while not routing.IsEnd(index):
                              # Convert variable indices to node indices in the displayed route.
                              route += str(city_names[routing.IndexToNode(index)]) + ' -> '
                              index = assignment.Value(routing.NextVar(index))
                        route += str(city_names[routing.IndexToNode(index)])
                        print("Route:\n\n" + route)
                  else:
                        print('No solution found.')
            else:
                  print('Specify an instance greater than 0.')
      if __name__ == '__main__':
            main()
                  


