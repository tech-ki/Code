
import datetime
print("Today is")

# Status of decay
class home:
    a = datetime.datetime.now()
    due = 5
    thing = "showed"
    next = 2
    
    job01 = { 
        "title": "DOing the jobb" ,
        "job": "Real Time Software Developer",
        "location" : "Florida, USA",
        "posted": "2023.11.27",
        "remote?": "yes",
        "clearence":"Security clearence",
        "level": "senior",
        "exp":"09 years",
        "degree":"bachelors",
        "salary":"$125,000 - $150,000",
        "skills":["Linux","C++",'real time linux',"GitLab"],
        }
    
    thing = { 
        "title": "DOing the thing" ,
        "area": "health",
        "thing" : "floss",
        "last": "today",
        "next": "02" }
    b = """DOing the thing
    area: health
    thing: floss teeth
    last: today
    next: 03 days\n--"""
    
    c = """DOing the thing
    area: code
    thing: code in python
    last: today
    next: 01 day\n--"""
    
    d = """DOing the thing
    area: code
    thing: IBM Cloud > Web Application Course
    last: 14 days ago
    next: 00 days
    status: !! needed \n--
    """
    e = """DOing the thing
    area: music
    thing: Music Theory - Chord C
    last: 14 days ago
    next: 00 days
    status: <3 want \n--
    """
    things = {
        "thing": thing, 
        "b" : b,
        "c" : c,
        "d" : d,
        "e": e
        
    }
    status = """Status Update:
    good: 3
    next: 2
    needed: 5
    areas: 
    - code(02) - music (02)-  art (01) - health (04)  - clean (03) - business (04)
    wants: 101
    rest: 1323
    --""" 
    wants = """I want
    coding job
    calendar app
    notetaking app
    massage
    aquarium
    VR Headset
    Maplestory
    Swimming
    Rock Climbing
    Animation
        - sailor moon
        - spinning quarter
    Blender
        - Ocean
        - Character jump
    """
    needs = """I need
    shower
    clean bedsheets
    hang up clothes in closet
    healthy food
    Dentist Appointment
    A Nap
    Yoga
    """

    print(a)
    print(a.strftime("The day of the year is ""%j out of 365"))
    print(a.strftime("There are""%j - 365 days left in this year"))
    
    print("This note is due",due)
    print("--\nIt has been",due,"days since you have",thing)
    print("This is due within the next",next,"days\n--")
    print(b)
    print(c)
    print(d)
    print(e)
    print("You are good in 7 areas with 11 things. :D")
    print("You are needed in 2 areas for 10 things.")
    print("You are wanted in 17 areas with 102 things.")
    print("--\n",status,"\n--")

    #print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m")
    
    #dictionary = key:value
    print(job01["job"])
    my = input("My (enter n = needs, w = wants, s = status, t = things), j = job list\n")
    if my == "s":
        print("My status is ",status)
    elif my == "w":
        print("My wants are ",wants)
    elif my == "n":
        print("My needs are ",needs)
    elif my == "j":
        for x, y in job01.items():
            print(x, ":", y)
    elif my == "t":
        for x, y in things.items():
            #print(x)
            #print(things.values()) - prints the second values
         print(x,":", y)
            #print("My list of things are ",things)
    else:
       print("Please select a correct option.")
    
    print("Hello")    
    #print(things["b"]["area"])
    #print("My Status\n",status)
    #print("My Needs \n",needs)

# colorspep8.py
def colors_16(color_):
    return("\033[2;{num}m {num} \033[0;0m".format(num=str(color_)))


def colors_256(color_):
    num1 = str(color_)
    num2 = str(color_).ljust(3, ' ')
    if color_ % 16 == 0:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
    else:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m")