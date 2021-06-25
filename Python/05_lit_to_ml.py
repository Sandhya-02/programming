
#! liters to ml
#! 1 lit = 1000ml
# lit=2
# mil = lit * 1000
# print("mil =" ,mil)
#! one kid came to shop, shop guy can convert ml to lit and lit to ml
#! shop guy asks the kid "denloki convert cheyali"
#! kid gives him input and gets the output

name= input("em convert cheyali")

if name =="ml":
    value= float(input("yenni ml ni convert cheyali"))
    lit= value/1000
    print("lit =",lit)
elif(name=="lit" ):
    value= float(input("yenni liters ni convert cheyali"))
    ml= value*1000
    print("ml = ",ml)
else:
    print("sarigga adugu ra babu")
