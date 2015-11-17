__author__ = 'f403'
import numpy as np
import Perception as p
if __name__=="__main__":
	X=np.array([[3,3],[4,3],[1,1]])
	Y=np.array([1,1,-1])
	ppn=p.perception(1)
	ppn.train(X,Y)
	print(ppn.w_)
	print(ppn.b_)
