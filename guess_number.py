from random import randint

number = randint(1, 100)
while True:
    guess = int(input('Number: '))
    if guess == number:
        print('Отличная интуиция! Вы угадали число :)')
        break
    elif guess < number:
        print('Ваше число меньше того, что загадано')
    else:
        print('Ваше число больше того, что загадано')
    # dkfjskdjfk