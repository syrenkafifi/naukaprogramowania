# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

if __name__ == "__main__":
    # prosimy uzytkownika by podal nam sciezke do pliku w ktorym sa zapisane pytania
    sciezka_do_pliku = input("Podaj sciezke do pliku: ")

    #otwieramy ten plik
    plik = open(sciezka_do_pliku)

    #tworzymy pusta liste na ktora bedziemy wrzucac odczytane pytania
    lista_pytan = []
    #w czyms takim co nazywa try/catch/finally (chodzi mniej wiecej o to ze jakby cos poszlo nie tak to zeby nie wywalilo nam calego programu)
    #czytamy plik linia po linii
    try:
        # petla caly czas sie wykonujaca dopoki nie zosatnie przerwana
        while True:
            #czytamy linie
            linia = plik.readline()
            #jezeli linia jest pusta tzn. nastapil koniec pliku to przerywamy czytanie
            if linia == '':
                break
            else:
                #jezeli linia nie byla pusta to zakladmy ze zgodnie z przyejta struktura pierwsza linia w segmencie oznacza kategorie
                kategoria = linia
            # znow czytamy linie
            linia = plik.readline()
            #znow sprawdzamy czy nie jest pusta
            if linia == '':
                break
            else:
                #zgodnie z przyjeta strukutra linia 2 to pytanie kolejne linie analogicznie
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

            # jezeli udalo nam sie odczytac wszystkie linie wchodzace w sklad bloku to tworzymy slownik pojedynczego bloku
            # do ktorego pakujemy odczytane dane
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
            # slownik wrzucamy na liste pytan
            lista_pytan.append(pojedynczy_blok)

            # i zaczynamy od nowa czytanie segmentow

    finally:
        # po odczycie zamykamy plik
        plik.close()
    # zerujemy wynik
    wynik = 0
    # iterujemy po liscie pytan
    for blok in lista_pytan:
        # wyswietlamy dane
        print(('kategoria: ' + blok['kategoria']))
        print(('pytanie: ' + blok['pytanie']))
        print(('1) ' + blok['odpowiedz_1']))
        print(('2) ' + blok['odpowiedz_2']))
        print(('3) ' + blok['odpowiedz_3']))
        print(('4) ' + blok['odpowiedz_4']))
        # czytamy odpowiedz uzytkownika
        odpowiedz = int(input('Twoja odpowiedz (podaj numer): '))
        # sprawdzamy odpowiedz uzytkownika
        if odpowiedz == int(blok['prawidlowa_odpowiedz']):
            # jak dobra to dajemy pkt
            wynik += 1
            print ('POPRAWNA ODPOWIEDŹ')
        else:
            print ('ZŁA ODPOWIEDŹ')
        #wyswietalmy wyjasnienie
        print((blok['wyjasnienie']))

    # podsumowanie gry
    print(('Odpowiedziales prawidlowo na ' + str(wynik) + ' z ' + str(len(lista_pytan)) + ' pytań'))







