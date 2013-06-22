# Pitcher class
# Represents a pitcher in game, holds a pitcher's stats

import math

class pitcher:
		
	def __init__(self, name="", o="", h="", r="", er="", bb="", so="", p="", s="", era="", note="", id=""):
		self.name = name
		self.o = o
		self.h = h
		self.r = r
		self.er = er
		self.bb = bb
		self.so = so
		self.p = p
		self.s = s
		self.era = era
		self.note = note
		self.id = id
		
	def __str__(self):
		s = " "
		ip = ""
		ps = ""
		if self.id != "":
			ip = str(math.floor((float(self.o)/3.0)*10)/10)
			s = "[" + str(self.name) + "](http://mlb.mlb.com/team/player.jsp?player_id=" + str(self.id) + ")"
			ps = str(self.p) + "-" + str(self.s)
		s = s + "|" + ip + "|" + str(self.h) + "|" + str(self.r) + "|" + str(self.er) + "|" + str(self.bb) + "|" + str(self.so) + "|" + ps + "|" + self.era + "|" + str(self.note) + "|"
		return s
		
		
# Batter class
# Represents a batter in game, holds a batter's stats
		
class batter:
		
	def __init__(self="", name="", pos="", ab="", r="", h="", rbi="", bb="", so="", ba="", id=""):
		self.name = name
		self.pos = pos
		self.ab = ab
		self.r = r
		self.h = h
		self.rbi = rbi
		self.bb = bb
		self.so = so
		self.ba = ba
		self.id = id
	
	def __str__(self):
		s = " "
		if self.id != "":
			s = "[" + str(self.name) + "](http://mlb.mlb.com/team/player.jsp?player_id=" + str(self.id) + ")"
		s = s + "|" + str(self.pos) + "|" + str(self.ab) + "|" + str(self.r) + "|" + str(self.h) + "|" + str(self.rbi) + "|" + str(self.bb) + "|" + str(self.so) + "|" + str(self.ba) + "|"
		return s
