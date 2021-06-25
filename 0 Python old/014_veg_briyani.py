

"""
if anitha and laxman went to resturent
and there order chicken briyani 
kani egg briyani teskochadu 
boy ne pillusthe sorry ani chptadu 
oddhu ani anukonii there will adjust with mango juices
"""
print("anitha and laxman went to resturent")
food_order = str(input())
if (food_order == "yes"):
    print("chicken briyani")
    not_order = str(input())
    if(not_order == "yes"):
        print("egg briyani")
    else:
        print("sorry sir/madam i will change the order")
else:
    print("mango juice")



