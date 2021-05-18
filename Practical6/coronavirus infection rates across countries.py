# input a table
import pandas as pd
import matplotlib.pyplot as plt
USA=29862124
India=11285561
Brazil=11205972
Russia=4360823
UK=4234924

# create a pie chart
labels= ['USA', 'India', 'Brazil', 'Russia', 'UK']
sizes= [29862124, 11285561, 11205972, 4360823, 4234924]
colors=['red', 'yellow', 'blue', 'green', 'pink']
explode = (0, 0.1, 0, 0, 0)
plt.axis('equal')

#specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',
shadow=False, labeldistance=1.1,startangle=90, pctdistance=0.6)

# Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
