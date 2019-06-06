import ijson
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np


time = []
with open("IBM_Cloudant_DB_Stand_09_04_2019_10_15.json", "r") as read_it:
	data = ijson.items(read_it, 'rows.item.doc.payload.d')
	columns = list(data)
	nodeid = [col["NodeID"] for col in columns]
	entfernung = [col["Entfernung"] for col in columns]
	fuellstand = [col["Fuellstand"] for col in columns]
	batterie = [col["Batterie"] for col in columns]
	batteriefuel = [col["BatterieFuel"] for col in columns]
	rssi = [col["RSSI"] for col in columns]
	state = [col["State"] for col in columns]
	open = [col["Open"] for col in columns]
	timestamp = [col["Timestamp"] for col in columns]
	for i in range(len(timestamp)):
		time.append(pd.Timestamp(timestamp[i]))
my_dict = {'timestamp': time, 'nodeid': nodeid, 'entfernung': entfernung,'fuellstand': fuellstand, 'batterie': batterie, 'batteriefuel':batteriefuel, 'rssi': rssi, 'state':state, 'open':open}
stand_df = pd.DataFrame(my_dict)
df = stand_df.convert_objects(convert_numeric= True)
plt.hist(nodeid)
#plt.plot(fuellstand)
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
print(df.describe(include= 'all'))
np.savetxt('describe.out', df.corr(method='pearson', min_periods= 1),  delimiter=',', fmt='%s', newline='\n')
print(df.corr(method='pearson', min_periods= 1))
plt.show()



