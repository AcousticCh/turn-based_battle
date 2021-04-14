from battleA import Monster
import random
import subprocess as sub

mon1 = Monster(900, 100, 250, 250, 500)
mon2 = Monster(800, 200, 200, 300, 500)
pika = Monster(700, 100, 300, 300, 400)
# to do:
# create multiple monsters and setup random monster selection with dictionary
# build monster creator 
# change pika to enemy that functions like player object

def battle_start():
	sub.run("clear")
	print("Create your monster!")
	print("You have a total of 2000 points to distribute between\nmax health, defense, and 3 attacks")
	points_available = 2000
	print(f"Points available = {points_available}.")
	health = int(input("Health limit is 1000.\nHealth = "))
	points_available -= health
	print(f"Points available = {points_available}.")
	defense = int(input("Defense limit is 300.\nDefense = "))
	points_available -= defense
	print("Attack damage is limitless inside of the total point limit")
	print(f"Points available = {points_available}.")
	attack1 = int(input("Attack 1 = "))
	points_available -= attack1
	print(f"Points available = {points_available}.")
	attack2 = int(input("Attack 2 = "))
	points_available -= attack2
	print(f"Points available = {points_available}.")	
	attack3 = int(input("Attack 3 = "))
	points_available -= attack3
	sub.run("clear")
	
	player = Monster(health, defense, attack1, attack2, attack3)
	
	battle = True
	while battle:
		player_turn(player)
		check_health(player)
		monster_turn(player)
		check_health(player)

def enemy_selection():
	#create a dictionary of enemy monsters
	#select random enemy for enemy object
	#enemy = random.randint()
	pass

def player_turn(player):
	print("attack choice:")
	print(f"1: attack 1, damage: {player.attack1} ")
	print(f"2: attack 2, damage: {player.attack2} ")
	print(f"3: attack 3, damage: {player.attack3} ")
	move_choice = input("select your move: ")
	sub.run("clear")
	if move_choice == "1":
		pika.current_health -= player.attack1 - pika.defense
		print(f"Pickachu current health is {pika.current_health}")
	if move_choice == "2":
		pika.current_health -= player.attack2 - pika.defense
		print(f"Pickachu current health is {pika.current_health}")
	if move_choice == "3":
		pika.current_health -= player.attack3 - pika.defense
		print(f"Pickachu current health is {pika.current_health}")
def monster_turn(player):
	move_choice = random.randint(1, 3)
	if move_choice == 1:
		damage_dealt = pika.attack1 - player.defense
		player.current_health -= damage_dealt
		print(f"Pikachu chose attack 1 and dealt {damage_dealt} damage")
		print(f"Player current health is {player.current_health}")
	if move_choice == 2:
		damage_dealt = pika.attack2 - player.defense
		player.current_health -= damage_dealt
		print(f"Pikachu chose attack 2 and dealt {damage_dealt} damage")
		print(f"Player current health is {player.current_health}")
	if move_choice == 3:
		damage_dealt = pika.attack3 - player.defense
		player.current_health -= damage_dealt
		print(f"Pikachu chose attack 3 and dealt {damage_dealt} damage")
		print(f"Player current health is {player.current_health}")

def check_health(player):
	if pika.current_health <= 0:
		print("player wins")
		quit()
	elif player.current_health <= 0:
		print("monster wins")
		quit()
	
		
		

battle_start()
