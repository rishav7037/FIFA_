import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('FullData.csv')
df2=df[['Aggression','Reactions','Composure']]
x=df2.describe().transpose()
print(x)
A75=x['75%']
AG=A75['Aggression']
RE=A75['Reactions']
CP=A75['Composure']
final=df.loc[(df['Aggression'] > AG) & (df['Reactions'] > RE) & (df['Composure'] > CP),['Name','Aggression','Reactions','Composure']]
fl=len(final)
print(fl)
finaly=final.loc[:fl]
print(final)
fy=len(finaly)
final4=final['Name'].tolist()
print(fy)
A50=x['50%']
AG2=A50['Aggression']
RE2=A50['Reactions']
CP2=A50['Composure']
final2=df.loc[(df['Aggression'] > AG2)&( df['Aggression'] < AG  ) & (df['Reactions'] > RE2) &(df['Reactions'] < RE)&(df['Composure'] < CP)&(df['Composure'] > CP2),['Name','Aggression','Reactions','Composure']]
print(final2)
final3=df.loc[(df['Aggression'] < AG2) & (df['Reactions'] < RE2),['Name','Aggression','Reactions']]
print(final3)
agr=final['Aggression'].tolist()
rec=final['Reactions'].tolist()
com=final['Composure'].tolist()
ln=len(final)
r=range(0,100)
data=[]
dataf3=[]
i=0
while i<100:
    sum=agr[i]+rec[i]+com[i]
    sum=sum/2
    data.insert(i,sum)
    dataf3.insert(i,final4[i])   
    i=i+1
    
#plt.scatter(r,data)
#fig, ax = plt.subplots()
#ax.scatter(r, data)
plt.xticks(range(0,100),dataf3,rotation='vertical',fontsize=5.4)
plt.plot(r,data)
plt.scatter(r,data,color='red')
plt.title('Percentage of field behaviour')
plt.xlabel('Players')
plt.ylabel('Percentage')

plt.show()
