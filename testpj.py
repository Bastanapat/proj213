import pandas as pd 
import csv
import os
from datetime import date
from datetime import datetime
from datetime import time
import numpy as np

try:
    os.makedirs("c:/poject/test")
except FileExistsError:
    pass  


os.chdir("c:/poject/test")
with open('testpjinno.csv','w',newline="") as f:
    mv = csv.writer(f)
    mv.writerow(['day','mount','year','hour','minute','secone','temp','humid'])
    
   



# k = np.genfromtxt("testpjinno.csv",delimiter=',',skip_header=1)
# u = 0
# temp_0min = []
# humid_0min = []  

# temp_1min = []
# humid_1min = [] 
# for i in k:
#     u+=1
#     if i[0] == datetime.now().day: #day
#         if i[3] == 0: # hour
#             if i[4] == 0: #minute
#                 temp = k[u-1,5]
#                 humid = k[u-1,6]
#                 temp_0min.append(temp)
#                 humid_0min.append(humid)
#                 # print(u-1,end=' ')
#                 # print(temp,end=' ')
#                 # print(humid)
#             elif i[4] == 1: #minute
#                 temp1 = k[u-1,5]
#                 humid1 = k[u-1,6]
#                 temp_1min.append(temp1)
#                 humid_1min.append(humid1)
# temp0min1 = np.mean(temp_0min)
# humid0min1 = np.mean(humid_0min)

# temp1min1 = np.mean(temp_1min)
# humid1min1 = np.mean(humid_1min)
# print(temp0min1)
# print(humid0min1)
# print(temp1min1)
# print(humid1min1)