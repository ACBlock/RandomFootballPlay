import random
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

class Player:
	def __init__(self, pos, resp):
		self.pos = pos
		self.resp = resp


def TypePlay(RB):
	if RB == 0:
		play = "Pass"
	else:
		play = random.choice(["Run", "Pass"])
	return play


def GenerateNumPlayers():
	"""Generates the number of offensive non QB, non OL players on a football field. Returns number of RB, TE, WR"""
	RB = random.randint(0, 3)
	if RB == 3:
		TE = random.randint(0, 2)
	else:
		TE = random.randint(0, 3)
	WR = 11 - (6 + RB + TE)
	return RB, TE, WR


def GenerateFormation(RB):
	"""Generates the formation an offense is in based on the number of RBs. Returns the formation as a string."""
	if RB == 0:
		formation = random.choice(["Spread"])
	elif RB == 1:
		formation = random.choice(["Ace", "Ace Weak", "Ace Strong"])
	elif RB == 2:
		formation = random.choice(["I", "I Weak", "I Strong", "Split"])
	elif RB == 3:
		formation = random.choice(["Power I"])
	return formation


def GeneratePlayerList(RB, TE, WR, Responsibility, Positions):
	"""Takes number of RB, TE, WR and creates a list of all the players. Return a list of positons and responsibilities."""
	temp = []
	Players = []
	RBs = []
	TEs = []
	WRs = []
	for i in range(RB):
		rb = Player(Positions[2], random.choice(list(Responsibility.keys())[0:2]))
		RBs.append(rb)

	for i in range(TE):
		te = Player(Positions[1], random.choice(list(Responsibility)))
		TEs.append(te)

	for i in range(WR):
		wr = Player(Positions[0], random.choice(list(Responsibility)[1:9]))
		WRs.append(wr)

	temp.append(RBs)
	temp.append(TEs)
	temp.append(WRs)
	for i in temp:
		for j in i:
			Players.append(j.pos)
			Players.append(j.resp)

	return Players


def GenerateRouteNumber(Rlist, dict):
	"""Returns a string that identifies the routes that the eligible recivers run on a given play"""
	Routes = []
	RouteNumber = []
	for i in Rlist[0::1]:
		Routes.append(i)
	for i in Routes:
		if i == "Block":
			Routes.remove(i)
	for i in Routes:
		if i in dict:
			# RouteNumber.append(i)
			RouteNumber.append(dict[i])

	return RouteNumber


def RunPlay():
	Run = random.choice(["Dive", "Counter", "Draw", "Off-tackle", "Pitch",
						 "Reverse", "Slant", "Sweep", "Trap", "Veer"])
	return Run


Positions = ["WR", "TE", "RB", "QB"]
Responsibilities = {
	"Block": 0,
	"Flat": 1,
	"Slant": 2,
	"Comeback": 3,
	"Curl": 4,
	"Out": 5,
	"In": 6,
	"Corner": 7,
	"Post": 8,
	"Go": 9
}
# ["Go", "Post", "Corner", "In", "Out", "Curl", "Comeback", "Slant", "Flat", "Block"]

RB, TE, WR = GenerateNumPlayers()
play = TypePlay(RB)

formation = GenerateFormation(RB)
PlayerList = GeneratePlayerList(RB, TE, WR, Responsibilities, Positions)
RouteNumber = GenerateRouteNumber(PlayerList, Responsibilities)
# print(GenerateRouteNumber(PlayerList, Responsibilities))
print(PlayerList)
print(play)

print("The offense is in", str(RB) + str(TE), "personnel", "and the formation is ", formation)

if play == "Pass":
	print("The Playcall is ", formation, RouteNumber)
else:
	print("The Playcall is ", formation, RunPlay())

num_plays = 10
playbook = {'Type': [], 'Formation': [], 'Player1 Pos': [], 'Player1 Route': [], 'Player2 Pos': [], 'Player2 Route': [],
			'Player3 Pos': [], 'Player3 Route': [], 'Player4 Pos': [], 'Player4 Route': [], 'Player5 Pos': [],
			'Player5 Route': []}
for i in range(num_plays):
	RB, TE, WR = GenerateNumPlayers()
	Players = GeneratePlayerList(RB, TE, WR, Responsibilities, Positions)
	playbook['Type'].append(TypePlay(RB))
	if "Run" in playbook.values():
		playbook['Formation'].append(GenerateFormation(RB))
		playbook['Player1 Pos'] = "RB"
		playbook['Player1 Route'] = "Run"
		playbook['Player2 Pos'].append(Players[2])
		playbook['Player2 Route'].append("Block")
		playbook['Player3 Pos'].append(Players[4])
		playbook['Player3 Route'].append("Block")
		playbook['Player4 Pos'].append(Players[6])
		playbook['Player4 Route'].append("Block")
		playbook['Player5 Pos'].append(Players[8])
		playbook['Player5 Route'].append("Block")
playbook_df = pd.DataFrame.from_dict(playbook)
print(playbook_df)
playbook_df.to_csv(r'c:\Users\Andre\Desktop\playbook.csv', index=False, header=True)
