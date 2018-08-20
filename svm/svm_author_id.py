#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
#Slicing training features and labels
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

#clf = SVC(kernel="linear")
#clf = SVC(C=10000.0, kernel="rbf")
#clf.fit(features_train, labels_train)
#pred = clf.predict(features_test)
#count=0
#for i in pred:
#    if i==1:
#        print i
#        count=count+1
#print count


#clf = SVC()
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
            decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
                max_iter=-1, probability=False, random_state=None, shrinking=True,
                    tol=0.001, verbose=False)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print pred
#print accuracy_score(pred, labels_test)
#########################################################


