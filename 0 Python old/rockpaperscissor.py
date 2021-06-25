print("press ",0,"rock ")
print("press ",1,"paper ")
print("press ",2,"scissors ")
player_jack = int(input("enter the number from 0,2:"))
items=["rock","paper","scissors"]
import random
sandhya_input = random.randrange(0,2)
print(items[player_jack],"selected by player")
print(items[sandhya_input],"selected by computer") 
if player_jack==0 and sandhya_input==1:
    print("sandhya winner")
elif player_jack==1 and sandhya_input==0:
    print("player winner")
elif player_jack==1 and sandhya_input==2:
    print("sandhya winner")
elif player_jack==2 and sandhya_input==1:
    print("player winner")
elif player_jack==0 and sandhya_input==2:
    print("player winner")
elif player_jack==2 and sandhya_input==0:
    print("sandhya winner")
else:
    print("both are winner")

