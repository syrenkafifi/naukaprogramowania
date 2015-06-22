# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

plansza = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def wyswietl_plansze(wygrana=0):
    print '    1   2   3'
    print '   ------------'
    i = 1
    for wiersz in plansza:
        rzad = str(i) + ' |'
        for kolumna in wiersz:
            if kolumna == -1:
                rzad += ' x |'
            elif kolumna == 1:
                rzad += ' o |'
            else:
                rzad += '   |'
        print rzad
        print '   ------------'
        i += 1
    print '\n'
    if wygrana == -1:
        print 'wygrałeś'
    elif wygrana == 1:
        print 'wygrał komputer'
    elif wygrana == 7:
        print 'remis'
    elif wygrana == 0:
        print 'graj dalej'


def postaw_krzyzyk(kolumna, wiersz):
    plansza[wiersz][kolumna] = -1


def reakcja_uzytkownika():
    wiersz = input("Podaj numer wiersza: ") - 1
    kolumna = input("Podaj numer kolumny: ") - 1
    if pole_jest_wolne(wiersz, kolumna):
        postaw_krzyzyk(kolumna, wiersz)
    else:
        print 'To pole jest zajete'
        reakcja_uzytkownika()


def analiza_sytuacji():
    wolne_miejsce = False
    skos_1 = 0
    skos_2 = 0
    for i in range(0, 3):
        wiersz = 0
        linia = 0
        skos_1 = skos_1 + plansza[i][i]
        skos_2 = skos_2 + plansza[2 - i][i]
        for j in range(0, 3):
            wiersz = wiersz + plansza[i][j]
            linia = linia + plansza[j][i]
            if plansza[i][j] == 0:
                wolne_miejsce = True
        if wiersz == 3 or linia == 3:
            return 1
        elif wiersz == -3 or linia == -3:
            return -1
    if skos_1 == 3 or skos_2 == 3:
        return 1
    if skos_1 == -3 or skos_2 == -3:
        return -1
    if not wolne_miejsce:
        return 7
    return 0


def sprawdz_niebezpieczna_sytuacje():
    skos_1 = 0
    skos_2 = 0
    for i in range(0, 3):
        wiersz = 0
        linia = 0
        skos_1 = skos_1 + plansza[i][i]
        skos_2 = skos_2 + plansza[2 - i][i]
        for j in range(0, 3):
            wiersz = wiersz + plansza[i][j]
            linia = linia + plansza[j][i]
        if wiersz == -2:
            for j in range(0, 3):
                if plansza[i][j] == 0:
                    plansza[i][j] = 1
            return True
        elif linia == -2:
            for j in range(0, 3):
                if plansza[j][i] == 0:
                    plansza[j][i] = 1
            return True
    if skos_1 == -2:
        for i in range(0, 3):
            if plansza[i][i] == 0:
                plansza[i][i] = 1
                return True
    elif skos_2 == -2:
        for i in range(0, 3):
            if plansza[i][2-i] == 0:
                plansza[i][2-i] = 1
                return True
    return False


def sprawdz_okazje_na_wygrana_sytuacje():
    skos_1 = 0
    skos_2 = 0
    for i in range(0, 3):
        wiersz = 0
        linia = 0
        skos_1 = skos_1 + plansza[i][i]
        skos_2 = skos_2 + plansza[2 - i][i]
        for j in range(0, 3):
            wiersz = wiersz + plansza[i][j]
            linia = linia + plansza[j][i]
        if wiersz == 2:
            for j in range(0, 3):
                if plansza[i][j] == 0:
                    plansza[i][j] = 1
            return True
        elif linia == 2:
            for j in range(0, 3):
                if plansza[j][i] == 0:
                    plansza[j][i] = 1
            return True
    if skos_1 == 2:
        for i in range(0, 3):
            if plansza[i][i] == 0:
                plansza[i][i] = 1
                return True
    elif skos_2 == 2:
        for i in range(0, 3):
            if plansza[i][2-i] == 0:
                plansza[i][2-i] = 1
                return True
    return False


def stoi_tu_krzyzyk(wiersz, kolumna):
    if plansza[wiersz][kolumna] == -1:
        return True
    else:
        return False


def stoi_tu_kolko(wiersz, kolumna):
    if plansza[wiersz][kolumna] == 1:
        return True
    else:
        return False


def pole_jest_wolne(wiersz, kolumna):
    if plansza[wiersz][kolumna] == 0:
        return True
    else:
        return False


def postaw_kolko(wiersz, kolumna):
    plansza[wiersz][kolumna] = 1


def jak_pole_jest_wolne_postaw_krzyzyk(wiersz, kolumna):
    if pole_jest_wolne(wiersz, kolumna):
        postaw_kolko(wiersz, kolumna)
        return True
    else:
        return False


def plansza_jest_czysta():
    plansza_czysta = True
    for i in range(0, 3):
        for j in range(0, 3):
            if not pole_jest_wolne(i, j):
                plansza_czysta = False
    return plansza_czysta


def graj_strategie():
    # stragia zaczynająca
    if plansza_jest_czysta():
        postaw_kolko(0, 0)
    else:


        # ruchy obronne na rozpoczęcie gry jeżeli nie zaczynaliśmy
        if stoi_tu_krzyzyk(0, 0):
            if jak_pole_jest_wolne_postaw_krzyzyk(1, 1):
                pass
            elif stoi_tu_krzyzyk(2, 2):
                if jak_pole_jest_wolne_postaw_krzyzyk(1, 0):
                    pass

        elif stoi_tu_krzyzyk(2, 2):
            if jak_pole_jest_wolne_postaw_krzyzyk(1, 1):
                pass
            elif stoi_tu_krzyzyk(0, 0):
                if jak_pole_jest_wolne_postaw_krzyzyk(1, 2):
                    pass
        elif stoi_tu_krzyzyk(0, 2):
            if jak_pole_jest_wolne_postaw_krzyzyk(1, 1):
                pass
            elif stoi_tu_krzyzyk(2, 0):
                if jak_pole_jest_wolne_postaw_krzyzyk(1, 2):
                    pass
        elif stoi_tu_krzyzyk(2, 0):
            if jak_pole_jest_wolne_postaw_krzyzyk(1, 1):
                pass
            elif stoi_tu_krzyzyk(0, 2):
                if jak_pole_jest_wolne_postaw_krzyzyk(1, 0):
                    pass
        elif stoi_tu_krzyzyk(1, 1) and pole_jest_wolne(0, 0) and pole_jest_wolne(0, 2) and pole_jest_wolne(2,
                                                                                                           0) and pole_jest_wolne(
                2, 2):
            postaw_kolko(0, 0)


def reakcja_komputera():
    if not sprawdz_okazje_na_wygrana_sytuacje():
        if not sprawdz_niebezpieczna_sytuacje():
            graj_strategie()


def zaczynamy():
    kolejnosc = raw_input("Kto zaczyna (k)omputer czy (u)zytkonik? ")
    if kolejnosc == 'k':
        reakcja_komputera()
    elif kolejnosc == 'u':
        pass
    else:
        zaczynamy()


if __name__ == "__main__":
    zaczynamy()

    wyswietl_plansze()
    wygrana = 0
    while wygrana == 0:
        if wygrana == 0:
            reakcja_uzytkownika()
            wygrana = analiza_sytuacji()
            wyswietl_plansze(wygrana)
        if wygrana == 0:
            reakcja_komputera()
            wygrana = analiza_sytuacji()
            wyswietl_plansze(wygrana)