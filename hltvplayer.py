#!/usr/bin/python

class Player:
	# Player Statistics dictionary
	Player_Statistics = {
	"Ingame_Name" : '',
	"IRL_Name" : '',
	"Current_Team" : '',
	"Age" : 0,
	"Total_Kills" : 0,
	"Headshot_Perc" : 0,
	"Total_Deaths" : 0,
	"KD_Ratio" : 0,
	"Damage_Per_Round" : 0,
	"Nade_Damage_Per_Round" : 0,
	"Maps_Played" : 0,
	"Rounds_Played" : 0,
	"Kills_Per_Round" : 0,
	"Assists_Per_Round" : 0,
	"Deaths_Per_Round" : 0,
	"Saved_By_Teammates_Per_Round" : 0,
	"Saved_Teammates_Per_Round" : 0,
	"Rating" : 0 # Rating 1.0
	}

	def __init__(self, igname):
		self.Player_Statistics["Ingame_Name"] = igname

	def updateStat(self, statname, value):
		# Takes stat name and value and updates players stat
		self.Player_Statistics[statname] = value