rep=[]

mol=""

bucket=[]

oldone=set([])

#f = open("19-test.input","r")
f = open("19.input","r")

lastone=False
for line in f:
	line=line.strip()

	if line=="":
		lastone=True
	elif lastone:
		mol=line.strip()
	else:
		cmd=line.split(" ")
		rep.append({"repl":cmd[0],"el":cmd[2]})


print rep
print mol

print "---"

tots=0


l=[]

el=""
for ch in mol:
	if str.istitle(ch):
		if el=="":
			el=el+ch
		else:
			l.append(el)
			el=ch
	else:
		el=el+ch
		l.append(el)
		el=""

l.append(el)

print l
print len(l)

rn=0
y=0
ar=0

count=-1
for el in l:
	count=count+1
	#print el
	if el=="Rn":
		count=count-3
		rn=rn+1
	if el=="Y":
		count=count-2
		y=y+1
	if el=="Ar":
		ar=ar+1


print count
print rn,y,ar


print "answer"
print len(l)-1-y*2-rn*2
#292 = 291 - 6*2 - 37*3