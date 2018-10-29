from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
get_ipython().run_line_magic('matplotlib', 'inline')
digits = load_digits()


# # Determining the Total number of imgaes and labels

print("Image data shape", digits.data.shape)
print("Target data shape", digits.target.shape)


# # Displaying some of the imgaes and labels

plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5],digits.target[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (8,8)), cmap = plt.cm.pink)
    plt.title('Training: %i\n' % label, fontsize = 20)


# # Deviding datasets into training and test set

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size= 0.23, random_state = 2)
print(x_train.shape)

print(y_train.shape)

print(x_test.shape)

print(y_test.shape)


# # Making an instance of the model and training it

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)


# # Predicting the output of the first elment of the test set

print(logisticRegr.predict(x_test[0].reshape(1, -1)))


# # Predicting the output of the forst 10 elements of the test set

print(logisticRegr.predict(x_test[0:10]))


# # Predicting for entire dataset

predictions = logisticRegr.predict(x_test)


# # Determining the accuracy of the model

score = logisticRegr.score(x_test, y_test)
print(score)


# # Representing the confusion matrics in a heatmap

cm = metrics.confusion_matrix(y_test, predictions)
print(cm)
plt.figure(figsize = (9,9))
sns.heatmap(cm, annot = True, fmt = ".3f", linewidths = .5, square = True, cmap = 'Blues_r')
plt.ylabel('Actual lable')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 15)


index = 0
misclassifiedIndex = []
for predict, actual in zip(predictions, y_test):
    if predict == actual:
        misclassifiedIndex.append(index)
        index += 1
plt.figure(figsize=(20,3))
for plotIndex, wrong in enumerate(misclassifiedIndex[0:4]):
    plt.subplot(1, 4, plotIndex + 1)
    plt.imshow(np.reshape(x_test[wrong], (8,8)), plt.cm.gray)
    plt.title("predicted: {}, actual: {}" .format(predictions[wrong], y_test[wrong]), fontsize=20)
    

