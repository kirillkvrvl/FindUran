import pandas as pd
kodlist=[]
data = pd.read_csv('https://raw.githubusercontent.com/infoculture/opencustoms/master/data/tnved.csv', encoding='utf-8', header=1)
for index, row in data.iterrows():
    if 'УРАН' in row['SIMPLE_NAM']:
        kodlist.append(row['KOD'])
kodlist.remove('293211')
kodlist.remove('29321100')
kodlist.remove('2932110000')
kodlist.remove('293219')
kodlist.remove('29321900')
kodlist.remove('2932190000')
kodlist.remove('2932201000')
kodlist.remove('29322010')
print(kodlist)
