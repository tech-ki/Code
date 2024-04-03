print("hello")

print('Enter your name:')
x = input()
print('Hello, ' + x) 

level = 0;
exp = 0;
fin = 1
### 
# i = 0
# while i < 6:
# i += 1
# if i == 3:
# print("You have mastered it!!")
# break
# print(i)
  
while fin > 0:
      if level == 0 and exp <= 10:
          nu = int(input(print("Do the thing?")))
          exp = exp + nu;
          print("Gained",exp,"exp points")
          
      elif exp > 10 and level == 0:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;
           
      elif level == 1 and exp <= 20:
          nu = int(input(print("Do the thing?")))
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;
          
      elif level ==1 and exp >= 20:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
     
      elif level == 2 and exp <= 40:
          nu = int(input(print("Do the thing?")))
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;
                
      elif level ==1 and exp >= 20:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
      
      elif level ==2 and exp >= 40:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
      
      elif level == 3 and exp <= 60:
          nu = int(input(print("Do the thing?")))
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;
      
      elif level ==3 and exp >= 60:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          
      elif level == 4 and exp <= 80:
          nu = int(input(print("Do the thing?")))
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;      
          
      elif level ==4 and exp >= 80:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
      
      elif level == 5 and exp <= 100:
          nu = int(input(print("Do the thing?")))
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          exp = exp + nu;
          
      elif level ==5 and exp >= 100:
          level+=1
          print("You are now level!",level)
          print("Gained",exp,"exp points")
          print("You have mastered it!!")
          fin = 0;
      
      
      
      
      