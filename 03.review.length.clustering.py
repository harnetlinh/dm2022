import json
import numpy as np


class Cluster:
    def __init__(self, cluster):
        self.cluster = []
        self.cluster.append(cluster)

    def __repr__(self):
        return str(self.cluster)

    def getClusterDistance(self, cluster, dist = 0):
        cluster1 = self.cluster
        cluster2 = cluster.cluster
        _dist = 0
        for i in cluster1:
            for j in cluster2:
                
                if i != j:
                    _dist = abs(i - j)
                    if _dist < dist:
                        dist = _dist

        return dist


# open the file
review_file = open("../data_test/yelp_academic_dataset_review.json")

data = []
count = 0

# Load the data
with review_file as f:
    for line in f:
        if count == 5:
            break
        data.append(json.loads(line))
        count = count + 1

maxtrix_text_length = []

# Extract the text from the data
texts = [d['text'] for d in data]

# Extract the length of the text
for text in texts:

    maxtrix_text_length.append(Cluster(len(text)))

# Convert the list to numpy array
maxtrix_text_length = np.array(maxtrix_text_length)

print(maxtrix_text_length)
