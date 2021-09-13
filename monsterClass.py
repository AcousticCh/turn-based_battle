#!/usr/bin/env python

class Monster(object):
	def __init__(self, max_health, defense, attack1, attack2, attack3):
		self.health_limit = 1000
		self.max_health = max_health
		self.current_health = self.max_health
		self.defense = defense
		self.attack1 = attack1
		self.attack2 = attack2
		self.attack3 = attack3
		if self.current_health > self.max_health:
			self.current_health = self.max_health
		if self.max_health + self.defense + self.attack1 + self.attack2 + self.attack3 > 2000:
			print("Too many points, limit is 2000")
	
	def boostHealth(self, boost):
		self.max_health += boost
		self.current_health += boost
		
