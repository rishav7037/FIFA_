import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\Users\\hp\\Downloads\\fulldata.csv')
cols = ['Name','Club_Joining','Contract_Expiry','Club', 'Rating', 'Age','Nationality']
player_data = df[cols]

contract= player_data.iloc[:,1]
contract.dropna(how='any',axis=0,inplace = True)
period = player_data.iloc[:,2]
period.dropna(how='any',axis=0,inplace = True)
print()
avg=period.mean()
print('Average contract period of each player',avg,'years')
print()
m=max(period)
print("Longest contract period : ",m)
print()
period_low= player_data.iloc[:,3]
ma=min(period_low)
print('Smallest contract period',ma)
df['Club_Joining'].fillna(value='02/10/17',inplace=True)
df['Contract_Expiry'].fillna(value='2019',inplace=True)
list2=(pd.DatetimeIndex(df['Club_Joining']).year.astype(int)).tolist()
list1=df['Contract_Expiry'].tolist()
z=[]
i=0
while i<17588:
    list2[i]=float(list2[i])
    list2[i]=float(list1[i])-float(list2[i])
    z.insert(i,list2[i])
    i=i+1

bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#total = [0.3,1.3,2.3,3.3,4.3,5.3,6.3,7.3]
x=plt.hist(z,bins,histtype='bar',rwidth=0.9)
plt.xlabel('total contract period years')
plt.ylabel('no of players')
plt.xticks(bins,rotation=90)
plt.title('contract period')

plt.show()