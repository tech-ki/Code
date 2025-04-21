const o1 = {
    o2: {
        name: "Sourav",
        contact: {
            email: "sourav@example.com",
            phone: "123-456-7890"
        }
    }
};

const o4 = {
    "charname": "Ki",
    "age": "29",
    "startdate": "2025.03.10",
    "level":0,
    "active": true,
    "quest": 
    [
      {
        "name": "Luke the Security Guard",
        "level": 20,
        "task": "Get me 1 salad and kill 10 Strige Wings and 100 Junior Necki so I can make a present for my mother.",
        "steps": ["Salad 0/1", "Stirge Wings 0/10", " Junior Necki 00/100"],
        "item": {
            "Salad":1,
            "Stirge Wings":0,
            "Junior Necki":0
        }
      },
      {
        "name": "Madame Uppercut",
        "age": 39,
        "secretIdentity": "Jane Wilson",
        "powers": [
          "Million tonne punch",
          "Damage resistance",
          "Superhuman reflexes"
        ]
      },
      {
        "name": "Eternal Flame",
        "age": 1000000,
        "secretIdentity": "Unknown",
        "powers": [
          "Immortality",
          "Heat Immunity",
          "Inferno",
          "Teleportation",
          "Interdimensional travel"
        ]
      }
    ],
    "skill": [ //Something you can work towards to level up
      {
        "name": "Molecule Man",
        "age": 29,
        "secretIdentity": "Dan Jukes",
        "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
      },
      {
        "name": "Madame Uppercut",
        "age": 39,
        "secretIdentity": "Jane Wilson",
        "powers": [
          "Million tonne punch",
          "Damage resistance",
          "Superhuman reflexes"
        ]
      },
      {
        "name": "Eternal Flame",
        "age": 1000000,
        "secretIdentity": "Unknown",
        "powers": [
          "Immortality",
          "Heat Immunity",
          "Inferno",
          "Teleportation",
          "Interdimensional travel"
        ]
      }
    ],
    "step": [ //A small actionable thing you do
      {
        "name": "Brush Teeth",
        "exp": 202,
        "desc": "Brush your teeth to clean your bones.",
        "rep": "1/1",
        "last": [
            "2025.03.10 (1)"
        ],
        "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
      },
      {
        "name": "Check Mail",
        "exp": 39,
        "desc": "You've Got Mail!",
        "rep": "1/7",
        "last": [
          "2025.03.10 (1)",
        ]
      },
      {
        "name": "Eternal Flame",
        "age": 1000000,
        "secretIdentity": "Unknown",
        "powers": [
          "Immortality",
          "Heat Immunity",
          "Inferno",
          "Teleportation",
          "Interdimensional travel"
        ]
      }
    ]
  }

// Using dot notation
//console.log(o1.o2.contact.email); 
console.log("\nname:  "+o4.charname); 
console.log("quest:  "+o4.quest[0].name); 
console.log("task:  "+o4.quest[0].steps); 
o4.level += 1
o4.quest[0].item.Salad +=1

console.log("You are now level:  "+o4.level); 
console.log("You now have item Salad:  "+o4.quest[0].item.Salad); 
console.log(o4.quest[0]); 

// Using bracket notation
//console.log(o1["o2"]["contact"]["phone"]); 

