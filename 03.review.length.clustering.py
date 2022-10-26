import json
import numpy as np

# open the file
review_file = open("../data_test/yelp_academic_dataset_review.json")

data = []
count = 0

# Load the data
with review_file as f:
    for line in f:
        count = count + 1
        if count == 1000:
            break
        data.append(json.loads(line))

maxtrix_text_length = []

# Extract the text from the data
texts = [d['text'] for d in data]

#calculate the distance between the text length
for i in range(len(texts)):
    for j in range(len(texts)):
        if i != j:
            maxtrix_text_length.append(abs(len(texts[i]) - len(texts[j])))

#find the max and min distance
maxtrix_text_length = np.array(maxtrix_text_length)
min_distance = np.min(maxtrix_text_length)
max_distance = np.max(maxtrix_text_length)
print("min distance: ", min_distance)
print("max distance: ", max_distance)


