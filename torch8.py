import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
names =['sepal-length', 'sepal-width','petal-length','petal-width,]

dataset = pd.read_csv('iris.data',names=names)

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (x,y,test_size=0.20)

from sklearn.preprocessing import StandardScaler
s = StandardScaler()
x_train =s.transfrom(x_train)
x_test =s.transfrom(x_test)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(x_train, y_train)

from sklearn.metrics import accuracy_score
y_pred = knn.predict(x_test)
print("정확도:{}".format(accuracy_score(y_test, y_pred)))

k=10
acc_array=np.zeros(k)
for k in np.arange(1,k+1,1):
     classifier =KNeighborsClassifier(n_neighbors=k).fit(x_train, y_train)
     y_pred = classifier.predict(x_test)
     acc = metrics.accuracy_score(y_test, y_pred)
     acc_array[k-1] = acc

max_acc = np.amax(acc_array)
acc_list = list(acc_array)
k = acc_list.index(max_acc)
print("정확도", max_acc, "으로 최적의 k는",k+1,"입니다.")

        