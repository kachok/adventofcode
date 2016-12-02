rep=[]

mol=""

bucket=[]

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
		rep.append({"el":cmd[0],"repl":cmd[2]})

f.close()

f = open("19.input","r")

input=f.read()

#input=input.replace("B", "Bb")


input=input.replace("B", "Bb")
input=input.replace("F", "Ff")
input=input.replace("H", "Hh")
input=input.replace("N", "Nn")
input=input.replace("O", "Oo")
input=input.replace("P", "Pp")

input=input.replace("CR", "CcR")
input=input.replace("Y", "Yy")


print input

input=input.replace("Ar", "Ar\n")

print input

mol2=mol

count=0
for el in rep:

	if el["repl"].find("Ar")>0:
		mol2=mol2.replace(el["repl"], el["el"])
		print len(mol), len(mol2)

print mol2