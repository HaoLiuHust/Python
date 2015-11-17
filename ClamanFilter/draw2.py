__author__ = 'f403'
import matplotlib.pyplot as ply
import numpy
from CalmanFilter import calmanfiter
f=open("outputSpineMid.txt",'r')
data=f.readlines()

datax=[round((float)(x.strip().split()[0]),3) for x in data[:150]]
datay=[round((float)(x.strip().split()[1]),3) for x in data[:150]]
dataz=[round((float)(x.strip().split()[2]),3) for x in data[:150]]

ply.subplot(2,2,1)
ply.grid()
print(datax)
ply.plot(datax,color="blue",label="X")
datafilterdx=calmanfiter(datax)
ply.plot(datafilterdx,color="red")
ply.subplot(2,2,2)
ply.grid()
print(datay)
ply.plot(datay,color="blue",label="X")
datafilterdy=calmanfiter(datay)
ply.plot(datafilterdy,color="red")
ply.subplot(2,2,3)
ply.grid()
print(dataz)
ply.plot(dataz,color="blue",label="X")
datafilterdz=calmanfiter(dataz)
ply.plot(datafilterdz,color="red")

ply.show()