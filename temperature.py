# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:55:08 2015

@author: Di3Walkur3
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#np.log is equal to ln(x)
#T is final temp
#C is room temp
#Ti is initial temp at time of arrival
#e is expontenial
#-k is cooling number
#t is time between the two temps
Ti = float(input('Initial temperature of object: '))
T = float(input('Final Temperature of object: '))
C = float(input('Temperature of the surroundings: '))
t = float(input('Time between the two temperatures: '))

k = (np.log((T-C)/(Ti-C))/t)
print('k= ',k)

minutes = (np.log((Ti-C)/(T-C))/-k)
hours = float(minutes/60)

print('Hours: ',hours)
print('Minutes: ',minutes)

x = np.linspace(0, t, 100)
b = float(Ti)
y = (C + (b-C) * np.exp(k * x))
#pickle_out = open('tempdata.pickle','wb')
#   pickle.dump(main_df, pickle_out)
#    pickle_out.close()    

plt.title('Netwons Law of Cooling')
plt.plot(x, y, '-k')
plt.xlabel('x= Time in minutes'); plt.ylabel('y=Objects Temperature')

