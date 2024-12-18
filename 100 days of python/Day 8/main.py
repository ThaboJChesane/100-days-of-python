#Write your code below this line 👇
from operator import truediv


def prime_checker(number):
    check = True
    for x in range(2, number):
        if number % x == 0:
            check = False
    if check:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)