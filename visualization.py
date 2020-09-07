import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:...') #movies.csv location
data = data[(data.genre == 'Comedy') | (data.genre == 'Action') |(data.genre == 'Animation')|(data.genre == 'Crime')|(data.genre == 'Drama')] 
data = data[(data.budget >= 50000000) & (data.year <=2016) & (data.year >= 1995)]
data = data[(data.company == 'Paramount Pictures') | (data.company =='Warner Bros.') | (data.company =='Twentieth Century Fox Film Corporation') | (data.company =='Universal Pictures') | (data.company =='Walt Disney Pictures')]

data['company'] = data['company'].astype('category') #converting the categorical "company" attribute to a numerical variable.
cat_columns = data.select_dtypes(['category']).columns
data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)

fig = plt.figure(figsize=(15, 8))
t = fig.suptitle('Budget - Gross - Company - Genre(Color)', fontsize =14)
ax = fig.add_subplot(111, projection='3d')

dict = {'Comedy': 'red', 'Action': 'green', 'Crime': 'blue', 'Drama': 'purple', 'Animation': 'yellow'} 
xs = list(data['budget'])
ys = list(data['gross'])
zs = list(data['company'])
data_points = [(x,y,z) for x, y, z in zip(xs, ys, zs)]


colors = [dict[i] for i in list(data['genre'])]

for data, color in zip(data_points, colors):
    x, y, z = data
    ax.scatter(x, y, z, alpha=0.6, c = color, edgecolors = 'none', s=80)
    
ax.set_xlabel('budget')
ax.set_ylabel('gross')
ax.set_zlabel('company')
plt.show()
