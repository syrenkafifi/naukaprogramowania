# -*- coding: utf-8 -*-

if __name__ == "__main__":

    koniec = None
    while koniec != '':
        liczba = raw_input("Podaj liczbę do testu:  ")
        if liczba != '':
            liczba = int(liczba)
            flaga = False
            for i in range(2,liczba):
                if liczba % i == 0:
                    flaga = True
            if flaga:
                print str(liczba) + " nie jest liczba pierwsza"
            else:
                print str(liczba) + " jest liczba pierwsza"
        else:
            koniec = raw_input("Aby zakończyć program, naciśnij klawisz Enter.")