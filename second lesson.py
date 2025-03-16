import random

top_of_range = input('type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number greater than 0 next time:)')
        quit()

else :
    print('please type a number this time. ')
    quit()


random_number = random.randint(1,100 )

guesses = 0

while True:
    guesses += 1
    your_guess = input ("make a guess:")

    if your_guess.isdigit():
        your_guess = int(your_guess)
    else:
        print('please type a number this time. ')
        continue

    if your_guess == random_number:
        print('you got it!')
        break

    else:
        if your_guess> random_number:
            print('you are above the number')
        else:
            print('you were below the number')

print('you got it in ' , guesses, "guesses , well done!")

another_round = input ('do you want to play again?')

if another_round !="yes":
    quit()

print('okay lets play !')

random_number = random.randint(1,100 )

guesses = 0

while True:
    guesses += 1
    your_guess = input ("make a guess:")

    if your_guess.isdigit():
        your_guess = int(your_guess)
    else:
        print('please type a number this time. ')
        continue

    if your_guess == random_number:
        print('you got it!')
        break

    else:
        if your_guess> random_number:
            print('you are above the number')
        else:
            print('you were below the number')

print('you got it in ' , guesses, "guesses , well done!")