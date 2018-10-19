import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import dates

# Read the data file and print the column headings
print ''
Woodshop = pd.read_csv("11-Woodshop-20181016.csv")
Woodshop = Woodshop.rename(columns = {' PM25': 'Woodshop PM25',' Co2': 'Woodshop CO2'})
print Woodshop.columns

# delete unwanted columns
print ''
dropList = ['Timestamp', ' PM10', ' Temperature', ' Relative Humidity', ' O3', ' ID', ' Monitor ID']
Woodshop = Woodshop.drop(dropList, axis=1)
print Woodshop.head(5)

# change index to datetime version of ' Local Timestamp' column 
print ''
Woodshop['Date'] = pd.to_datetime(Woodshop[' Local Timestamp'],format='%m/%d/%y %H:%M')
Woodshop = Woodshop.drop(' Local Timestamp', axis=1)
Woodshop = Woodshop.set_index('Date')
print Woodshop.head(5)

# Group by hour and show mean of each group
print ''
next = Woodshop.groupby(Woodshop.index.hour).mean()
print next.head(24)

print ''
