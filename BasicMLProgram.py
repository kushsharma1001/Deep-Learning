import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:\\Users\\ksharma\\Downloads\\LEARN\\Deep Learning by Rohan Inkers\\Basic program univariate dataset training\\train.csv') #import CSV training dataset into dataframe

print('Training Dataset loaded into Dataframe : ')
print(df.head()) # print dataframe
print(df.shape) # size of training dataframe
clean_df = df.dropna() # clean dataframe

print('Cleaning on Dataframe completed : ')
print(clean_df.head()) #print clean dataframe now
print('Clean Dataframe size is :')
print(clean_df.shape) # size of clean dataframe i.e. without NA, Duplicates etc...

x_train = clean_df['x'].reshape(-1,1)
y_train = clean_df['y']

print ("Mean of X Training set: ", np.mean(x_train), "\n")
print ("Median of X Training set: ", np.median(x_train), "\n")
print ("Mean of Y Training set: ", np.mean(y_train), "\n")
print ("Median of Y Training set: ", np.median(y_train), "\n")
print ("Std Dev of X Training set: ", np.std(x_train), "\n")
print ("Std Dev of Y Training set: ", np.std(y_train), "\n")

#Median and mean are similar so the training set isn't skewed by any outliers that might cause leverage when doing the linear regression

# So, Now let's plot some of the data
plt.title('Relationship between X and Y')
plt.scatter(x_train, y_train,  color='black')
plt.show()

# Use subplot to have graphs side by side
plt.subplot(1, 2, 1)
plt.title('X training set')
plt.hist(x_train)

plt.subplot(1, 2, 2)
plt.title('Y training set')
plt.hist(y_train)
plt.show()

plt.subplot(1, 2, 1)
plt.title('X training set')
plt.boxplot(x_train)

plt.subplot(1, 2, 2)
plt.title('Y training set')
plt.boxplot(y_train)
plt.show()

lm = LinearRegression()

lm.fit(x_train, y_train) #training linear regression model using clean dataframe

df2 = pd.read_csv('C:\\Users\\ksharma\\Downloads\\LEARN\\Deep Learning by Rohan Inkers\\Basic program univariate dataset training\\test.csv') #import CSV testing dataset into dataframe

print('Testing Dataset loaded into Dataframe : ')
print(df2.head()) # print dataframe
print(df2.shape) # size of test dataframe
clean_df2 = df2.dropna() # clean test dataframe
print('Cleaning on Test Dataframe completed : ')
print(clean_df2.head()) #print clean dataframe now
print('Clean Dataframe size is :')
print(clean_df2.shape) # size of clean dataframe i.e. without NA, Duplicates etc...

x_test = clean_df2['x'].reshape(-1,1)
y_test = clean_df2['y']

y_predicted = lm.predict(x_test)

print(y_predicted)

plt.title('Comparison of Y values in test and the Predicted values')
plt.ylabel('Test Set')
plt.xlabel('Predicted values')
plt.scatter(y_predicted, y_test,  color='black')
plt.show()
