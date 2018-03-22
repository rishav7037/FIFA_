import pandas as pd
df=pd.read_csv('C:\\Users\\hp\\Downloads\\fulldata.csv')
x=df['Nationality'].tolist()
y=set(x)
attributes=['Skill_Moves','Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle',
'Aggression','Reactions','Attacking_Position','Interceptions','Vision','Composure','Crossing',
'Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance','Agility',
'Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes']
continent_a=df[['Nationality','Skill_Moves','Ball_Control','Dribbling','Marking','Sliding_Tackle','Standing_Tackle',
'Aggression','Reactions','Attacking_Position','Interceptions','Vision','Composure','Crossing',
'Short_Pass','Long_Pass','Acceleration','Speed','Stamina','Strength','Balance','Agility',
'Jumping','Heading','Shot_Power','Finishing','Long_Shots','Curve','Freekick_Accuracy','Penalties',
'Volleys','GK_Positioning','GK_Diving','GK_Kicking','GK_Handling','GK_Reflexes']]

Africa = ['Algeria','Guinea Bissau','São Tomé & Príncipe','Guinea Bissau ','DR Congo','Central African Rep.','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Comoros','Congo','Congo Democratic Republic of','Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea-Bissau','Ivory Coast','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe','Burkina Faso']
Asia = ['Afghanistan','China PR','Korea Republic','Palestine','Korea DPR','Timor-Leste','Chinese Taipei','Bahrain','Armenia','Bangladesh','Azerbaijan','Bhutan','Brunei','Burma (Myanmar)','Cambodia','China','East Timor','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Georgia','Kazakhstan','North Korea','South Korea','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Nepal','Oman','Pakistan','Philippines','Qatar','Russian Federation','Saudi Arabia','Singapore','Sri Lanka','Syria','Tajikistan','Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen']
Europe = ['Albania','FYR Macedonia','Faroe Islands','Serbia','Gibraltar','Kosovo','Bosnia Herzegovina','Andorra','Scotland','Austria','Belarus','Belgium','Bosnia and Herzegovina','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Republic of Ireland','Italy','Latvia','Liechtenstein','Northern Ireland','Lithuania','Luxembourg','Macedonia','Malta','Moldova','Monaco','Montenegro','Netherlands','Norway','Poland','Portugal','Romania','Russia','San Marino','Serbi','Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','England','Vatican City','Republic of Ireland','Wales']
North_America = ['Antigua and Barbuda','Puerto Rico','St Lucia','Antigua & Barbuda','Montserrat','Bermuda','St Kitts Nevis','Bahamas','Barbados','Belize','Canada','Costa Rica','Cuba','Dominica','Dominican Republic','El Salvador','Grenada','Guatemala','Haiti','Honduras','Jamaica','Mexico','Nicaragua','Panama','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Trinidad and Tobago','United States']
Australia = ['Australia','FIFA16_NationName_215','Guam','Fiji','Kiribati','Marshall Islands','Micronesia','Nauru','New Zealand','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
South_America =['Argentina','Curacao','Trinidad & Tobago','Aruba','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela']

g=df.groupby('Nationality')
continent=[]
i=0
while i<17588:
    if x[i] in Asia:
        continent.insert(i,'Asia')
    elif x[i] in Africa:
        continent.insert(i,'Africa')
    elif x[i] in North_America:
        continent.insert(i,'North_America')
    elif x[i] in South_America:
        continent.insert(i,'South_America')
    elif x[i] in Europe:
        continent.insert(i,'Europe')
    elif x[i] in Australia:
        continent.insert(i,'Australia')
    i=i+1

asian_player = pd.DataFrame()
for row in range(6):
     asian_player = asian_player.append(continent_a.loc[continent_a['Nationality'] == 'Asia' ])

Europe_player = pd.DataFrame()
for row in range(33):
     Europe_player = Europe_player.append(continent_a.loc[continent_a['Nationality'] == Europe[row] ])

SA_player = pd.DataFrame()
for row in range(13):
     SA_player = SA_player.append(continent_a.loc[continent_a['Nationality'] == South_America[row] ])

NA_player = pd.DataFrame()
for row in range(11):
     NA_player = NA_player.append(continent_a.loc[continent_a['Nationality'] == North_America[row] ])

AF_player = pd.DataFrame()
for row in range(17):
     AF_player = AF_player.append(continent_a.loc[continent_a['Nationality'] == Africa[row] ])
     
A_player = continent_a.loc[continent_a['Nationality'] == 'Australia' ]
Avg = {}
for a in range(35):
    Avg[a] = Europe_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('Europe players are expert in = ',attributes[k[v.index(max(v))]])

Avg = {}
for a in range(35):
    Avg[a] = asian_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('Asian player are expert in = ',attributes[k[v.index(max(v))]])

Avg = {}
for a in range(35):
    Avg[a] = SA_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('South Africa player are expert in = ',attributes[k[v.index(max(v))]])

Avg = {}
for a in range(35):
    Avg[a] = NA_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('North America player are expert in = ',attributes[k[v.index(max(v))]])

Avg = {}
for a in range(35):
    Avg[a] = AF_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('AFrica player are expert in = ',attributes[k[v.index(max(v))]])

Avg = {}
for a in range(35):
    Avg[a] = A_player[attributes[a]].mean()
v=list(Avg.values())
k=list(Avg.keys())
print('\033[1m''Austrailan player are expert in = ',attributes[k[v.index(max(v))]])