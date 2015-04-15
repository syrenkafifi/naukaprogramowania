# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import random

lista_par = [
    ('OORO', 'OROO'),
    ('OROO', 'ROOO'),
    ('ROOO', 'OORO')
]

wyniki_par = [
        {
            'gracz_1': 0,
            'gracz_2': 0,
        },
        {
            'gracz_1': 0,
            'gracz_2': 0,
        },
        {
            'gracz_1': 0,
            'gracz_2': 0,
        }
]

penney = ['O', 'R']

for i in range(0,3):
    for j in range(0,1000):
        wygrana = False
        ciag = ''
        while not wygrana:
            ciag+=(random.choice(penney))
            okno = ciag[-4:]
            if okno == lista_par[i][0]:
                wyniki_par[i]['gracz_1']+=1
                wygrana = True
            if okno == lista_par[i][1]:
                wyniki_par[i]['gracz_2']+=1
                wygrana = True

print 'WYNIKI'

for i in range(0,3):
    print 'PARA ' + str(i) + ' - gracz_1: ' + str(wyniki_par[i]['gracz_1'])+'    - gracz_2: ' + str(wyniki_par[i]['gracz_2'])
