# -*- coding:utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
import numpy as np

np.set_printoptions(threshold='nan', linewidth=10000)  # 全部输出

train_data = np.loadtxt('data.csv', dtype=float, comments=',')
data = train_data[:, 1:]   # 训练数据集的X值
# print data
label = train_data[:, 0]   # 训练数据集的Y值（标签）
# print label
clf = RandomForestClassifier(n_estimators=80)   # 用随机森林方法进行分类
clf = clf.fit(data, label)

test_data = np.loadtxt('data1.csv', dtype=float, comments=',')
test_x = test_data[:, 1:]   # 测试数据集
result = []
for i in range(len(test_x)):
    ret = int(clf.predict(test_x[i])[0])
    result.append(ret)

for j in range(0, len(result), 3):
    if result[j+1] == -1:
        print result[j] + result[j+2]
    if result[j+1] == -2:
        print result[j] * result[j+2]

