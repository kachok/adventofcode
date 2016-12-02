f = open("22.input","r")

line=f.readline().strip().split(":")[1]
points=int(line)
line=f.readline().strip().split(":")[1]
damage=int(line)

print points, damage

spells={}
f = open("22.spells","r")

line=f.readline()
for i in range(0,5):
	line=f.readline().strip().split(",")
	#print line
	spells[line[0]]={"mana":int(line[1]), "turns":int(line[2]), "damage":int(line[3]), "heal":int(line[4]), "armor":int(line[5]), "newmana":int(line[6])}

print spells

import copy

u=50
mana=500


import itertools
opt=itertools.product([0,1,2,3,4], repeat=6)
for o in opt:
	print o

	play(o)

#u=10
#mana=250
#points=13
#damage=8


def cast(u, mana, points, damage, active):
	print ">>>>>cast"
	#print "spells", spells
	#print active

	remove=[]
	for sp in active:
		u=u+active[sp]["heal"]
		mana=mana+active[sp]["newmana"]

		points=points-active[sp]["damage"]

		active[sp]["turns"]=active[sp]["turns"]-1
		
		if active[sp]["turns"]<=0:
			remove.append(sp)

	for s in remove:
		print "remove", s, active[s]
		del active[s]

	#print "spells", spells
	return u,mana,points, damage, active

def castone(u, mana, points, damage, active, spell):
	print ">>>>>castone", spell
	#print "spells", spells
	print active, spell, spells[spell]
	u=u+spells[spell]["heal"]
	mana=mana+spells[spell]["newmana"]

	points=points-spells[spell]["damage"]

	if spells[spell]["turns"]>1:
		active[spell]=copy.deepcopy(spells[spell])
		active[spell]["turns"]=active[spell]["turns"]-1


	print active
	print

	#print "spells", spells
	return u,mana,points, damage, active


def play(o, lvl, u, mana, cost, points, damage, active):
	#Player turn
	#Execute spells
	u, mana, points, damage, active = cast(u, mana, points, damage, active)

	#Check for dead
	if u<=0:
		return False,0
	if points<=0:
		return True, cost

	#Pick spell <- fork here
	newspell=""
	mincost=1000000

	for sp in spells:
		print sp
		if sp not in active.keys() and mana>spells[sp]["mana"]:
			newspell=copy.deepcopy(sp)
			mana2=mana-spells[newspell]["mana"]
			cost2=cost+spells[newspell]["mana"]
			u2=u
			points2=points
			damage2=damage
			active2=copy.deepcopy(active)

			#u2, mana2, points2, damage2, active2 = cast(u, mana-spells[sp]["mana"], points, damage, {sp:spells[sp]})

			win, newcost=play(lvl, u2, mana2, cost2, points2, damage2, active2, newspell)
			print win, newcost
			if win:
				if mincost>newcost:
					mincost=newcost

	if newspell=="" or mincost==1000000:
		print "run out of spells"
		return False, cost
	else:
		return True, newcost

	print "NEVER!!!!"
	return False, cost

		#print "spells", spells
	lvl=lvl+1
	if lvl==24:
		print "EXIT"
		exit()
		return False, -1

	print "lvl, u, mana, cost, points, damage, active, newspell"
	print lvl, u, mana, cost, points, damage, active, newspell

	#Player turn continues
	#Execute picked spell
	if newspell!="":
		print "casting: ", newspell
		print lvl, u, mana, cost, points, damage, active, newspell
		u, mana, points, damage, active = castone(u, mana, points, damage, active, newspell)
		print lvl, u, mana, cost, points, damage, active, newspell
		print "----"


	#Check for dead
	if u<=0:
		print "died"
		return False,cost
	if points<=0:
		return True, cost
	
	#Boss turn
	#Execute spells
	u, mana, points, damage, active = cast(u, mana, points, damage, active)

	#Check for dead
	if u<=0:
		return False,0
	if points<=0:
		return True, cost

	#Boss hit
	uhit=damage
	for sp in active:
		uhit=uhit+active[sp]["armor"]
	u=u-max(uhit, 1)

	#Check for dead
	if u<=0:
		return False,0
	if points<=0:
		return True, cost


	return "asdasd"


print "play ----"
#play(u, mana, points, damage, {"boom":spells["Poison"]})


'''
Player turn
Execute spells
Check for dead
Pick spells and execute it <- fork here
Check for dead

Boss turn
Execute spells
Check for dead
Boss hit
Check for dead
'''


active={}
lvl=0
cost=0

newspell=""
mincost=1000000

for sp in spells:
	print sp
	if sp not in active.keys() and mana>spells[sp]["mana"]:
		print "try ", sp
		newspell=copy.deepcopy(sp)
		mana2=mana-spells[newspell]["mana"]
		cost2=cost+spells[newspell]["mana"]
		u2=u
		points2=points
		damage2=damage
		active2=copy.deepcopy(active)

		#u2, mana2, points2, damage2, active2 = cast(u, mana-spells[sp]["mana"], points, damage, {sp:spells[sp]})

		win, newcost=play(lvl, u2, mana2, cost2, points2, damage2, active2, newspell)
		print win, newcost
		if win:
			if mincost>newcost:
				mincost=newcost

print "FINALE! "
if newspell=="":
	print "run out of spells", newspell, mincost
	print False, cost
else:
	print True, newcost, mincost, cost

#print play(0, u, mana, 0, points, damage, {}, "")
