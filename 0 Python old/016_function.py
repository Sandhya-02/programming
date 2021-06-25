first = int(input("enter the number  "))
second = int(input("enter the number  "))
 

select =int(input("press 1 to add\n press 2 to sub\n press 3 to mul \n press 4 to div\n "))
print ("what do u want to do\n")

if (select == 1):
    sum = first+second
    print(first,second," = ",sum)
if (select == 2):
    sub = first-second
    print(first, second," = ",sub)
if (select == 3):
    mul = first*second
    print(first, second," = ",mul)
if (select == 4):
    div = first/second
    print(first, second," = ",div)
     



# def add():
#     a,b=getinput()
#     return a+b
# def sub():
#     a,b = getinput()
#     return a-b
# def mul():
#     a,b = getinput()
#     return a*b
# def div():
#     a,b = getinput()
#     return a//b
