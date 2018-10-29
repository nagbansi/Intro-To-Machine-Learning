#!/usr/bin/python

import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
data.target_names

#Defining all the categories
categories = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
                'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey',
                'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns',
                'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

#training the data on these categories
train = fetch_20newsgroups(subset = 'train', categories = categories)
#testing the data for these categories
test = fetch_20newsgroups(subset = 'test', categories = categories)
#printin trainh data
print(len(test.data))
print(len(train.data))

#Importing neccesary packages
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

#Creating a model based on multinomial naive bayes
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

#Training the model with train data
model.fit(train.data, train.target)

##Creating labels for test data
labels = model.predict(test.data)

#Creating confusion matrix and heat map
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False
            , xticklabels = train.target_names, yticklabels = train.target_names)

#Ploting hratmap of confusion matrix
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.savefig("/home/nagbansi/Pictures/naive_bayes.png")
