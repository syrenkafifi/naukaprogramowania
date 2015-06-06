# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

if __name__ == "__main__":
    # sciezka_do_pliku = raw_input("Podaj sciezke do pliku: ")
    sciezka_do_pliku = 'pytania'
    plik = open(sciezka_do_pliku)

    lista_pytan = []
    try:
        # tekst = plik.read()
        while True:
            linia = plik.readline()
            if linia == '':
                break
            else:
                kategoria = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                pytanie = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                odpowiedz_1 = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                odpowiedz_2 = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                odpowiedz_3 = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                odpowiedz_4 = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                prawidlowa_odpowiedz = linia
            linia = plik.readline()
            if linia == '':
                break
            else:
                wyjasnienie = linia

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

    finally:
        plik.close()
    wynik = 0
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







