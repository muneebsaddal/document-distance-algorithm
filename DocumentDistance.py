import re
import string

D1_freq = {}
D2_freq = {}
D1 = open('file 1.txt', 'r')
D2 = open('file 2.txt', 'r')
str1 = D1.read().lower()
str1 = re.findall(r'\b[a-z]{1,15}\b', str1)
str2 = D2.read().lower()
str2 = re.findall(r'\b[a-z]{1,15}\b', str2)
for word in str1:
    count = D1_freq.get(word,0)
    D1_freq[word] = count + 1
     
D1_freq_list = D1_freq.keys()
 
for words in D1_freq_list:
    print (words, D1_freq[words])