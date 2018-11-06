
# coding: utf-8

# In[27]:


import numpy as np
from sklearn import svm, datasets
import csv

iris = datasets.load_iris()
print (iris)


# In[28]:


#x = iris.data
#y = iris.target
#print("Data: " + repr(len(x)))
#print("Target: " + repr(len(y)))
#print(x)


# In[29]:


import random
#trainingSet = []
#testSet = []
def splitDataSet(dataSet, trainingSet, testSet, split):
    for i in range(len(dataSet) - 1):
        for j in range(4):
            dataSet[i][j] = float(dataSet[i][j])
        if random.random() < split:
            trainingSet.append(dataSet[i])
        else:
            testSet.append(dataSet[i])
            
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# In[30]:


#print("trainingSet: " + repr(len(trainingSet)))
#print("testSet: " + repr(len(testSet)))


# In[31]:


import math

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']

distance = euclideanDistance(data1, data2, 3)
print('Distance: ' + repr(distance))


# # getNeighbors: will return that testInstance belongs to which class 
# # [IN] trainingSet
# # [IN] testInstance
# # [IN] k nearest neighbors
# # [OUT] Neighbor which testInstance belongs to

# In[32]:


import operator
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        #print('dist: ', dist, ' ', trainingSet[x])
        distances.append((trainingSet[x], dist))

    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# In[33]:


#trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
#testIns = [5, 5, 5]
#k = 1
#neighbors = getNeighbors(trainSet, testIns, 1)
#print(neighbors)


# # getResponse: check test instance belongs to which class
# # [IN] Output of getNeighbors(K-Nearest Neigbors)
# # [Out] test Instance belongs to which class

# In[34]:


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse = True)
        return sortedVotes[0][0]


# In[35]:


#neighbors = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
#response = getResponse(neighbors)
#print(response)


# # getAccuracy: calculate ratio of total correct prediction to all the prediction made

# In[36]:


def getAccuracy(testSet, predictions):
    correct = 0;
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


# In[37]:


#testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
#predictions = ['a', 'a', 'a']
#accuracy = getAccuracy(testSet, predictions)
#print(accuracy)


# In[39]:


def main():
    #iris = datasets.load_iris()
    #x = iris.data
    #y = iris.target
    #z = iris.target_names
    
    #print("Data: " + repr(len(x)))
    #print("Target: " + repr(len(y)))
    #print(x)
    
    trainingSet = []
    testSet = []
    split = 0.67
    #splitDataSet(x, trainingSet, testSet, split)
    loadDataset('irisData.txt', split, trainingSet, testSet)
    print("trainingSet: " + repr(len(trainingSet)))
    print("testSet: " + repr(len(testSet)))
    print(trainingSet)
    
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print("Predicted: " + repr(result) + ", Actual: " + repr(testSet[x][-1]))
    
    accuracy = getAccuracy(testSet, predictions)
    print("Accuracy: " + repr(accuracy) + "%")
    
main()
    
    

