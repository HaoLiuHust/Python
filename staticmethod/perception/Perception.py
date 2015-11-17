__author__ = 'f403'
import numpy as np
class perception:
	def __init__(self,eta=0.1):
		self.eta=eta

	def train(self,X,y):
		self.w_ = np.zeros(X.shape[1])
		self.w_.astype('int64')
		self.b_=0
		self.cost_ = []
		error = 0
		while True:
			for xi,target in zip(X,y):
				flag=False
				if target!=self.predict(xi):
					self.w_+=(self.eta*target*xi)
					self.b_+=(self.eta*target)
					print(self.w_)
					flag=True
					break

			if flag is False:
				break


	def predict(self,xi):
		y=np.dot(xi,self.w_)+self.b_
		return np.where(y>0,1,-1)
