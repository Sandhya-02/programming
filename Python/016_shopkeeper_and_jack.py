"""
jack asked  u to go to  shop and get eggs
since its  afternoon the shopkeeper is sleeping 
u need to knock the door 6 times to wake him up 

shop said he has only donkey eggs
you need to call jack to inform the issue
but jack will only pick the call if it rangs 3 times 

after jack answered the call he says bring two donkey eggs one for u and one for me

"""

num = int(input("jack asked me to go to shop to gets eggs "))
for i in range(6):
    i = i+1
    print("shop keeper not open the door ",i)
    if(i==6):
        break
print("finally opened the door at 6 time")
shop = str("donkey_eggs")
print("shope_keeper has only " ,shop)
call = int(input("call to jack"))
for i in range(3):
    i = i+1
    print("called to idoit jack and not attempted at ",i)
    if(i ==3):
        break
print("finally attempted the call at 3 time")
print("okay said to bring 2 donkey eggs 1 for jack and 1 for her close one tanusree")