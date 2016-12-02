f = open("16.input","r")

tots=0
aunts={}

r={
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1	
}

for line in f:
	#print "---"
	line=line.strip()
	line=line.strip(".")
	line=line.replace(",","")
	cmd=line.split(" ")

	aunts[cmd[1]]={}

	for i in range(0, (len(cmd)-2)/2):
		aunts[cmd[1]][cmd[2+2*i][:-1]]=int(cmd[2+2*i+1])

	#print cmd
#print aunts

for a in aunts:
	print a, aunts[a], r

	her=True
	for el in r:
		print "el", el, r[el], aunts[a], aunts[a].keys()
		if el in aunts[a].keys():
			#print ">>", aunts[a][el]
			
			if (el=="cats" or el=="trees"):
				if aunts[a][el]<=r[el]:
					her=False
					print "catstrees"
			elif (el=="pomeranians" or el=="goldfish"):
				if aunts[a][el]>=r[el]:
					her=False
					print "pomgold"
			elif aunts[a][el]!=r[el]:
				print "false", el
				her=False

	if her:
		print "her", a, aunts[a]
		break
