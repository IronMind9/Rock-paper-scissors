#start the game 
#get the user answer (rock or paper or scissors)
#ask the computer to get random answer of these 
#if (user == rock and pc == scissors or user == scissors and pc == paper or user == paper and pc == rock ) so user win 
#otherwise case pc win / user lose! 
import random

player = input("chose between : 'rock' or 'scissors' or 'paper' : \n ")

pc = random.choice(['rock' , 'paper' , 'scissors' ])
 
print(f"pc choosed : {pc}" )

if (pc == player):
    print ("I'ts a Tie ! ")
    
elif(player == 'rock' and pc == 'scissors' or player == 'scissors' and pc == 'paper'or player == 'paper' and pc == 'rock'): 
    print (" Player win !") 
    
else : 
    print ("You lose !")  