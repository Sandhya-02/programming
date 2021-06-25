
#! sandhya went to bar with jack to buy a drink
#! drinks are [redwine,cocktail,whiskey,vodka,beer with green bottle]
#! but sandhya dont like to drink beer she want to replace with magicmoment
#! sandhya shooting on jack plz replace it hahhaha let is;

list = ["redwine","cocktail","whiskey","vodka","beer with green bottle"]
print(list)
if "beer with green bottle" in list:
    list.remove("beer with green bottle")
    list.append("magic moment with violet bottle")
    print("after removing of a beer with green bottle=",list)