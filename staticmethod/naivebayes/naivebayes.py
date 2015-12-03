__author__ = 'f403'
#coding=utf-8
import numpy as np
class Naivebayes:
	classlabel=[]
	Coccur=[]
	prior=[]
	post_prob=[]
	attributes=[]
	@staticmethod
	def train(traindata,trainlabel):
		Naivebayes.prior=Naivebayes.priorprobility(trainlabel)
		Naivebayes.post_prob=Naivebayes.conprobility(traindata,trainlabel)


	@staticmethod
	def priorprobility(trainlabel):
		'''计算先验概率'''
		Naivebayes.classlabel=np.unique(trainlabel)
		Naivebayes.Coccur=[0]*len(Naivebayes.classlabel)
		for i in range(len(Naivebayes.classlabel)):
			for x in trainlabel:
				if x==Naivebayes.classlabel[i]:
					Naivebayes.Coccur[i]+=1

		#Naivebayes.Coccur=np.bincount(trainlabel)
		Naivebayes.classdict=dict(zip(Naivebayes.classlabel,Naivebayes.Coccur))
		prior=[x/len(trainlabel) for x in Naivebayes.Coccur]
		return prior

	@staticmethod
	def conprobility(traindata,trainlabel):
		try:
			numofatt=len(traindata[0])
		except IndexError as e:
			return  None

		post_prob=[]
		for i in range(0,numofatt):
			att=Naivebayes.attribute(traindata,i)
			uniqueatt=np.unique(att)
			Naivebayes.attributes.append(uniqueatt)
			conprob=[]
			for k in range(len(Naivebayes.classlabel)):
				times=[0]*len(uniqueatt)
				for j in range(len(uniqueatt)):
					for h in range(len(att)):
						if att[h]==uniqueatt[j] and trainlabel[h]==Naivebayes.classlabel[k]:
							times[j]=times[j]+1

				conprob.append([x/sum(times) for x in times])

			post_prob.append(conprob)
		return  post_prob


	@staticmethod
	def attribute(traindata,dim):
		return [x[dim] for x in traindata]

	@staticmethod
	def predict(predictdata):
		prob=[1]*len(Naivebayes.classlabel)
		for i in range(len(Naivebayes.classlabel)):
			for j in range(len(predictdata)):
				loc=np.searchsorted(Naivebayes.attributes[j],predictdata[j])
				prob[i]=prob[i]*Naivebayes.post_prob[j][i][loc]
			prob[i]=prob[i]*Naivebayes.prior[i]

		maxloc=np.argmax(prob)
		return Naivebayes.classlabel[maxloc],prob[maxloc]




if __name__=='__main__':
	traindata=[[1,'S'],[1,'M'],[1,'M'],[1,'S'],[1,'S'],[2,'S']
	           ,[2,'M'],[2,'M'],[2,'L'],[2,'L'],[3,'L'],[3,'M'],
	           [3,'M'],[3,'L'],[3,'L']]
	trainlabel=[-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
	Naivebayes.train(traindata,trainlabel)
	print(Naivebayes.prior)
	print(Naivebayes.Coccur)
	print(Naivebayes.post_prob)
	(preclass,prob)=Naivebayes.predict([2,'S'])
