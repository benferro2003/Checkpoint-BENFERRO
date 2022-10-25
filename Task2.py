#!/usr/bin/env python3
if __name__ == '__main__':
    print('Checkpoint task 2 - BEN FERRO')
    slices = int(input('How many slices of spam one requires?'))
    while slices < 1:
        slices = int(input('How many slices of spam one requires?'))

    spam = 'spam, '
    if slices == 2:
        print(f'Egg with {spam}, and spam coming up!')
    elif slices == 1:
        print(print(f'Egg with {spam} coming up!'))

    else:
        print(f'Egg with {spam * (slices-1)}and spam coming up!')
