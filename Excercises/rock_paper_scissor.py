"""
implement a roack paper scissor game

user with computer (random generated)

0 -> rock           wins against scissors
1 -> paper          wins against rock
2 -> scissor        wins against paper

total cases = 9 
user    ,    computer , results
0               0       draw
0               1       computer wins
0               2       user wins
1               0       user wins
1               1       draw
1               2       computer 
2               0       computer
2               1       user
2               2       draw


"""

import random 

user_input = int(input("Enter 0,1 or 2 for rock,paper or scissor respectively:  "))

comp_input = random.randint(0,2)

game_pics = ['✊' , '🖐️' ,  '✌️' ]



if (user_input < 0 or user_input > 2) :
    print("invalid input")

else :
    print(f"user entered  {user_input} for {game_pics[user_input]}")
    
    print(f"computer choose {comp_input} for {game_pics[comp_input]}")
    
    if (user_input==comp_input):
        print("draw ⚖️")

    elif (( user_input == 0 and comp_input ==2 ) or ( user_input == 1 and comp_input ==0 ) or ( user_input == 2 and comp_input == 1 )) :
        print(" you win 🏆")
    else :
        print("you loose 💀 ")