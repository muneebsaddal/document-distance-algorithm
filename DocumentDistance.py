import re
import math
import time

# timer starts here
start_time = time.clock()

# declaring dictionaries
dic1 = {}
dic2 = {}

# opening files
D1 = open('file 1.txt', 'r') 	# 362,366 words
D2 = open('file 2.txt', 'r') 	# 312,295 words

# creating list of words
str1 = D1.read().lower()
str1 = re.findall(r'\b[a-z]{1,15}\b', str1)
str2 = D2.read().lower()
str2 = re.findall(r'\b[a-z]{1,15}\b', str2)

# storing freqency of words in Dictionary
for word in str1:
	count = dic1.get(word, 0)
	dic1[word] = count + 1

for word in str2:
	count = dic2.get(word, 0)
	dic2[word] = count + 1

# Calculating magnitude of document
d1_magnitude = 0
for key in dic1:
	d1_magnitude += math.pow(dic1[key], 2)
d1_magnitude = math.sqrt(d1_magnitude)

d2_magnitude = 0
for key in dic2:
	d2_magnitude += math.pow(dic2[key], 2)
d2_magnitude = math.sqrt(d2_magnitude)

# Dot Product of common words
d1_keys = set(dic1.keys())
d2_keys = set(dic2.keys())
intersect_keys = d1_keys.intersection(d2_keys)
a = []
b = []
c = []
for letters in set(intersect_keys):
	a.append(dic1[letters])
	b.append(dic2[letters])
for value in range(len(a)):
	c.append(a[value] * b[value])

# Calculating theta
theta = (math.acos(sum(c) / (d1_magnitude * d2_magnitude))) * 57.2957795131

# Timer ends here
time = round(((time.clock() - start_time) * 1000))

# Showing output
print("\nDocument Distance ---> %s degree" % (round(theta, 2)))
print("Execution time ---> %s milliseconds\n" % time)
