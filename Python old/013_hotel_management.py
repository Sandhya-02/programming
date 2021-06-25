"""
hotel  lo guests ostuu unnaru 
valla names record cheskoni oka list  create cheyali
vellipoye guests names seperate list lo record cheyali

oka guest appude recetion daggaraki occhi join ayyi 
ventane cancel my reservation annadu  (delete the guy from old list)
"""

# bookings = []
# print(bool("would you like to book a room"))
# if  True:
#     book = input
#     bookings.append(book)
#     print("people present in hotel = ",bookings)
#     checkout=[]
#     print(bool("meeru dobbeddam anukuntunnara"))
#     if True:
#         checking_out  = input)
#         checkout.append(checking_out)
#         print("people who checked out = ",checkout)

bookings = []
answer = str(input("would you like to book a room"))
print(answer)
if answer == "yes":
    book = str(input("please tel us your name"))
    bookings.append(book)
    print("people present in hotel = ", bookings)

    checkout = []
    answer = str(input("would you like to checkout"))
    print(answer)
    if answer == "yes":
        checkout_person = str(input())
        checkout.append(checkout_person)
        print("people who checked out = ", checkout)
else:
    print("thank you for visiting ")
