# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

import pickle

if __name__ == "__main__":
    # sciezka_do_pliku = raw_input("Podaj nazwe pliku gdzie zapiszesz pytania: ")
    sciezka_do_pliku = 'pytania'

    lista_pytan = []

    while True:
        kategoria = raw_input('Podaj nazwe kategorii (aby przerwać wpisz k): ')
        if kategoria == 'k':
            break
        pytanie = raw_input('Zadaj pytanie (aby przerwać wpisz k): ')
        if pytanie == 'k':
            break
        odpowiedz_1 = raw_input('Podaj odpowiedź 1 (aby przerwać wpisz k): ')
        if odpowiedz_1 == 'k':
            break
        odpowiedz_2 = raw_input('Podaj odpowiedź 2 (aby przerwać wpisz k): ')
        if odpowiedz_2 == 'k':
            break
        odpowiedz_3 = raw_input('Podaj odpowiedź 3 (aby przerwać wpisz k): ')
        if odpowiedz_3 == 'k':
            break
        odpowiedz_4 = raw_input('Podaj odpowiedź 4 (aby przerwać wpisz k): ')
        if odpowiedz_4 == 'k':
            break
        prawidlowa_odpowiedz = raw_input('Podaj numer prawidlowej odpowiedzi (aby przerwać wpisz k): ')
        if prawidlowa_odpowiedz == 'k':
            break
        wyjasnienie = raw_input('Podaj wyjasnienie (aby przerwać wpisz k): ')
        if wyjasnienie == 'k':
            break


        pojedynczy_blok = {
                'kategoria': kategoria,
                'pytanie': pytanie,
                'odpowiedz_1': odpowiedz_1,
                'odpowiedz_2': odpowiedz_2,
                'odpowiedz_3': odpowiedz_3,
                'odpowiedz_4': odpowiedz_4,
                'prawidlowa_odpowiedz': prawidlowa_odpowiedz,
                'wyjasnienie': wyjasnienie,
            }
        lista_pytan.append(pojedynczy_blok)

        dalej = raw_input('Czy chcesz kontynuować przygotowywanie pytań (wpisz tak): ')
        if dalej != 'tak':
            break

    pickle.dump(lista_pytan, open(sciezka_do_pliku, 'wb'))






