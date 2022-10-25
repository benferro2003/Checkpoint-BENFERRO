#!/usr/bin/env python3
def title():
    name = input('Enter thy Name!')
    if name.startswith('Lord') or name.startswith('Lady'):
        print(f'It shall be so, {name}!')
    else:
        print(f'You may not be known by that name!')


if __name__ == '__main__':
    print('Checkpoint task 1 - BEN FERRO')
    title()
