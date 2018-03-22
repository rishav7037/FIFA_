import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
dataset = pd.read_csv('FullData.csv')
x = len(dataset)
print(x)
stat=dataset.describe().transpose()
print(stat)
s75=stat['75%']
Bl=s75['Ball_Control']
Sp=s75['Shot_Power']
Ac=s75['Acceleration']
vs=s75['Finishing']
cr=s75['Penalties']
sp=s75['Speed']
ls=s75['Long_Shots']
final=dataset.loc[(dataset['Ball_Control'] > Bl) & (dataset['Shot_Power'] > Sp) & (dataset['Acceleration'] >Ac ) & (dataset['Finishing'] > vs) & (dataset['Penalties'] > cr) & (dataset['Speed'] > sp) & (dataset['Long_Shots'] > ls), ["Name","Ball_Control","Shot_Power","Acceleration","Finishing","Penalties","Speed","Long_Shots"]]
fl=len(final)
finaly=final.loc[:fl]
fy=len(finaly)
print(fy)
data2=[]
ball_control=final['Ball_Control'].tolist()
shot_power=final['Shot_Power'].tolist()
acc=final['Acceleration'].tolist()
vis=final['Finishing'].tolist()
cro=final['Penalties'].tolist()
sped=final['Speed'].tolist()
los=final['Long_Shots'].tolist()
nm=final['Name'].tolist()

i=0
while i<fl:
    sum=ball_control[i]+shot_power[i]+acc[i]+vis[i]+cro[i]+sped[i]+los[i]
    sum=sum/7
    data2.insert(i,sum)
    i=i+1

rl=len(data2)

rl=len(data2)
md=mean(data2)
md=md+2
print(md)
dataf2=[]
dataf3=[]
i=0
while i<rl:
    if data2[i] > md:
        dataf2.insert(i,data2[i])
        dataf3.insert(i,nm[i])
        
    i=i+1

rl1=len(dataf2)
m1=len(dataf3)
print(m1)
print(dataf3[0])

r=list(range(rl1))
plt.title("Best Goal Scorrer")
plt.xticks(range(rl1),dataf3,rotation='vertical',fontsize=5.4)
plt.plot(r,dataf2,color='red')
plt.scatter(r,dataf2)

#plt.bar(r,dataf2)
plt.show()
