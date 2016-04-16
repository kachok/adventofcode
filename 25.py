row=2947
column=3029


#row=4
#column=3

print "row ", row, ", column ",column


num=1

for i in range(row):
	#print i
	num=num+i

#print num

for j in range(column-1):
	#print j
	num=num+(row+j+1)

print "num ",num

first=20151125
mult=252533
div=33554393


for k in range(num-1):
	first=first*mult%div

	#print k+2, first

print first
