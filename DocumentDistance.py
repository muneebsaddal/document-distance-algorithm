import math
import time

# timer starts here
start_time = time.clock()

fhand = open('file 1.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

fhand1 = open('file 2.txt')
counts1 = dict()
for line in fhand1:
    words = line.split()
    for word in words:
        if word not in counts1:
            counts1[word] = 1
        else:
            counts1[word] += 1

# Calculating magnitude of document
d1_magnitude = 0
for key in counts:
	d1_magnitude += math.pow(counts[key], 2)
d1_magnitude = math.sqrt(d1_magnitude)

d2_magnitude = 0
for key in counts1:
	d2_magnitude += math.pow(counts1[key], 2)
d2_magnitude = math.sqrt(d2_magnitude)

# Dot Product of common words
d1_keys = set(counts.keys())
d2_keys = set(counts1.keys())
intersect_keys = d1_keys.intersection(d2_keys)
a = []
b = []
c = []
for letters in set(intersect_keys):
	a.append(counts[letters])
	b.append(counts1[letters])
for value in range(len(a)):
	c.append(a[value] * b[value])

# Calculating theta
theta = (math.acos(sum(c) / (d1_magnitude * d2_magnitude))) * 57.2957795131

# Timer ends here
time = round(((time.clock() - start_time) * 1000))

# Showing output
print("\nDocument Distance ---> %s degree" % (round(theta, 2)))
print("Execution time ---> %s milliseconds\n" % time)
