# captcha_show160

##	降噪
1.	去掉背景色、噪声色 
2.	降噪结果：噪声、背景 为0的矩阵
##	训练集数据
1.	Label：加法 -> -1, 乘法 -> -2, 数据 
2.	Data：一维0，1矩阵
##	分类器
使用sklearn的  RandomForestClassifier
##	测试 : 
识别率 90% 以上	
##	版本
1.	python 2.7
2.	scikit-learn (0.18.1)


