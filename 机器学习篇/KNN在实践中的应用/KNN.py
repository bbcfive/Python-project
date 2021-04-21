from array import array

from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group , labels

def classify(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize , 1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = { }
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
		sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fr = open(filename)
	array0lines = fr.readlines()
	number0fLines = len(array0lines)
	returnMat = zeros((number0fLines,3))
	classLabelVector = []
	index = 0
	for line in array0lines:
		line = line.strip()
		listFormLine = line.split('\t')
		returnMat[index,:] = listFormLine[0:3]
		classLabelVector.append(int(listFormLine[-1]))
		index +=1
	return returnMat,classLabelVector