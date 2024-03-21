#Initially imported entire random module and used randint function with range determined by length of list. Just using choice function makes code much simpler to read.
from random import choice
from time import sleep

name_main_character = input("What is your main character's name?\n")
sleep(0.5)
pronouns_main_character = input("\nPlease select the pronouns for your main character:\n 1: she/her\n 2: he/him\n 3: they/them\n")

#Check 1, 2 or 3 selected, otherwise request input again
while pronouns_main_character != "1" and pronouns_main_character != "2" and pronouns_main_character != "3":
    pronouns_main_character = input("Invalid selection. Please select 1, 2 or 3:\n 1: she/her\n 2: he/him\n 3: they/them\n")

pronouns_main_character = int(pronouns_main_character)
pronouns_dictionary = {
    1:["she", "her", "her", "hers"], 
    2:["he", "him", "his", "his"], 
    3:["they", "them", "their", "theirs"]
}

#Create a main character tuple (because won't change). Quicker to reference this than writing variable and dictionary refs each time mc is mentioned.

mc = (name_main_character, pronouns_dictionary[pronouns_main_character])

#Create supporting character dictionary for random character selection: {sc0:[name, relationship, [subject_pronoun, object_pronoun, possessive_adjective, possessive_pronoun]], sc1:[], sc2:[], etc.}
#Try using pop to remove characters from dictionary and assigning them to a list as they are used. To avoid double use of characters.
sc_dictionary = {
    1:["Angelica", "friend", ["she", "her", "her", "hers"]], 
    2:["Simon", "cousin", ["he", "him", "his", "his"]],
    3:["Bob", "elderly neighbour", ["he", "him", "his", "his"]],
    4:["Connie", "work colleague", ["she", "her", "her", "hers"]],
    5:["Dr Lee", "dentist", ["she", "her", "her", "hers"]]
}

#Create lists for weather, day, time, emotions, etc.

weather = ["dreary", "cloudy", "sunny", "warm", "cold", "windy"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time = ["morning", "afternoon", "evening"]
activity = ["cycling", "for a walk", "walking the dog", "rollerskating"]

sleep(0.5)
print(f"\nIt was a {choice(weather)} {choice(day)} {choice(time)} and {mc[0]} was out {choice(activity)}.")
sleep(2.5)
print(f"As {mc[1][0]} rounded the corner, {mc[1][0]} noticed something strange.")
sleep(2.5)
#Create random/user selected events and reactions

event = ["bank robbery", "car pile-up", "dog fight"]
reaction = ["keep walking", "call for help", "go assist"]

print(f"A {choice(event)} was taking place in the street ahead.")
sleep(2.5)
mc_reaction = input(f"\nWhat should {mc[0]} do?:\n 1: {reaction[0]}\n 2: {reaction[1]}\n 3: {reaction[2]}\n")

while mc_reaction != "1" and mc_reaction != "2" and mc_reaction != "3":
    mc_reaction = input(f"Invalid selection. Please select 1, 2 or 3:\n 1: {reaction[0]}\n 2: {reaction[1]}\n 3: {reaction[2]}\n")

mc_reaction = int(mc_reaction)

sleep(1)
print(f"\n{mc[0]} decided to {reaction[mc_reaction-1]}.")

#Investigate Colorama to include colour in outputs (see Lesson 7 notes) and whether can pause between print statements