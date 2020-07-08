import pandas as pd

data=pd.read_csv(r'C:\Users\ansar\Desktop\Machine Learning/bottle.csv')
#print(data)

# dataframe.size 
#size = data.size 
  
# dataframe.shape 
#shape = data.shape 

# printing size and shape 
#print("Size = {}\nShape ={}\nShape[0] x Shape[1] = {}". 
#format(size, shape, shape[0]*shape[1])) 

#Identify Null values in data
#null_columns=data.columns[data.isnull().any()]
#data[null_columns].isnull().sum()


#print(data[data.isnull().any(axis=1)][null_columns].head())

#print(data.columns[data.isnull().any()])
column_with_nan = data.columns[data.isnull().any()]
for column in column_with_nan:
     if data[column].isnull().sum()*100.0/data_shape[0] > 0:
             data.drop(column,1, inplace=True)
print(data.index[data.isnull().any(axis=1)])