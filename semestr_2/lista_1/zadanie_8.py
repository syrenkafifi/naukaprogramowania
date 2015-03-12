# -*- coding: utf-8 -*-
#to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

if __name__ == "__main__":

    koniec = None
    while koniec != '':
        # sciagam za pomoca raw_inputa stringa
        liczba = raw_input("Podaj liczbę do testu:  ")
        # jezeli string nie jest pustym stringiem (tj. enterem) to go dalej przetwarzam
        if liczba != '':
            # potrzebuje liczbe wiec zamieniam sobie stringa na liczbe za pomoca int()
            liczba = int(liczba)
            #liczba pierwsza to liczba naturalna wieksza od 1 podzielna przez 1 i sama siebie

            # ustawiam sobie flage jako fałsz
            flaga = False
            if liczba == 1:
                flaga = True
            else:
                # interuje sobie za pomoca petli for i wyrazenia range
                # # jest to petla for each
                # czyli iteruje po wszystkich wyrazenia tablicy (w zasadzie listy, ale o tym potem)
                # wyrazenie range(2, liczba) zwroci mi tablice/liste
                # od 2 do liczba-1
                # przykladowo liczba = 5 czyli range(2,5) zwroci mi tablice [2,3,4]
                # za pomoca wyrazenia for i in range(2, liczba) dostane w kolejnych przejscia i=2, i=3, i=4
                # teoretycznie moglbym zaczac range od 1 ale liczba pierwsza to
                # liczba ktora jest podzielna przez 1 i sama siebie
                # jedynke pomijam bo kazda liczba calkowita przez nia sie dzieli
                for i in range(2, liczba):
                    # jezeli liczba jest podzielna przez i to reszta z dzielenia wynosi zero
                    if liczba % i == 0:
                        # skoro liczba jest podzielna przez jakas inna liczbe niz 1 i sama siebie
                        # to znaczy ze nie jest liczba pierwsza
                        flaga = True
                        #przerywam petle bo juz jestem pewien ze ta liczba nie jest pierwsza
                        break
            if flaga:
                # jezeli flage ustawilem na true to oznacza ze liczba nie jest liczba pierwsza wiec wyswietlam stosowny
                # komunikat
                print str(liczba) + " NIE jest liczba pierwsza"
            else:
                # i odpowiedni komunikat
                print str(liczba) + " jest liczba pierwsza"
        else:
            # taki tam chamski sposob na przerwanie programu ;P
            koniec = raw_input("Aby zakończyć program, naciśnij klawisz Enter.")