import numpy as np
import time
seqLen = 1000
def popSort(arrySeq):
	seqLen = len(arrySeq)
	for i in range(seqLen):
		for j in range(seqLen-i-1):
			if arrySeq[j]>arrySeq[j+1]:
				arrySeq[j],arrySeq[j+1] = arrySeq[j+1],arrySeq[j]
	return arrySeq
np.random.seed(123)
arry = np.random.rand(1, seqLen)[0]
start = time.clock()
a = popSort(arry)
end = time.clock()
print("冒泡法排序用时：",round(end-start,2))

def quickSort(arrySeq):
	def seg(lowC,highC):
		if lowC>=highC:
			return
		flag = arrySeq[highC]
		lowCurse = lowC-1
		for highCurse in range(lowC,highC+1):
			if arrySeq[highCurse]>flag:
				pass
			else:
				lowCurse+=1
				if lowCurse < highCurse:
					arrySeq[lowCurse],arrySeq[highCurse] = arrySeq[highCurse],arrySeq[lowCurse]				 
		lowCurse+=1
		if lowCurse<highC:
			arrySeq[lowCurse],arrySeq[highC] = arrySeq[highC],arrySeq[lowCurse]
		seg(lowC,lowCurse-2)
		seg(lowCurse,highC)

	seg(0,len(arrySeq)-1)
	return 1
np.random.seed(123)
arry = np.random.rand(1, seqLen)[0]
start = time.clock()
arrySeq = quickSort(arry)
end = time.clock()
print("快速排序用时：",round(end-start,2))

 