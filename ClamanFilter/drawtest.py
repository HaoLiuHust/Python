__author__ = 'f403'
import matplotlib.pyplot as plt
import numpy
from CalmanFilter import calmanfiter
f=open("output.txt",'r')
data=f.readlines()
data=[round((float)(x),3) for x in data]
print(data)
plt.grid()
plt.plot(data)

xhat=calmanfiter(data)
plt.plot(xhat)
print(xhat)
plt.show()