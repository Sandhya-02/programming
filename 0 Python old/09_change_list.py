# dreamers = ["manasa","tanusree","karishma "]
# dreamers[2] = "sandhya mama"
# print(dreamers)   

# earth = ["sun","moon","sky","jack","sandhya"]
# earth[3:5] = ["manasa","tanusree"]
# print(earth)

# earth = ["sun","moon","sky","jack","sandhya"]
# earth[1:3] = ["manasa","abc","edf"]
# print(earth)

# earth = ["sun","moon","sky","jack","sandhya"]
# earth.insert (3,"manasa")
# print(earth)

# num = [11,12,13,14,15]
# sum =  num[0]+num[1]
# num.insert(0,sum)
# print(num)

# num = [11,12,13,14,15]
# sum =  num[0]+num[1]
# num.insert(0,sum)
# print(num)

# insert
# del
# pop
# extend
# replace
# remove

# list = ["a","m","d","c","e"]

# del list[1]
# print("after deleting m",list)

# list.insert(1,"sandy mama")
# print("after inserting sandy mama",list)

# list.pop(2)
# print("after popping a",list)

# list1=["red","hot red","light red","pale red"]
# list.extend(list1)
# print("after using extend ",list)

# list.remove("c")
# list.remove("e")
# print("after removing e and c",list)
# list.remove("a")

# list.insert(1,"loves")
# print("after inserting loves ",list)

name = ["jack ","manasa ","tanusree ","karishma "]
character = ["naughty ","hot girl","soft looking","clam girl"]
types = ["hot girls to kiss ","hot guy to date like jack ","good guy like jack ","handsome guy to use like a jack "]
#!jack is a naughty guy and he want a hot girls to kiss
print(name[0],"is a",character[0],"guy and he want a",types[0])
#! manasa is a hot girl and she is searching for a hot guy to date like jack
print(name[1], "is a",character[1],"and she is searching for a",types[1])
#! tanusree is a soft looking but she use a good guy like jack
print(name[2], "is a",character[2],"but she use a",types[2])
#!karishma is a clam girl but she need a handsome guy to use like a jack
print(name[3], "is a ",character[3], "but she need a ",types[3])








list = [ 1, 2, 12, 45, 789, "raj" ]

print ("starting :",list)

del list[0]
print(list)

list.pop(3)
print(list)

a = list.pop(2)
print ("Deleted value is : ",a)
print(list.pop(2))
print ("Final list :",list)


list = ['jack','raj','sri']
print(len(list))