import random

numbers=random.randint(10,100)
user_play=input("Write your name.")
numbers_of_gueses=0
print('Welcome ' + user_play + ' I hope you will guess the numbers from 1..100 ')

while numbers_of_gueses < 100:

    gueses = int(input())
    numbers_of_gueses += 1
    if gueses > numbers:
        print("Your guese is too low try again")
    elif gueses < numbers:
        print('Your gueses are within the range')
    else:
        break
if gueses == numbers:
    print('You have  guessed the number ' + str(numbers_of_gueses) + ' trial!')
else:
    print('You have not guased the numbermart ' + str(numbers))
