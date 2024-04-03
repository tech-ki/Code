# Create an array of levels
curr = 0;
A = 0;
B = 1;

class level:

    item = str(input("Enter an item: "))
    B = int(input("Enter a level: "))
    diff = B - A;
    
    print("The",item,"skill is level",B)
    print("\nMy current level is ",curr)
    print("I need",diff,"more levels to reach here.")
    print("Practice these items to level up!")
    
    skills = {
        1:"python",
        2:"teeth",
    }
    
    items = {
        "python": "1", 
        "html" : "2",
        "css" : "5",
        "c" : "0",
        "java": "2"    
    }
    skill1 = {
        "name":"python",
        "level":2
    }
    
    skill2 = {
        "name":"css",
        "level":4
    }
    
    skills = {
        "skill1":skill1,
        "skill2":skill2
    }
    
    
    skills["skill1"].update({"level": 3})
    print("Congrats!! Your",skills["skill1"]["name"],"skill has leveled up!!")
    
    print("Skill:",skills["skill1"]["name"],"is level",skills["skill1"]["level"])
    
    print("Skill:",skills["skill2"]["name"],"is level",skills["skill2"]["level"])
    
