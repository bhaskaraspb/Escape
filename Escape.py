# this is displayed to the user upon starting game

import math

def open_game ():
	opening_message = """
	
	Good morning, Captain Zhorkov. The year is 2314. You have been chosen by the Federation of Space Expansion to serve as the leader on a human mission to colonize other planets. 
	Your current spaceship Beagle is equipped with mineral harvesting technology, 100 food, 10 well-trained men and women at 100% health, and 10 mineral. Godspeed to you!
	"""
	print opening_message
	leave_earth()

opening_line = "\tESCAPE"

def start_game () :
	print "\n"
	for i in opening_line:
		print i,
	print "\n"
	decision = raw_input("\tTo play, type GO.")
	if "GO" in decision:
		open_game () 
	
year = 2314
energy_count = 100
human_count = 10
mineral_count = 10
food_count = 100
health_level = 1.00
knowledge_level = 5
solar_farm_count = 0
greenhouse_count = 0
mineral_harvester_count = 0
engineering_school_count = 0
science_lab_count = 0
solar_farm_count = 0
technologies = []

def leave_earth (): 
	global year
	year += 1
	print "\nYou are now arriving on Mars. The year is %d." % year
	print "You have %d energy." % energy_count
	print "You have %d humans in your colony." % math.ceil(human_count)
	print "You have %d mineral." % mineral_count
	print "You have %d food." % food_count
	print "The health of your colony is %d." % health_level
	print "The knowledge level of your colony is %d." % knowledge_level
		
	decision = raw_input("What would you like to do now?")
	
	if "greenhouse" in decision:
#		number = raw_input("How many?")
		build_greenhouse()# * number
	elif "solar" in decision:
#		number = raw_input("How many?")
		build_solar_farm()# * number
	elif "mineral harvester" in decision:
#		number = raw_input("How many?")
		build_mineral_harvester()# * number
	elif "engineering school" in decision:
#		number = raw_input("How many?")
		build_engineering_school()# * number
	elif "science lab" in decision:
#		number = raw_input("How many?")
		build_science_lab()# * number
	elif "battery" in decision:
		research_battery_tech()
	elif "ion engine" in decision:
		research_ion_engine()
	elif "options" in decision:
		print_options()
	elif "quit" in decision:
		quit_game()
	else: pass_turn()

def pass_turn ():
	global year
	year +=1
	human_refresh()
	energy_refresh()
	mineral_refresh()
	food_refresh()
	health_refresh()
	knowledge_refresh()
	
	if human_count < 2: 
		colony_dies("all of your colonists have died.")
	if energy_count < human_count:
		colony_dies("you have run out of enough energy.")
	if food_count < human_count:
		colony_dies("you have run out of food.")
	
	print "\nThe year is %d." % year
	print "You have %d energy." % energy_count
	print "You have %d humans in your colony." % math.ceil(human_count)
	print "You have %d mineral." % mineral_count
	print "You have %d food." % food_count
	print "The health of your colony is %d." % health_level
	print "The knowledge level of your colony is %d." % knowledge_level
	print "You have %d solar farms." % solar_farm_count
	print "You have %d greenhouses." % greenhouse_count
	print "You have %d mineral harvesters." % mineral_harvester_count
	print "You have %d engineering schools." % engineering_school_count
	print "You have %d science labs." % science_lab_count
	print "You have researched these technologies: %s." % technologies
	print "View your building options by typing 'options'."
		
	decision = raw_input("What would you like to do now?")
	
	if "greenhouse" in decision:
#		number = raw_input("How many?")
		build_greenhouse()# * number
	elif "solar" in decision:
#		number = raw_input("How many?")
		build_solar_farm()# * number
	elif "mineral harvester" in decision:
#		number = raw_input("How many?")
		build_mineral_harvester()# * number
	elif "engineering school" in decision:
#		number = raw_input("How many?")
		build_engineering_school()# * number
	elif "science lab" in decision:
#		number = raw_input("How many?")
		build_science_lab()# * number
	elif "battery" in decision:
		research_battery_tech()
	elif "hibernation" in decision:
		research_hibernation()
	elif "ion engine" in decision:
		research_ion_engine()
	elif "options" in decision:
		print_options()
	elif "Alpha Centauri" in decision:
		leave_planet()
	elif "quit" in decision:
		quit_game()
	else: pass_turn()

# Currently time is not considered a factor among the options to build; this should be included as an improvement
def print_options ():
	print """
	Greenhouse: takes 1 mineral to construct and produces 1 food per year
	Mineral harvester: takes 5 mineral to construct and produces 1 mineral per year
	Solar farm: takes 10 mineral to construct and produces 1 energy per year. This energy is intermittent cannot be stored.
	Engineering school: takes 20 mineral to construct and produces 1 knowledge per year until knowledge reaches 20
	Battery tech: requires knowledge level of 10 and 10 mineral to construct. It allows you to store up to 100 energy.
	Ion engine: requires knowledge level of 10 and 100 mineral to construct.
	"""
	pass_turn()
	
def energy_refresh():
	global energy_count
	global human_count
	global solar_farms
	global technologies
	if energy_count > 0: energy_count = energy_count - 1*human_count + 5*solar_farm_count
	if "battery_tech" not in technologies and energy_count >= 100:
		energy_count = 100
		print "Can't store more than 100 energy without battery technology."

def human_refresh():
	global health_level
	global energy_count
	global human_count
	if health_level > 0.9:
		human_count = human_count * 1.03
	elif health_level > 0.8:
		human_count = human_count
	elif health_level > 0.5:
		human_count = human_count * 0.8
	else: human_count = human_count * 0.6

def mineral_refresh():
	global mineral_count
	global human_count
	global mineral_harvester_count
	global greenhouse_count
	global solar_farm_count
	if mineral_count > 0:
		mineral_count = mineral_count - greenhouse_count - solar_farm_count + 5 * mineral_harvester_count
	
def food_refresh():
	global human_count
	global food_count
	global greenhouse_count
	food_count = food_count - human_count + 5*greenhouse_count

def health_refresh():
	global human_count
	global food_count
	global health_level
	if food_count / human_count > 3 and health_level < 1.00: 
		health_level += 0.01
	elif food_count / human_count > 1: 
		health_level = health_level
	else: health_level -= 0.01
	
def knowledge_refresh():
	global knowledge_level
	global engineering_school_count	
	knowledge_level = knowledge_level + engineering_school_count + 5 * science_lab_count

def build_greenhouse():
	global year
	global mineral_count
	global greenhouse_count
	if mineral_count > 1:
		mineral_count -= 1
		greenhouse_count += 1
		pass_turn()
	else: 
		print "Insufficient mineral."
		pass_turn()

def build_solar_farm():
	global year
	global solar_farm_count
	global energy_count
	global mineral_count
	if mineral_count > 1:
		mineral_count -= 1
		solar_farm_count += 1
		pass_turn()
	else: 
		print "Insufficient mineral."
		pass_turn()

def build_mineral_harvester():
	global year
	global mineral_count
	global energy_count
	global mineral_harvester_count
	if mineral_count > 1:
		mineral_count -= 1
		energy_count -= 10
		mineral_harvester_count += 1
		pass_turn()
	else: 
		print "Insufficient mineral."
		pass_turn()
		
def build_engineering_school():
	global year
	global mineral_count
	global engineering_school_count
	if mineral_count > 10:
		mineral_count -= 10
		engineering_school_count += 1
		pass_turn()
	else: 
		print "Insufficient mineral."
		pass_turn()
		
def build_science_lab():
	global year
	global mineral_count
	global science_lab_count
	if knowledge_level >= 20 and mineral_count > 50:
		mineral_count -= 50
		science_lab_count += 1
		pass_turn()
	else: 
		print "Insufficient mineral or knowledge."
		pass_turn()
		
def research_battery_tech():
	global year
	global mineral_count
	global technologies
	global knowledge_level
	if knowledge_level >= 100 and mineral_count > 100:
		mineral_count -= 100
		technologies.append("battery_tech")
		pass_turn()
	else: 
		print "Insufficient mineral or knowledge."
		pass_turn()

def research_hibernation() :
	global year
	global mineral_count
	global technologies
	global knowledge_level
	if knowledge_level >= 200 and mineral_count > 200:
		mineral_count -= 200
		technologies.append("hibernation")
		pass_turn()
	else: 
		print "Insufficient mineral or knowledge."
		pass_turn()
		
def research_ion_engine():
	global year
	global mineral_count
	global technologies
	global knowledge_level
	if knowledge_level >= 1000 and mineral_count > 500:
		mineral_count -= 500
		technologies.append("ion_engine")
		pass_turn()
	else: 
		print "Insufficient mineral or knowledge."
		pass_turn()

def quit_game():
	print "You have abandoned your species!"
	exit(0)

def colony_dies(reason):
	print "Your colony perishes because", reason
	exit(0) 

def leave_planet():
	global year 
	global energy_count
	global technologies
	if "ion_engine" in technologies and "hibernation" in technologies and energy_count >= 1000:
		energy_count -= 1000
		year += 40
		closing_message = """
		
		Preparing for liftoff...
		...
		Taking off!!!
		...
		...
		...min
		Congratulations! It is the year %d and you have reached Alpha Centauri.
		You have saved the human race by starting a colony outside of our solar system.
		Come back and play Escape V2 for more action.
		""" % year
		print closing_message
		exit(0)

#SET energy and solar farms back to 0

start_game()