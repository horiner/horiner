from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemise[current_enemy]
    enemy_hp = enemise[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    print()

def shop():
    print('Добро пожаловать, странник! Что тебе требуеться?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if item in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    else:
        print(f'Кладите {value["price"]} монеты в мешок.')



