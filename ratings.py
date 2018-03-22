import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('C:\\Users\\hp\\Downloads\\fulldata.csv')
df2=df[['Rating','Nationality']]
print(df2.isnull().any().any())
print(df2.describe())
n1=np.array(df2.groupby('Nationality'))
mean= np.array(df2.groupby('Nationality').mean())
final=df.loc[(df2['Ratings'] >=mean)]
distance = [0,1,2,3,4,5,6,7]
f1=plt.figure(6)
p1 = plt.hist(mean)
plt.xlabel("Ratings")
plt.ylabel("No. of club")
plt.xticks(distance, mean,rotation=90)
plt.title('Attribute by club')
f1.show()
#mean.plot(kind='line')
