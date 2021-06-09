
import math

def calculate_area_of_circle(radius):
    area=math.pi*(radius*radius)
    print("%.2f" % area)
calculate_area_of_circle(6)

def area_of_cylinder(radius,height):
    area=math.pi*(radius*radius)*height
    print("%.2f" %area)
area_of_cylinder(23,34)
player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Okay! ' + player_name + ' I am Guessing a number between 1 and 100')
for number in range(1, 10):
    while number == 10:
        number_of_guesses = int(input())
    number += 1
    if number_of_guesses > number:
        print('Your guess is too low')
    elif number_of_guesses > number:
        print('Your guess is too high')
    elif number_of_guesses >= number:
        print("your guess is with the range")
        break
    elif number_of_guesses >= number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))
