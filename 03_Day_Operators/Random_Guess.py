#guess numbers?
import random

print('Your Name!')
name = input()

print(f'Well! {name} I am thinking of number between 1 to 20.')
ranNum = random.randint(1, 20)

for guesses in range(1, 7):
    print('Take a guess?')
    guess=int(input())

    if guess < ranNum:
        print('Your guess is too low!')
    elif guess > ranNum:
        print('You guessed higher!')
    else:
        break

if guess == ranNum:
    print('Good Job ' + name + '.You guessed it in  '+ str(guesses) + ' guesses.')
else:
    print('Sorry! you could not guess it right! The number guessed was ' + str(ranNum) + '.')


