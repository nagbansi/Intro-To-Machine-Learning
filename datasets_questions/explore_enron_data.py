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
poiCount = 0;
for person in enron_data:
    if enron_data[person]["poi"]==1:
        poiCount = poiCount +1
print "No of POIs in E+F dataset: ", poiCount


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


#who took home the most money (largest value of "total_payments" feature)?
print "Kenneth Lay total_payments: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Jeffrey Skilling total_payments: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Andrew Fastow total_payments: ", enron_data["FASTOW ANDREW S"]["total_payments"]


#How is it denoted when a feature doesn't have a well-defined value?
# Ans: 'NaN'


#How many folks in this dataset have a quantified salary?
quantified_salary = 0
email_addr = 0
for folk in enron_data:
    if enron_data[folk]["salary"] != 'NaN' or enron_data[folk]["salary"] > 0:
        quantified_salary = quantified_salary + 1
    if enron_data[folk]["email_address"] != 'NaN':
        email_addr = email_addr + 1
print "Folks with quantified salary: ", quantified_salary
print "Folks with known email address: ", email_addr


#How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments?
#What percentage of people in the dataset as a whole is this?
countOfNaNPayments = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == 'NaN':
        countOfNaNPayments = countOfNaNPayments + 1
print "No of people have 'NaN' for their total payments: ", countOfNaNPayments
print "Percentage of people have 'NaN' for their total payments: ", (float(countOfNaNPayments)/(len(enron_data))) * 100


#How many POIs in the E+F dataset have "NaN" for their total payments?
#What percentage of POI's as a whole is this?
count = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == 'NaN' and enron_data[person]["poi"] == True:
        count = count + 1
print "No of poi have 'NaN' for their total payments: ", count
print "Percentage of poi have 'NaN' for their total payments: ", (float(count)/poiCount) * 100 #poiCount: Total no of POI 

#If a machine learning algorithm were to use total_payments as a feature, 
#would you expect it to associate a "NaN" value with POIs or non-POIs?
#Ans: With non-POIs


#What is the new number of people of the dataset?
#Ans:   len(enron_data) + new 
#       = 146 + 10
#       += 156

#What is the new number of folks with "NaN" for total payments?
#Ans:   Old(countOfNaNPayments) + new 
#       = 21 + 10
#       = 31


#What is the new number of POI's in the dataset? 
#Ans:   poiCount + new 
#       = 35 + 10 
#       = 45


#What is the new number of POI's with NaN for total_payments?
#Ans:   count + new
#       = 0 + 10
#       = 10


#Once the new data points are added, do you think a supervised classification 
#algorithm might interpret "NaN" for total_payments as a clue that someone is a POI?
#Ans: Yes
