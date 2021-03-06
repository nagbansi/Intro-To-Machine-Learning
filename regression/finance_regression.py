#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    

import matplotlib
matplotlib.use('agg')
import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
#features_list = ["bonus", "long_term_incentive"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

from sklearn.linear_model import LinearRegression
#Create regression
reg = LinearRegression()
#fit regression
reg.fit(feature_train, target_train)
print "Prediction: ", reg.predict(feature_test)

#What are the slope and intercept?
print "Coef: ", reg.coef_
print "Intercept: ", reg.intercept_

#What's that score on the testing data?
print"\n######## stats on test dataset #########"
print "r-squared score: ", reg.score(feature_test, target_test)

#What's that score on the training data?
print"\n######## stats on training dataset #########"
print "r-squared score: ", reg.score(feature_train, target_train)

#What target are you trying to predict?
# Ans: bonus


#What is the input feature being used to predict it?
# Ans: salary 


#f you made the mistake of only assessing on the training data, 
#would you overestimate or underestimate the performance of your regression?
# Ans: overestimate, because we wont be knowing that there is over fitting happening.


#If you had to predict someone's bonus and you could only have one piece of information about them, 
#would you rather know their salary or the long term incentive that they received?
# Ans: long term incentive


### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass


#Now we'll be drawing two regression lines, one fit on the test data (with outlier) and one fit on the training data (no outlier).
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b")

#What's the slope of the new regression line?
print "\nSlope/Intercept of the new regression line"
print "Coef: ", reg.coef_
print "Intercept: ", reg.intercept_


plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
plt.savefig("/home/nagbansi/Pictures/plot.png")
