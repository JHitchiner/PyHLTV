#!/usr/bin/python

import requests
from lxml import html
from hltvplayer import *

def parseHTLVhtml(r):

	#Takes in a request object and returns a player object

	# Check to see if got 200 response back, if not end parsing
	if r.status_code != 200:
		print("Unable to parse html, got status code", r.status_code)
	# Continue if got 200 response
	# Convert response to strcutred format, create new player object, fill statistics
	tree = html.fromstring(r.content)
	igname = tree.xpath('//h1[@class="summaryNickname text-ellipsis"]/text()')[0]
	player = Player(igname) # Creater player object to fill in stats

	# Now have player object, time to fill in all statistics
	irlname = tree.xpath('//div[@class="text-ellipsis"]/text()')[0]
	player.updateStat("IRL_Name", irlname)

	currteam = tree.xpath('//a[@class="a-reset text-ellipsis"]/text()')[0]
	player.updateStat("Current_Team", currteam)

	age = tree.xpath('//div[@class="summaryPlayerAge"]/text()')[0]
	age = int(age.replace(" years", ""))
	player.updateStat("Age", age)

	totkills = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[1]/span[2]/text()')[0]
	player.updateStat("Total_Kills", int(totkills))

	hsperc = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[2]/span[2]/text()')[0]
	hsperc = round((float(hsperc.replace("%", "")) / 100.0), 4) #Round to make less ugly
	player.updateStat("Headshot_Perc", hsperc)

	totdeath = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[3]/span[2]/text()')[0]
	player.updateStat("Total_Deaths", int(totdeath))

	kdratio = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[4]/span[2]/text()')[0]
	player.updateStat("KD_Ratio", float(kdratio))

	dmgpround = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[5]/span[2]/text()')[0]
	player.updateStat("Damage_Per_Round", float(dmgpround))

	nadedmgpround = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[6]/span[2]/text()')[0]
	player.updateStat("Nade_Damage_Per_Round", float(nadedmgpround))

	mapsplayed = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[1]/div[7]/span[2]/text()')[0]
	player.updateStat("Maps_Played", int(mapsplayed))

	roundsplayed = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[1]/span[2]/text()')[0]
	player.updateStat("Rounds_Played", int(roundsplayed))

	killspround = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[2]/span[2]/text()')[0]
	player.updateStat("Kills_Per_Round", float(killspround))

	assistsperround = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[3]/span[2]/text()')[0]
	player.updateStat("Assists_Per_Round", float(assistsperround))

	deathsperround = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[4]/span[2]/text()')[0]
	player.updateStat("Deaths_Per_Round", float(deathsperround))

	savedbyteam = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[5]/span[2]/text()')[0]
	player.updateStat("Saved_By_Teammates_Per_Round", float(savedbyteam))

	savedteam = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[6]/span[2]/text()')[0]
	player.updateStat("Saved_Teammates_Per_Round", float(savedteam))

	rating = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[8]/div/div[2]/div[7]/span[2]/text()')[0]
	player.updateStat("Rating", float(rating))

	#Print full player stats after filling for debugging
	#print(player.Player_Statistics.items())

	return player

	