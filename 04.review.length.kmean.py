from ast import While
import json
import numpy as np

# open the file
review_file = open("../data_test/yelp_academic_dataset_review.json")

data = []
count = 0

# Load the data
with review_file as f:
    for line in f:
        if count == 20:
            break
        data.append(json.loads(line))
        count = count + 1

maxtrix_text_length = []

# Extract the text from the data
texts = [d['text'] for d in data]
# Extract the length of the text
for text in texts:
    maxtrix_text_length.append(len(text))
print(maxtrix_text_length)

# get 3 random centroids
centroids = np.random.choice(maxtrix_text_length, 3)
print("Random centroids: ", centroids)

# create 3 clusters which created by element near by the centroids from maxtrix_text_length
clusters = [[], [], []]
for i in maxtrix_text_length:
    if abs(i - centroids[0]) < abs(i - centroids[1]) and abs(i - centroids[0]) < abs(i - centroids[2]):
        clusters[0].append(i)
    elif abs(i - centroids[1]) < abs(i - centroids[0]) and abs(i - centroids[1]) < abs(i - centroids[2]):
        clusters[1].append(i)
    elif abs(i - centroids[2]) < abs(i - centroids[0]) and abs(i - centroids[2]) < abs(i - centroids[1]):
        clusters[2].append(i)

print("The clusters are: ")
print(clusters)
# find the new centroid element from list element in clusters
new_centroids = []
for i in range(0, len(clusters)):
    # mean of the cluster
    _mean_centroid = np.mean(clusters[i])
    _new_centroid = clusters[i][0]
    for item in clusters[i]:
        # find the element in the cluster which is near by the mean of the cluster
        if abs(item - _mean_centroid) < abs(_new_centroid - _mean_centroid):
            _new_centroid = item
    new_centroids.append(_new_centroid)

print("The new centroids are: ")
print(new_centroids)
    
