import os
import kNN

CURRENT_DIR = os.path.dirname(__file__)

groups, labels = kNN.createDataset()

print kNN.classify0([0,0,0],groups,labels,3)

dataSetFile = os.path.join(CURRENT_DIR + '/datingTestSet.txt')

datingDataMat,datingLabels = kNN.file2matrix(dataSetFile)

print kNN.classify0([40920,  8.326976,	0.953952],groups,labels,3)