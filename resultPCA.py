#	Author:	Hayatullah Ibrahimy
#	Date:	Jun 23, 2017
#	Berlin, Germany
#	Prancipal Component Analysis

from sklearn.decomposition import PCA
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt2
from scipy import stats
import math
#------------------------------------
df	=	pd.read_csv(
	filepath_or_buffer='newMatrixFinal',
	header=None,
	sep=',')

df.columns=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

df.dropna(how="all", inplace=True)		#	drops the empty line at file-end

X	=	df.ix[:,0:].values			#	The Whole Matrix
Y	=	df.ix[:,0:].values

#-------------------------------------------------
print ('-----------Original Data------------')
print (df)			#	Original Data
print ('-----------The Matrix---------------')
print (X)			#	The Matrix
#print y			#	Copy of Matrix
#------------------------PCA-------------------------------------------
pca	=	PCA(	n_components	=	2	)
pca.fit(X)
rows = str(len(X))
TitleMSG =  rows + 'x292' + ' Matrix'
print ('----------PCA Explained Variance Ratio--------------')
#print pca.explained_variance_ratio_

firstComp	=	pca.components_[0]
secondComp	=	pca.components_[1]
#print firstComp
#print secondComp
transformedData = pca.fit_transform(X)
print ('--------------Transformed Data----------------------')
print (transformedData)

print ('--------------Variance of PCA----------------------')
print (pca.explained_variance_ratio_)

ax = plt.subplot(111)

print(transformedData[0])
for i,j in zip(transformedData, X):

    ax1	=	plt.scatter(	firstComp[0]*i[0],	firstComp[1]*i[0],	c='r')	# Print out the PCA 1 line
    ax2	=	plt.scatter(	secondComp[0]*i[0],	secondComp[1]*i[0], c='b')	# Print out the PCA 2 line
    ax3	=	plt.scatter(	j[0],	j[1], c='g')						# Print Out the Original Data


ax.legend((ax1,ax2,ax3), ('PCA 1','PCA 2','Original Data'),loc=4)
plt.xlabel("SEHI1")
plt.ylabel("SEHI2")
plt.title("PCA Output of " + TitleMSG)
plt.axis('equal')
plt.show()

# ------------------------Dis from dots to PCA1-------------------------------------------
# use p1,p2 to get the line of PCA1
p1 = (transformedData[0][0]*firstComp[0], transformedData[0][1]*firstComp[1])
p2 = (transformedData[1][0]*firstComp[0], transformedData[1][1]*firstComp[1])
p3 = (X[0][0],X[0][1])


# Calculate the distance from each point to the PCA1
# d = linalg.norm(np.cross(p2-p1, p1-p3))/linalg.norm(p2-p1)
def distance_to_line(p1,p2,p3):
    diff_x = p2[0] - p1[0]
    diff_y = p2[1] - p1[1]
    num = abs(diff_y*p3[0] - diff_x*p3[1] + p2[0]*p1[1] - p2[1]*p1[0])
    den = math.sqrt(diff_y**2 + diff_x**2)
    return num/den

list_dis = []
num_points =  X.shape[1]

for p3 in X:
    i = 0
    dis = distance_to_line(p1,p2,p3)
    list_dis.append(dis)

fig, ax = plt.subplots()

# the number of databin to show
num_bins = 100
# the histogram of the data
n, bins, patches = ax.hist(list_dis, num_bins, normed=1)

ax.set_xlabel('Distance from original data points to PCA1')
ax.set_ylabel('Probability density')
plt.title("Histogram for distance from original data to PCA1  ")


# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()