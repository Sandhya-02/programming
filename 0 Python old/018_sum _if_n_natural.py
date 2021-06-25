"""
sum of n natural numbers 

program would be like this 
enter how many numbers u want to print
input : 10
output : 1 2 3 4 5 6 7 8 9 10
output : sum of 10 natural numbers = 1+2+3+.....+10
"""
# num = int(input("enter the number"))
sum = 0
for i  in range(1,11):
    sum = sum+i 
print(sum)

