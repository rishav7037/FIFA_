import pandas as pd
import collections as c
import matplotlib.pyplot as plt
#import numpy as np

df=pd.read_csv('C:\\Users\\hp\\Downloads\\fulldata.csv')
club_ana = df[['Club','Skill_Moves','Ball_Control','Dribbling','Marking',
	'Sliding_Tackle','Standing_Tackle','Aggression','Reactions','Attacking_Position','Interceptions',	'Vision',
	'Composure','Crossing','Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance',
	'Agility','Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
	'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes']]
mean = club_ana.groupby('Club').mean()

max_mean = mean.max( axis = 1 )
attribute = mean.idxmax( axis = 1 )
counter = c.Counter(attribute)
distance = [0,1,2,3,4,5,6,7]
X=['Acceleration','Agility','Balance','Jumping','Reactions','Speed','Stamina','Strength']
Y=[98, 12, 72, 91, 54, 114, 28, 165]

f1=plt.figure(6)
p1 = plt.bar(range(8), Y, 0.5,color='green')
plt.xlabel("Attributes")
plt.ylabel("No. of club")
plt.xticks(distance, X,rotation=90)
plt.title('Attribute by club')
f1.show()

