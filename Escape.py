import math

def open_game ():
#Opening message for player once game begins
	print "Good morning, Captain Zhorkov. The year is 2314."
#raw_input is included here to slowly output the opening message, as user reads
	gap = raw_input("")
	print "You have been chosen by the Federation of Space Expansion" 
	gap = raw_input("")
	print "to serve as the leader on a human mission to colonize other planets."
	gap = raw_input("")
	print "Your current spaceship Beagle is equipped with"
	gap = raw_input("")
	print "mineral harvesting technology, 100 food," 
	gap = raw_input("")
	print "10 well-trained men and women at 100% health, and 10 mineral."
	gap = raw_input("")
	print "Godspeed to you!"
	gap = raw_input("")
	leave_earth()

#Template for game logo that is displayed before game begins
opening_line = """
E  S  C  A  P  E
v1	-bhaskaraspb 
"""

#This function displays the game logo and allows the user to begin the game
def start_game () :
	print "\n"
	for i in opening_line:
		print i,
	print "\n"
	decision = raw_input("\tTo play, type GO:\n\t")
	if "GO" in decision:
		open_game () 
	
#Beginning stats for the user 
#At the moment these are static; next version should include randomness
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

#User views starting stats as user lands on Mars
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
	next_turn()

#Refreshes stats upon each turn. Calls each helper function refresh the corresponding stat.
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
	next_turn()

# Allows the user to build structures or research technologies
def next_turn():
	decision = raw_input("What would you like to do now?\n")
	if "greenhouse" in decision:
		build_greenhouse()
	elif "solar" in decision:
		build_solar_farm()
	elif "mineral harvester" in decision:
		build_mineral_harvester()
	elif "engineering school" in decision:
		build_engineering_school()
	elif "science lab" in decision:
		build_science_lab()
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

# Provides the user with all possible options of structures to build and technologies to research
def print_options ():
	print """
	Greenhouse: 
	*Takes 1 mineral to construct
	*Produces 5 food per year
	*Requires 1 mineral per year for upkeep
	
	Mineral harvester: 
	*Takes 1 mineral and 10 energy to construct 
	*Produces 5 mineral per year
	
	Solar farm: 
	*Takes 1 mineral to construct 
	*Produces 1 energy per year 
	*Require 1 mineral per year for upkeep 
	*Without battery tech, no more than 100 energy can be stored
	
	Engineering school: 
	*Takes 20 mineral to construct 
	*Produces 1 knowledge per year
	
	Science lab: 
	*Requires a knowledge level of 20
	*Takes 50 mineral to construct 
	*Produces 5 knowledge per year
	
	Battery tech: 
	*Requires a knowledge level of 50
	*Takes 100 mineral to construct 
	*It allows you to store an unlimited amount of energy
	
	Hibernation: 
	*Requires a knowledge level of 200 
	*Takes 200 mineral to contruct
	*A key technology for interstellar travel
	
	Ion engine: 
	*Requires knowledge level of 1000
	*Takes 500 mineral to construct
	*A key technology for interstellar travel
	"""
	next_turn()

#Refreshes the energy count	
def energy_refresh():
	global energy_count
	global human_count
	global solar_farms
	global technologies
	if energy_count > 0: energy_count = energy_count - 1*human_count + 5*solar_farm_count
	if "battery_tech" not in technologies and energy_count >= 100:
		energy_count = 100
		print "Can't store more than 100 energy without battery technology."

#Refreshes the human count based on natural growth rate and starvation if food count drops
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

# Refreshes the mineral count
def mineral_refresh():
	global mineral_count
	global human_count
	global mineral_harvester_count
	global greenhouse_count
	global solar_farm_count
	if mineral_count > 0:
		mineral_count = mineral_count - greenhouse_count - solar_farm_count + 5 * mineral_harvester_count
	
# Refreshes the food count
def food_refresh():
	global human_count
	global food_count
	global greenhouse_count
	food_count = food_count - human_count + 5*greenhouse_count

# Refreshes the health of the colony
def health_refresh():
	global human_count
	global food_count
	global health_level
	if food_count / human_count > 3 and health_level < 1.00: 
		health_level += 0.01
	elif food_count / human_count > 1: 
		health_level = health_level
	else: health_level -= 0.01

# Refreshes the knowledge level	
def knowledge_refresh():
	global knowledge_level
	global engineering_school_count	
	knowledge_level = knowledge_level + engineering_school_count + 5 * science_lab_count

# Builds a greenhouse
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

#Builds a solar farm
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

#Builds a mineral harvester
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

#Builds an engineering school
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

#Builds a science lab
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

#Researches battery tech
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

#Researches hibernation
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

#Researches ion engine
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

#User can voluntarily quit the game
def quit_game():
	print "You have abandoned your species!"
	exit(0)

#Exits the game if colony dies because of low resources or extinction
def colony_dies(reason):
	print "Your colony perishes because", reason
	exit(0) 

#User wins the game by successfully leaving Mars and going to Alpha Centauri
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
		...
		Congratulations! It is the year %d and you have reached Alpha Centauri.
		You have saved the human race by starting a colony outside of our solar system.
		Come back and play Escape V2 for more action.
		""" % year
		print closing_message
		exit(0)

start_game()