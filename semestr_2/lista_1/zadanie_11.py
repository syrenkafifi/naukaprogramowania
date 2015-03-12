# -*- coding: utf-8 -*-
#to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import random

if __name__ == "__main__":
    liczba_prob = 0
    #losuje liczbe z zakresu od 1 do 100
    szukana_liczba = random.randint(1, 100)

    while True:
        liczba = raw_input("Zgadnij o jakiej liczbie myślę:  ")
        liczba_prob += 1
        if liczba != '':
            liczba = int(liczba)
            # jezeli trafilem w to co wybral sobie komputer to przeywam petle
            if liczba == szukana_liczba:
                break
                # jezeli nie trafilem i jezeli liczba jaka podalem byla mniejsza od szukanej liczby wyswieltma komunikat
            elif liczba < szukana_liczba:
                print "PUDŁO ! Szukana liczba jest większa."
            else:
                #i wyswietlam komunikat jezeli nie trafilem i liczba byla mniejsza
                print "PUDŁO ! Szukana liczba jest mniejsza"
        liczba_prob += 1

    #wyswietlam informacje o wynikach
    print "Szukana liczba była liczba " + str(szukana_liczba) + " i zgadłeś ją w " + str(liczba_prob) + " próbie."
