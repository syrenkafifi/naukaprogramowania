# -*- coding: utf-8 -*-
#to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import random

if __name__ == "__main__":
    # ustawiam liczne rzutow
    liczba_rzutow = 100
    # ustawiam wartosci poczatkowe licznikow
    liczba_orlow = 0
    liczba_reszek = 0
    #analogicznie koszytam z ranga
    for i in range(0, liczba_rzutow):
        # korzystam z random.choica jako parametr podaje mu liste zawierającą 2 stringi 'orzeł' i 'reszka'
        # jezeli wylosowany z tego zbioru element jest orlem to zwieksza wartosc liczby orlow
        # a jak nie zwiekszam liczbe reszek
        if random.choice(['orzeł', 'reszka']) == 'orzeł':
            liczba_orlow += 1
        else:
            liczba_reszek += 1

    print 'W trakcie ' + str(liczba_rzutow) + ' rzutów orzeł wypadł ' + str(liczba_orlow) + 'razy, a reszka ' + \
          str(liczba_reszek) + ' razy.'
