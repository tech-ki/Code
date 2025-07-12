
import qst

#questnames = {
#  "Roger's apple" : quest1,
#  "Mays's Medicine" : quest2,
#  "Water Plates" : quest3,
#}
print("\n-- 💖 My Quests 💖 --")
print("🤍 Closed, 🩵 Avaliable , 💛 In Progress , 💖 Done")
print("Type 'c' to see closed quests\n") 

# print keys,val as a list
#for x in questnames.keys():
#  print("🤍",x)
  
  
n = 1
global s
global g 
global x
g = "Avaliable"
  
# print Quest Names
for x in qst.quests.keys():
  g = qst.quests[x]['status'];
  
  if g == "Avaliable":
    s = "🩵  "
  elif g == "Progress":
    s = "💛 "
  elif g == "Done":
    s = "💖 "
  else:
    s = "🤍 "
  
  # Print all but closed quests
  if s != "🤍 ":
    if s == "🩵  ":
      print(n,s,qst.quests[x]['name'])
      n += 1
    elif s == "💛 ":
      print(n,s,qst.quests[x]['name'])
      n += 1
    elif s == "💖 ":
      print(n,s,qst.quests[x]['name'])
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
n = input("\n-- Select your Quest: \n> ",)
if n == "c": #Closed
  n = "1"
  a = 0
  s = "🤍"
  app = "quest"+n
  
  # Archived
  print("Here are your archived quests: ")
  for x in qst.quests.keys():
   if qst.quests[x]['status'] == "Closed":
    print(a,s,qst.quests[x]['name'])
    a += 1
    quit()
  
else:
  app = "quest"+n
  print("You selected:",s,qst.quests[app]["name"])
  
  #Books
  if qst.quests[app]["type"] == "book":
   print("This is a book!")
   #print(a,s,qst.quests[x]['name'])
   #a += 1
  else:
   print("Not a book!")

a = qst.quests[app]["name"]
b = qst.quest1["steps"]
c = qst.quest1.get("steps")

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
print("Quest Name:",s,qst.quests[app]["name"])
thistuple = qst.quests[app]["steps"]
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