# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow
import pickle

if __name__ == "__main__":
    sciezka_do_pliku = raw_input("Podaj sciezke do pliku: ")
    wynik = 0
    lista_pytan = pickle.load( open(sciezka_do_pliku, 'rb'))
    for blok in lista_pytan:
        print 'kategoria: ' + blok['kategoria']
        print 'pytanie: ' + blok['pytanie']
        print '1) ' + blok['odpowiedz_1']
        print '2) ' + blok['odpowiedz_2']
        print '3) ' + blok['odpowiedz_3']
        print '4) ' + blok['odpowiedz_4']
        odpowiedz = int(raw_input('Twoja odpowiedz (podaj numer): '))
        if odpowiedz == int(blok['prawidlowa_odpowiedz']):
            wynik += 1
            print 'POPRAWNA ODPOWIEDŹ'
        else:
            print 'ZŁA ODPOWIEDŹ'
        print blok['wyjasnienie']

    print 'Odpowiedziales prawidlowo na ' + str(wynik) + ' z ' + str(len(lista_pytan)) + ' pytań'







