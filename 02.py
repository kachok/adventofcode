f = open("02.input","r")

tots=0

ribbon=0

for line in f:
	line=line.strip()
	dim=line.split("x")
	dim=[int(dim[0]), int(dim[1]), int(dim[2])]

	a,c=min(dim[0],dim[1], dim[2]),max(dim[0],dim[1], dim[2])
	b=dim[0]+dim[1]+dim[2]-a-c
	print dim
	print a,b,c
	print "paper", 2*(a*b+a*c+c*b)+a*b
	tots=tots+2*(a*b+a*c+c*b)+a*b

	print "ribbon", 2*(a+b)+a*b*c
	ribbon=ribbon+2*(a+b)+a*b*c


print "tots"
print tots


print "ribbon"
print ribbon
