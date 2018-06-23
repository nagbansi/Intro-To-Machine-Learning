#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

#pickle.load returns a dict
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#How many data points (people) are in the dataset?
print "No of data points: ", len(enron_data)


#For each person, how many features are available?
print "Available features for each person: ", len(enron_data.values()[0])


#How many POI's are there in the E+F dataset?
count = 0;
for person in enron_data:
    if enron_data[person]["poi"]==1:
        count = count +1
print "No of POIs in E+F dataset: ", count


#How many POI's were there total?
f = open("../final_project/poi_names.txt", 'r')
poi = f.readlines()
print"Total no of POIs: ", len(poi[2:])
f.close()


#What is the total value of the stock belonging to James Prentice?
print "Total value of the stock belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]


#How many email messages do we have from Wesley Colwell to persons of interest?
print "No. of email messages from Wesley Colwell to persons of interest: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]


#What is the value of stock options exercised by Jeffrey K Skilling?
print "Value of stock options exercised by Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
