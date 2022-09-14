#Write your code below this line 👇
def prime_checker(number):
    if number ==2 or number == 3:
        print(f'{number} is a prime number.')
    elif number %2 == 0 or number %3 == 0:
        print(f'{number} is a NOT prime number')
    else:
        print(f'{number} is a prime number.')

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



