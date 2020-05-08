import re

fhand = open('regex_sum_473833.txt','r')
lst = []
for line in fhand:
	line = line.rstrip()
	x = re.findall('[0-9]+',line)
	for i in x:
		i = int(i)
		lst.append(i)

print(sum(lst))