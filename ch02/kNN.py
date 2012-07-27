from numpy import *
import csv
import operator

def createDataset():
  group = array([[1.0,1.1,0],[1.0,1.0,0],[0,0,0],[0,0.1,0]])
  labels = ['A','A','B','B']
  return group, labels

def file2matrix(filename):
  fr = open(filename)
  numberOfLines = len(fr.readlines())
  returnMat = zeros((numberOfLines,3))
  classLabelVector = []
  fr = open(filename)
  index = 0
  for line in fr.readlines():
    line = line.strip()
    listFromLine = line.split('\t')
    returnMat[index:] = listFromLine[0:3]
    classLabelVector.append(int(listFromLine[-1]))
    index += 1
  return returnMat, classLabelVector
    
def classify0(inX,dataSet,labels,k):
  # Length of Y
  dataSetSizeY = dataSet.shape[0]
  # Create an empty matrix the same with inX
  # as the default value and subtract.
  diffMat = tile(inX,(dataSetSizeY,1)) - dataSet
  # Square the matrix
  sqDiffMat = diffMat**2
  # Sum the values along the X axis
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances**0.50
  # Sort
  sortedDistIndicies = distances.argsort()
  print sortedDistIndicies
  classCount = {}
  for i in range(k):
      voteIlabel = labels[sortedDistIndicies[i]]
      classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
  sortedClassCount = sorted(classCount.iteritems(),
      key=operator.itemgetter(1), reverse=True)
  return sortedClassCount[0][0]