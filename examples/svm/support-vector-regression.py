#Support Vector Regression (SVR) using linear and non-linear kernels
import matplotlib
print matplotlib.__version__
#matplotlib.use('GTK')
matplotlib.use("Agg")
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

#Generate Sample data
x = np.sort(5 * np.random.rand(40, 1), axis = 0)
y = np.sin(x).ravel()

#Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))

#create classifier regression model
svr_rbf = SVR(kernel="rbf", C=1000, gamma=0.1)
svr_lin = SVR(kernel="linear", C=1000, gamma=0.1)
svr_poly = SVR(kernel="poly", C=1000, gamma=0.1)

#Fit regression model
y_rbf = svr_rbf.fit(x,y).predict(x)
y_lin = svr_lin.fit(x,y).predict(x)
y_poly = svr_poly.fit(x,y).predict(x)

#Plotting of results
lw = 2
plt.scatter(x, y, color="darkorange", label="data")
plt.plot(x, y_rbf, color="navy", lw=lw, label="RBF Model")
plt.plot(x, y_lin, color="c", lw=lw, label="Linear Model")
plt.plot(x, y_poly, color="cornflowerblue", lw=lw, label="Polynomial Model")
plt.xlabel("data")
plt.ylabel("target")
plt.title("Support Vector Regression")
plt.legend()
plt.show()
plt.savefig("/home/nagbansi/s.png")
