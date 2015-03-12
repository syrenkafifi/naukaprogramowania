# -*- coding: utf-8 -*-
#to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import random

if __name__ == "__main__":
    #ustawiam liczbe rzutow
    liczba_rzutow = 1000
    # ustawiam liste w ktorej bede trzymal wyniki
    tablica_wynikow = [0, 0, 0, 0, 0, 0]

    # petla for ktora wykona sie tyle razy ile jest zapisane w zmiennej liczba_rzutow
    for i in range(0, liczba_rzutow):
        # dokonuje losowania inta z zakresu od 0 do 5
        # wylosowana liczba posluzy mi jako indeks do tablicy/listy
        # jezeli przykladowo wylosowalem 2 (co odpowiada 3 na kostce)
        # biore 3 element tablicy ktory jest zaindeksowany jako 2
        # i zwiekszam jego wartosc o jedna
        tablica_wynikow[random.randint(0, 5)] += 1

    print 'W trakcie ' + str(liczba_rzutow) + ' rzutów sześcienną kostką, wypadły następujące liczby:'
    # wyswietlam wyniki
    for i in range(0, 6):
        print str(i + 1) + ' - ' + str(tablica_wynikow[i]) + ' razy,'
