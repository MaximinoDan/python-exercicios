'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO'.'''

cid = str(input('Digite em que cidade você nasceu? ')).strip()

print(cid[:5].upper() == 'SANTO')