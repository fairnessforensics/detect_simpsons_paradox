# this is the original figure code used in the paper, the more concise
# version in the notebooks was preferred for documentation
fig = plt.figure()
colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
markers = {'Iris-setosa':'x', 'Iris-versicolor':'o', 'Iris-virginica':'s'}

for i in range(len(iris_df['sepal width'])):
    test = plt.scatter(iris_df['sepal width'][i], iris_df['petal width'][i],
                       c=colors[iris_df['class'][i]], 
                       marker=markers[iris_df['class'][i]], label=iris_df['class'][i])

plt.xlabel('sepal width',  fontsize=24)
plt.ylabel('petal width', fontsize=24)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

from collections import OrderedDict
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), prop={'size':15})

# Add correlation line
axes = plt.gca()
x = iris_df['sepal width']
y = iris_df['petal width']

m, b = np.polyfit(x, y, 1)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '--',color='black')

setosa = iris_df[iris_df['class'] =='Iris-setosa']
versicolor = iris_df[iris_df['class'] =='Iris-versicolor']
virginica = iris_df[iris_df['class'] =='Iris-virginica']
x1 = setosa['sepal width']
y1 = setosa['petal width']

m1, b1 = np.polyfit(x1, y1, 1)
X_plot1 = np.linspace(2,4.5,100)
plt.plot(X_plot1, m1*X_plot1 + b1, '-', color='red')

x2 = versicolor['sepal width']
y2 = versicolor['petal width']

m, b = np.polyfit(x2, y2, 1)

X_plot = np.linspace(1.9,3.5,100)
plt.plot(X_plot, m*X_plot + b, '-', color='blue')

x3 = virginica['sepal width']
y3 = virginica['petal width']

m, b = np.polyfit(x3, y3, 1)
X_plot = np.linspace(2,4,100)
plt.plot(X_plot, m*X_plot + b, '-', color='green')

plt.show()
