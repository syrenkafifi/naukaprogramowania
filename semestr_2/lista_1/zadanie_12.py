# -*- coding: utf-8 -*-
#to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import random

if __name__ == "__main__":
    liczba_prob = 0
    # ustawiam poczatkowe przedzialy [0,100]
    a = 1
    b = 100
    strzal_komputera = None
    # petla bedzie sie wykonywac zawsze az do przerwania przy trafieniu
    while True:
        # komputer sobie strzela
        strzal_komputera = random.randint(a, b)
        liczba_prob += 1
        # ustawiam odpowiedz jako pusta
        odpowiedz = None
        # petla while bedzie wykonywac sie dopoki dopoty odpowiedz nie bedzie znajdwać sie w krotce (kotce) tupli :P
        # dopuszczalne odpowiedzi to 't' odpowiadajace tak
        # 'm' szukana liczba jest mniejsza
        # 'w' szukana liczba jest wieksza
        # napewno chociaz raz odpowiedz nie bedzie zawarta w tupli (krotce kotce :P)
        # poprostu ustawilem zbior akceptowalnych odpowiedzi
        while odpowiedz not in ('t', 'm', 'w'):
            odpowiedz = raw_input("PRÓBA #" + str(liczba_prob) +": Czy liczba o której pomyślałeś to " + str(strzal_komputera) +
                              " ? (t)ak/jest (w)ieksza/jest (m)niejsza ")
        # jezeli odpowiedz jest 't' to znaczy ze komputer zgadl i przerywam petle while
        if odpowiedz == 't':
            break
        # jezeli nie trafilem i odpowiedz byla m to znaczy ze musimy zmiejszyc liczbe b odpowiadajaca gornemu
        # ograniczeniu z jakiego losujemy liczby
        elif odpowiedz == 'm':
            b = strzal_komputera-1
        else:
            # jezeli nie trafilem i odpowiedz byla w to znaczy ze musimy zwiekszyc liczbe a odpowiadajaca dolnemu
            # ograniczeniu z jakiego losujemy liczby
            a = strzal_komputera+1

        # jezeli a == b to nas zakres jednoznacznie wskazuje na szukana liczbe i mozemy przerwac petle juz tutaj
        # bo jest mozliwy tylko 1 wynik
        if a == b:
            strzal_komputera = a
            break

    print "Szukana liczba była liczba " + str(strzal_komputera) + " i zgadłem ją w " + str(liczba_prob) + " próbie."
