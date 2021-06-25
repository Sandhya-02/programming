"""puppy ki health baledu 
so you keep calling a hospital several tyms
they picked up your call on the 9th attempt
after the pick your call you'll 
inform them about your sitution and book
an appointment to the doctor """

# n = int(input("enter how many times u want to call "))
# for i in range(n):
#     i=i+1
#     print("called ",i)
#     if(i==9):
#         break
# print("call is answered at ",i)
# print("i would like to book an appointment for my baby puppy")


n = int(input("enter how many times u want to call "))
for i in range(n):
    print("value of i is ",i)
    i=i+1
    print("value of i = i+1 is ",i)
   
    if(i==9):
        print("after running i==9 i value is ",i)
        break
print("call is answered at ",i)
print("i would like to book an appointment for my baby pup")