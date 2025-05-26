
q1 = ("apple", "banana", "cherry","dog",4,5,6,7,8,9)
q2 = ("💖 Quest Avaliable - Roger's apple", 
             "Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")


# -- List Quests & Details
quest0 = {
  "name": "Ford",
  "status": "Avaliable",
  "steps": ["red", "white", "blue"]
}

quest1 = {
  "name": "Roger's apple",
  "status": "Avaliable",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest2 = {
  "name": "Mays's Medicine",
  "status": "Avaliable",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest3 = {
  "name": "Water Plates",
  "status": "Avaliable",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest4 = {
  "name": "Job Search",
  "status": "Avaliable",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest5 = {
  "name": "Vaccum Roomba",
  "status": "Avaliable",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest6 = {
  "name": "Restore Bathroom",
  "status": "Progress",
  "steps": ("Hey! I run the facilities here. It is time for ya cleaning session.", 
             "This week we'll cover the bathroom",
             "Make sure to wipe down the floors, and the sink. A little spray goes a long way",
             "Another area of choice is the bathtub. I tend to do the toilet too in pairs.",
             "I'd appreciate the help maintaining the facilities.",
             "Only the best for the queen. Oh, Thank for your help sugar, I really appreciate it. I'll see you next week!",
             "🌟 You gained: \n30 health \n20 enviroment points! \nexp 50")
}

quest7 = {
  "name": "Quest List 1.1",
  "status": "Done",
  "steps": ("Let's build a quest log!", 
             "First let's choose a data structure. A list or a dictionary.", 
             "A dictionary seems to be the best course of action! Don't forget to nest them so we can have a quest manager.",
             "Build a dictionary for quest with a questname, queststatus and queststeps",
             "You've now learned how to use dictionaries! Congradulations!.",
             "🌟 You gained: \n3 data cards \n3 bytes! \nexp 100",
             "Next: Perhaps add an inventory or add some badges next!")
}

quest8 = {
  "name": "Quest List 1.2",
  "status": "Done",
  "steps": ("Let's build a quest log with badges!", 
             "First we learned how to handle dictionaries and loops in python. Let's test that knowledge.", 
             "Add a loop that changes the lists' badges due to their progress.",
             "🤍 Closed, 🩵 Avaliable , 💛 In Progress , 💖 Done",
             "You've now upgraded your skills on how to use dictionaries and loops with python! Congradulations!.",
             "🌟 You gained: \n3 data cards \n3 bytes! \nexp 100",
             "Next: Perhaps add pre and post req. or add an inventory or external files next!"),
  "pre": [quest7]
}

# Quest Manager
quests = {
  "quest1" : quest1,
  "quest2" : quest2,
  "quest3" : quest3,
  "quest4" : quest4,
  "quest5" : quest5,
  "quest6" : quest6,
  "quest7" : quest7,
  "quest8" : quest8
  #"quest9" : quest9,
  #"quest10" : quest10,
  #"quest11" : quest11,
  #"quest12" : quest12,
  
}

#questnames = {
#  "Roger's apple" : quest1,
#  "Mays's Medicine" : quest2,
#  "Water Plates" : quest3,
#}
print("-- 💖 My Quests 💖 --")
print("🤍 Closed, 🩵 Avaliable , 💛 In Progress , 💖 Done\n")

# print keys,val as a list
#for x in questnames.keys():
#  print("🤍",x)
  
  
n = 1
global s
global g 
global x
g = "Avaliable"
  
# print Quest Names
for x in quests.keys():
  g = quests[x]['status'];
  
  if g == "Avaliable":
    s = "🩵 "
  elif g == "Progress":
    s = "💛 "
  elif g == "Done":
    s = "💖 "
  else:
    s = "🤍 "
  
  print(n,s,quests[x]['name'])
  n += 1
  




"""
sl = input("Select your Quest: \n",)
if sl == "1":
  global sell 
  sell = "quest1"
  print("You selected: ",quests[sell]["name"])
  
elif sl == "2":
  sell = "quest2"
  print("You selected: ",quests[sell]["name"])
else:
  print("null")
"""

n = input("\n-- Select your Quest: \n>",)
app = "quest"+n
print("You selected: ",s,quests[app]["name"])

a = quests[app]["name"]
b = quest1["steps"]
c = quest1.get("steps")

#print("---Quests ----1")
#print(d)
#print("-- Quest Name: ",a)

# print array as list
# for d in quest1['steps']:
#    print(d)

# ----- 1st
""" 
i = 0
while i < len(quest1['steps']):

  an = input("\nNext? (1) or Back? (2) or Close? (0) \n> ",)
  if an == "1":
      if i < len(quest1['steps'])-1:
          i = i + 1
          print(quest1['steps'][i])
      else:
          print("🟥 end of quest")
          break
  elif an == "2":
       i = i - 1
       print(quest1['steps'][i])
  elif an == 0:
    continue
  else:
     print("1 Finish")
     break
else:
    print("🟥 Done")
print("🟥 close")
i = 0
"""
print("---Quests ----")
print("Quest Name: ",s,quests[app]["name"])
thistuple = quests[app]["steps"]
print(thistuple[0])
#while a != 0:
    
#in = input("\nNext? (1) or Back? (2) or Close? (0) \n> ",)

# ----- 2nd

i = 0
while i < len(thistuple):
  an = input("\nNext? (1) or Back? (2) or Close? (0) \n> ",)
  if an == "1":
      if i < len(thistuple)-1:
          i = i + 1
          print(thistuple[i])
      else:
          print("🟥 end of quest")
          break
  elif an == "2":
       i = i - 1
       print(thistuple[i])
  elif an == 0:
    continue
  else:
     print("🟥 Finish")
     break
else:
    print("🟥 Done")
print("🟥 close")