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

#example 1
#u=10
#mana=250
#points=13
#damage=8

#example 2
#u=10
#mana=250
#points=14
#damage=8

'''
turn starts
effects apply

if boss - hit
if player - cast spell

'''

game = {
	"yourturn":True,
	"you": {"hitpoints":u, "mana": mana, "armor":0, "activespells":{}, "manaused":0},
	"boss": {"hitpoints":points, "damage":damage},
	"log":[]
}

import copy

def turn(game):
	#turn starts
	#print game

	#effects apply
	#print "boss before: ", game["boss"]
	game=applyeffects(game)
	#print "boss after : ", game["boss"]

	if (game["boss"]["hitpoints"]<=0):
		return [game] 	

	#if boss - hit
	if (not game["yourturn"]):
		game["you"]["hitpoints"]=game["you"]["hitpoints"]-max(game["boss"]["damage"]-game["you"]["armor"],1)
		#print "boss hit, ",max(game["boss"]["damage"]-game["you"]["armor"],1)
		
		game["yourturn"]=not game["yourturn"]

		if (game["you"]["hitpoints"]<=0):
			return [game]
		return [game]

	#if player - cast spell
	else:
		availablespells=pickspell(game)
		if len(availablespells)==0:
			game["you"]["hitpoints"]=-1
			return [game]
		#print availablespells

		games=[]
		for sp in availablespells:
			newgame = copy.deepcopy(game)
			newgame["log"].append(sp)

			#print "cast ",sp, spells[sp]

			if spells[sp]["turns"]==0:
				#execute spell instantly
				newgame["you"]["hitpoints"]=newgame["you"]["hitpoints"]+spells[sp]["heal"]
				newgame["you"]["mana"]=newgame["you"]["mana"]+spells[sp]["newmana"]

				newgame["you"]["mana"]=newgame["you"]["mana"]-spells[sp]["mana"]


				newgame["boss"]["hitpoints"]=newgame["boss"]["hitpoints"]-spells[sp]["damage"]				

				newgame["you"]["manaused"]=newgame["you"]["manaused"]+spells[sp]["mana"]
			else:
				#add to active spells
				newgame["you"]["manaused"]=newgame["you"]["manaused"]+spells[sp]["mana"]
				newgame["you"]["mana"]=newgame["you"]["mana"]-spells[sp]["mana"]

				newgame["you"]["activespells"][sp]=copy.deepcopy(spells[sp])

			games.append(newgame)

			newgame["yourturn"]=not newgame["yourturn"]

		return games


def applyeffects(game):
	removallist=[]
	game["you"]["armor"]=0

	for sp in game["you"]["activespells"]:
		game["you"]["hitpoints"]=game["you"]["hitpoints"]+game["you"]["activespells"][sp]["heal"]
		game["you"]["mana"]=game["you"]["mana"]+game["you"]["activespells"][sp]["newmana"]

		game["you"]["armor"]=game["you"]["armor"]+game["you"]["activespells"][sp]["armor"]

		game["boss"]["hitpoints"]=game["boss"]["hitpoints"]-game["you"]["activespells"][sp]["damage"]

		game["you"]["activespells"][sp]["turns"]=game["you"]["activespells"][sp]["turns"]-1
		
		if game["you"]["activespells"][sp]["turns"]<=0:
			removallist.append(sp)

	for s in removallist:
		#print "remove", s, game["you"]["activespells"][s]
		del game["you"]["activespells"][s]
	
	return game

def pickspell(game):
	availablespells=[]
	for sp in spells:
		if not (sp in game["you"]["activespells"].keys()):
			if spells[sp]["mana"]<=game["you"]["mana"]:
				availablespells.append(sp)

	return availablespells


print "---"


def run(level, games):
	#print "run ", level
	for game in games:
		if game["you"]["hitpoints"]<=0:
			#print game["log"]
			#print "game over - loss, manaused ", game["you"]["manaused"]
			return
		elif game["boss"]["hitpoints"]<=0:
			print game["log"]
			print "game over - WIN, manaused ", game["you"]["manaused"]
			return
		else:
			g=turn(game)
			run(level+1, g)
	return

run(0, [game])
