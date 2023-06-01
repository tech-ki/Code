'''
Created on Sep 20, 2021

@author: ciarraw
'''

if __name__ == '__main__':
    pass

def cheer_up(times : int) -> None:    
    for i in range(1,times+1):
        print('You will become a great programmer'+i*'!')
        
sadness = input('Enter number indicating how sad you are \n')
cheer_up(int(sadness))