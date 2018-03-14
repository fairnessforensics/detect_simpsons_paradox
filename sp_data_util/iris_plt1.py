# this is the original figure code used in the paper, the more concise
# version in the notebooks was preferred for documentation
fig = plt.figure()
font = {'weight':'normal'}
plt.rc('font', **font)
colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
markers = {'Iris-setosa':'x', 'Iris-versicolor':'o', 'Iris-virginica':'s'}

for i in range(len(iris_df['sepal length'])):
    plt.scatter(iris_df['sepal length'][i], iris_df['sepal width'][i],c=colors[iris_df['class'][i]], marker=markers[iris_df['class'][i]], label=iris_df['class'][i])


plt.xlabel('sepal length',  fontsize=24)
plt.ylabel('sepal width', fontsize=24)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

import matplotlib.patches as mpatches
from collections import OrderedDict
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), prop={'size':15})

# Add correlation line
axes = plt.gca()
x = iris_df['sepal length']
y = iris_df['sepal width']

m, b = np.polyfit(x, y, 1)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '--',color='black')

setosa = iris_df[iris_df['class'] =='Iris-setosa']
versicolor = iris_df[iris_df['class'] =='Iris-versicolor']
virginica = iris_df[iris_df['class'] =='Iris-virginica']
x1 = setosa['sepal length']
y1 = setosa['sepal width']

m1, b1 = np.polyfit(x1, y1, 1)
X_plot1 = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1]-2,100)
plt.plot(X_plot1, m1*X_plot1 + b1, '-', color='red')

x2 = versicolor['sepal length']
y2 = versicolor['sepal width']

m, b = np.polyfit(x2, y2, 1)
X_plot = np.linspace(axes.get_xlim()[0]+0.5,axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '-', color='blue')

x3 = virginica['sepal length']
y3 = virginica['sepal width']

m, b = np.polyfit(x3, y3, 1)
X_plot = np.linspace(axes.get_xlim()[0]+0.5,axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '-', color='green')

plt.show()
