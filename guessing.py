from sys import argv,exit
from random import randint


def function1(guess, answer, a, b):
    if a <= guess <= b:
        if guess == answer:
            print(f'Congrats! {guess} was the number')
            return True
        else:
            print('Wrong!')
    else:
        print(f'try between {a} and {b}')
        return False
if __name__ == '__main__':
    try:
        a = int(argv[1])
        b = int(argv[2])
    except:
        print('Usage: guessing.py number[start] number[end]')
        exit()

    answer = randint(a, b)
    print(answer)

    while True:
        try:
            user_guess = int(input(f'Try guess the number between {a} and {b}: '))
            if(function1(user_guess,answer,a,b)):
                break
        except ValueError:
            print('Try guessing a number')
            continue



