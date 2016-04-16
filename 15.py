f = open("15.input","r")

tots=0
ing={}

for line in f:
	print "---"
	line=line.strip()
	line=line.strip(".")
	line=line.replace(",","")
	cmd=line.split(" ")

	ing[cmd[0]]=[int(cmd[2]),int(cmd[4]),int(cmd[6]),int(cmd[8]),int(cmd[10])]

	print cmd

q1=ing["Sprinkles:"]
q2=ing["Butterscotch:"]
q3=ing["Chocolate:"]
q4=ing["Candy:"]


big=0

for i in range(0,101):
	for j in range (0,101-i):
		for k in range (0,101-i-j):
			for l in range(0,101-i-j-k):

				#i+j+k+l
				s=[0,0,0,0]
				for n in range(0,4):
					s[n]=q1[n]*i+q2[n]*j+q3[n]*k+q4[n]*l

				tots=max(s[0],0)*max(s[1],0)*max(s[2],0)*max(s[3],0)

				cals=q1[4]*i+q2[4]*j+q3[4]*k+q4[4]*l

				if big<tots:
					big=tots
				
				#if :
				#	print ">>>",s, cals, tots
				#	print i,j,k,l, i+j+k+l,

print ing

print big
