
# List all Quests & Quest Manager Here!
q1 = ("apple", "banana", "cherry","dog",4,5,6,7,8,9)
q2 = ("💖 Quest Avaliable - Roger's apple", 
             "Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")

# -- List Quests & Details
quest0 = {
  "name": "Closed",
  "status": "Closed",
  "type": "quest",
  "steps": ["red", "white", "blue"]
}

quest1 = {
  "name": "Roger's apple",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest2 = {
  "name": "Restore Bones",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("Hey! I'm a miner!", 
             "I see you have a gold mine here! You have to make sure you protect it. Defenses go down every 24 hours. Comolete these tasks to restore the bass.",
             "Wash you teeth, Mine between them, and mouthwash it to seal it in. Come back here when your done!",
             "Congradulations! Defenses are back up! I will call you again when defenses are low again. This gold is priceless! make sure to keep it safe from the rats trying to eat at it!"
             "\n🌟 You gained: \n30 defense \nexp 50")
}

quest3 = {
  "name": "Python Outside",
  "status": "Done",
  "type": "quest",
  "steps": ("Hey! This file is getting pretty big! Let's see what we can do about that..", 
             "Python modules are python files you can run outside of a file and share amongst the files. You simply import the file and run the modules within it by calling it..",
             "You've now learned how to use modules! Here's a gift! You're getting along so well!!",
             "🌟 You gained: \n3 data cards \n3 bytes! \nexp 100")
}

quest4 = {
  "name": "Job Search",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("Hey! I'm the instuctor here to teach you a lot of things.", 
             "Let's have some fun.", "Surprise! If your HP drops to 0, its a huge problem. Now i'll give you a Roger's Apple to recover your health. Open your inventory and by pressing 'I' and eat it.",
             "You've now learned how to use items! Here's a gift for your travels. Use it when you are in a pinch.",
             "🌟 You gained: \n3 apple \n3 green apple! \nexp 10")
}

quest5 = {
  "name": "Vaccum Roomba",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("Hey! Got alot of dust critters roaming about now.", 
             "Let's tidy up a bit. Run the roomba 2 times, 1 for upstairs and 1 for downstairs. Don't forget the Fabuloso for fragrance. Lavendar is quite lovely.",
             "You've now learned how to clean the floors! Here's a gift for your hardwork",
             "🌟 You gained: \n3 vaccs \nexp 20")
}

quest6 = {
  "name": "Restore Bathroom",
  "status": "Progress",
  "type": "quest",
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
  "type": "quest",
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
  "type": "quest",
  "steps": ("Let's build a quest log with badges!", 
             "First we learned how to handle dictionaries and loops in python. Let's test that knowledge.", 
             "Add a loop that changes the lists' badges due to their progress.",
             "🤍 Closed, 🩵 Avaliable , 💛 In Progress , 💖 Done",
             "You've now upgraded your skills on how to use dictionaries and loops with python! Congradulations!.",
             "🌟 You gained: \n3 data cards \n3 bytes! \nexp 100",
             "Next: Perhaps add pre and post req. or add an inventory or external files next!"),
  "pre": [quest7]
}

quest9 = {
  "name": "Mono Font",
  "status": "Done",
  "type": "quest",
  "steps": ("I want a monospaced font to use for my ipad coding terminal.", 
             "Let's create a custom version of my favorite font nunito. 1st, lets try Fontforge. None of these options work for me,let's try something else.",
             "2nd. let's try to use FontLab. I adjusted the weight spacing but it still isn't working properly. Let's try something else.",
             "3rd. This time i'm using a web font editor named Glyphor Studio. I can change the spacing globally across letters then change the position of the spacing for each one! This one works!",
             "I imported it into FLStudio and changed the terminal and editor font and it works!",
             "You've now learned create a monospaced font! Great job! I know this has been on your mind for a while. Here's a gift for your hardwork",
             "🌟 You gained: \n3 style points \nexp 100")
}

quest10 = {
  "name": "Teacher Ms. Ki",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("I love to teach. I love the understanding that happens.", 
             "Let's create a custom version of my favorite font nunito. 1st, lets try Fontforge. None of these options work for me,let's try something else.",
             "2nd. let's try to use FontLab. I adjusted the weight spacing but it still isn't working properly. Let's try something else.",
             "3rd. This time i'm using a web font editor named Glyphor Studio. I can change the spacing globally across letters then change the position of the spacing for each one! This one works!",
             "I imported it into FLStudio and changed the terminal and editor font and it works!",
             "You've now learned create a monospaced font! Great job! I know this has been on your mind for a while. Here's a gift for your hardwork",
             "🌟 You gained: \n3 style points \nexp 100")
}

quest11 = {
  "name": "Lush Hair",
  "status": "Avaliable",
  "type": "quest",
  "steps": ("I love to teach. I love the understanding that happens.", 
             "Let's create a custom version of my favorite font nunito. 1st, lets try Fontforge. None of these options work for me,let's try something else.",
             "2nd. let's try to use FontLab. I adjusted the weight spacing but it still isn't working properly. Let's try something else.",
             "3rd. This time i'm using a web font editor named Glyphor Studio. I can change the spacing globally across letters then change the position of the spacing for each one! This one works!",
             "I imported it into FLStudio and changed the terminal and editor font and it works!",
             "You've now learned create a monospaced font! Great job! I know this has been on your mind for a while. Here's a gift for your hardwork",
             "🌟 You gained: \n3 style points \nexp 100")
}


# Chapters
bk2ch1 = {
  "steps" : "This is Chapter 1."
   
}

# Books
book1 = {
  "name": "The Musician's Guide to Theory and Analysis",
  "status": "Avaliable",
  "type": "book",
  "chapter": "1",
  "steps": ("There are 6 Parts and 37 Chapters to this college level music theory book.", 
             "Select by Part or Chapter",
             "2nd. let's try to use FontLab. I adjusted the weight spacing but it still isn't working properly. Let's try something else.",
             "3rd. This time i'm using a web font editor named Glyphor Studio. I can change the spacing globally across letters then change the position of the spacing for each one! This one works!",
             "I imported it into FLStudio and changed the terminal and editor font and it works!",
             "You've now learned create a monospaced font! Great job! I know this has been on your mind for a while. Here's a gift for your hardwork",
             "🌟 You gained: \n3 style points \nexp 100")
}

bk2ch2 = {
  "steps": ("This is Chapter 2.",
            "To be announced.")
}

book2 = {
  "name": "Internet & World Wide Web - How to Program",
  "status": "Avaliable",
  "type": "book",
  "chapter": bk2ch1,
  "steps": ("There are 29 Chapeter in this college level web development textbook. This book was reccomended by Saint Leo University.", 
             "Select by Part or Chapter",
             "This feature is under construction.",
             "Goal: Select chapter, select section, read text, Add quizes?, ",
             "I imported it into FLStudio and changed the terminal and editor font and it works!",
             "Please come back later! ",
             bk2ch2["steps"],
             "🌟 You gained: \n3 style points \nexp 100")
}


books = {
  "book1":book1,
  "book2":book2
}

#print(myfamily["child2"]["name"])
chapters = {
  
}


# Quest Manager
quests = {
  "quest0" : quest0,  
  "quest1" : quest1,
  "quest2" : quest2,
  "quest3" : quest3,
  "quest4" : quest4,
  "quest5" : quest5,
  "quest6" : quest6,
  "quest7" : quest7,
  "quest8" : quest8,
  "quest9" : quest9,
  "quest10" : quest10,
  "quest11" : quest11,
  "quest12": book1,
  "quest13": book2
  #,"quest11" : quest11
  #,"quest12" : quest12
  
}

