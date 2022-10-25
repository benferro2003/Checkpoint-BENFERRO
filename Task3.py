#!/usr/bin/env python3
if __name__ == '__main__':
    print('Checkpoint task 3 - BEN FERRO')
    password = 'banana'
    guess = input('Greetings! What is the password?')
    while guess != password:
        print('incorrect! you may try again.')
        guess = input('Greetings! What is the password?')
    print("Correct! You may enter.")
