#!/usr/bin/env python3
import random

if __name__ == '__main__':
    print('Checkpoint task 5 - BEN FERRO')

    """Josh helped me with this"""

    deck = ['8S', '65', 'TD', 'KC', 'TC', 'AH', '3H', 'AS', 'JS', '5C', '2D', '4D', 'AC',
            'TH', 'KH', '2S', '8C', '6H', '6C', '8D', '2C', 'JH', '4H', 'KD', '3S', 'AD',
            '2H', '7D', '5D', '9D', '4S', '5H', 'TS', 'JC', '7C', 'QH', '3D', 'QC', '7H',
            '5S', 'QD', '9S', '3C', '9C', 'QS', '4C', '9H', '8H', '6D', 'KS', 'JD', '7S']

    random.shuffle(deck)

    North = deck[1:13]
    South = deck[13:26]
    East = deck[26:39]
    West = deck[39:52]

    print(f'North --> {", ".join(North)} \nSouth --> {", ".join(South)} \nEast --> {", ".join(East)} \nWest --> {", ".join(West)}')

    print("Looking for the Ace of Spades")
    if 'AS' in North:
        print('North Player has It')

    if 'AS' in South:
        print('South Player has It')

    if 'AS' in East:
        print('East Player has It')

    if 'AS' in West:
        print('West Player has It')

    print(f'\n=====\n')
