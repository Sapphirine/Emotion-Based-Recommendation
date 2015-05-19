__author__ = 'Siyuan'
from sklearn.cluster import KMeans
from matplotlib import pyplot
import numpy as np

k = 10
data1 = []
data2 = []
name1 = []
name2 = []
point1 = []
point2 = []
users = []
scores = []

dim1 = open("output.txt", 'r')  #  the file of the result of emotion quantification in 1 or 2 dimension
dim2 = open("newoutput.txt", 'r')
twitter = open("twitter.txt", 'r')
flag = 0
for line in dim2: # read the result of business names and scores 2 dimension
    if(flag == 0):
        line = line[1:-2]
        sp = line.split(",")
        pointx = float(sp[0])
        pointy = float(sp[1])
        coords = [pointx,pointy]
        flag = 1
        data2.append(coords)
    else:
        name2.append([line])
        flag = 0

flag = 0
for line in dim1:   # read the result of business names and scores 1 dimension
    if(flag == 0):
        line = line[0:-1]
        data1.append(line)
    else:
        name1.append([line])
        flag = 0

flag = 0
for line in twitter:  # read the result of twitters names and scores
    if(flag == 0):
        line = line[1:-2]
        sp = line.split(",")
        pointx = float(sp[0])
        pointy = float(sp[1])
        coords = [pointx, pointy]
        flag = 1
        scores.append(coords)
    else:
        users.append([line])
        flag = 0

for score in scores: # mapping of recommendation
    if score[0]<5:
        score[0] = 10 - score[0]
    if score[1]<6:
        score[1] = 10 - score[1]


kmeans = KMeans(n_clusters=k)
result1 = kmeans.fit(data2)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print(centroids)

prediction = kmeans.predict(twitter)
print(prediction)


for i in range(0, k):
    count = {}
    output = open("2d"+str(i)+".txt", 'a')
    poss = np.where(labels == i)
    for pos in poss[0]:
            output.write(str(data2[pos])+";")
            title = ''.join(name2[pos])
            title = title.strip()
            if title not in count:
                   count[title] = 1
            else:
                   count[title] += 1
    Scount= sorted(count.iteritems(), key=lambda d : d[1], reverse = True)
    print[Scount]

    output.close


result2 = kmeans.fit(data1)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print(centroids)


for i in range(0, k):
    count = {}
    output = open("1d"+str(i)+".txt", 'a')
    poss = np.where(labels == i)
    for pos in poss[0]:
            output.write(str(data2[pos])+";")
            title = ''.join(name2[pos])
            title = title.strip()
            if title not in count:
                   count[title] = 1
            else:
                   count[title] += 1
    Scount = sorted(count.iteritems(), key=lambda d : d[1], reverse = True)
    print[Scount]

    output.close
