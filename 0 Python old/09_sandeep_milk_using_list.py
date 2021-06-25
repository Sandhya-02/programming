"""
mummy and sandeep went for shopping
sandeep trolley lo [eggs , meat,small milk packet, bread,jam,] teskocchadu
mummy said get big milk packet 
sandeep small milk packet ni teesesi big milk packet bag lo pettukunnadu 

"""
list = ["eggs","meat","small milk packet","bread","jam"]
print(list)
if "small milk packet" in list:
    list.remove("small milk packet")
    """ del(4) pop(3)"""

    list.append("big milk packet")
    """ insert """
    print("after removing small milk packet =",list)



    