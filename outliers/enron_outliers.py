#!/usr/bin/python

import matplotlib
matplotlib.use("Agg")
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import operator

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

#for j, i in data_dict.items():
#    print data_dict[j]['total_payments'],j 

#Identify the Biggest Enron Outlier
max_total_payments = max([data_dict[j]['total_payments'] for j in data_dict if data_dict[j]['total_payments'] != 'NaN' and j != 'TOTAL'])
print "total_payments to biggest outlier: ", max_total_payments
outlier_name = [j for j in data_dict if data_dict[j]['total_payments'] == max_total_payments] 
print "biggest outlier: ", outlier_name


#Does this outlier seem like a data point that we should include when running machine learning on this dataset? 
#Or should we remove it?

#Ans: We can remove it



for point in data:
        salary = point[0]
        bonus = point[1]
        matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
matplotlib.pyplot.savefig("/home/nagbansi/Pictures/Enron Outliers.png")
