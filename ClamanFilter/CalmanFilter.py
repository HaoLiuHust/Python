__author__ = 'f403'
import numpy
def calmanfiter(dataorigin):
	n_iter=len(dataorigin)
	sz=(n_iter,)
	Q=1e-5

	xhat=numpy.zeros(sz)
	P=numpy.zeros(sz)
	xhatminus=numpy.zeros(sz)
	Pminus=numpy.zeros(sz)
	K=numpy.zeros(sz)

	R=0.1**3
	xhat[0]=dataorigin[0]
	P[0]=1.0
	for k in range(1,n_iter):
		xhatminus[k]=xhat[k-1]
		Pminus[k]=P[k-1]+Q
		K[k]=Pminus[k]/(Pminus[k]+R)
		xhat[k]=xhatminus[k]+K[k]*(dataorigin[k]-xhatminus[k])
		P[k]=(1-K[k])*Pminus[k]

	xhat=[round((float)(x),3) for x in xhat]
	return xhat