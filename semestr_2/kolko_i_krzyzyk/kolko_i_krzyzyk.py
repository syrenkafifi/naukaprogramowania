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


def reakcja_uzytkownika():
    wiersz = input("Podaj numer wiersza: ")
    kolumna = input("Podaj numer kolumny: ")
    plansza[wiersz - 1][kolumna - 1] = -1


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
        for i in range(0, 2):
            if plansza[i][i] == 0:
                plansza[i][j] = 1
        return True
    elif skos_2 == -2:
        if plansza[i][i] == 0:
            plansza[2 - i][j] = 1
        return True
    return False


def graj_strategie():
    if plansza[0][0] == -1:
        if plansza[0][2] == 0:
            plansza[0][2] = 1
        elif plansza[2][0] == 0:
            plansza[0][2] = 1
        elif plansza[1][1] == 0:
            plansza[1][1] = 1
    elif plansza[2][2] == -1:
        if plansza[0][0] == 0:
            plansza[0][0] = 1
        elif plansza[1][1] == 0:
            plansza[1][1] = 1
    elif plansza[2][0] == -1:
        if plansza[0][2] == 0:
            plansza[0][2] = 1
        elif plansza[1][1] == 0:
            plansza[1][1] = 1
    elif plansza[0][2] == -1:
        if plansza[2][0] == 0:
            plansza[2][0] = 1
        elif plansza[1][1] == 0:
            plansza[1][1] = 1
    elif plansza[0][0] == 0:
        plansza[0][0] = 1
    elif plansza[0][0] == 1:
        if plansza[2][2] == 0:
            plansza[2][2] = 1
        elif plansza[2][2] == 1:
            if plansza[0][2] == 0:
                plansza[0][2] = 1
            elif plansza[0][2] == 1:
                if plansza[0][1] == 0:
                    plansza[0][1] = 1
                elif plansza[1][2] == 0:
                    plansza[1][2] =1
    else:
        for i in range(0,3):
            for j in range(0,3):
                if plansza[i][j] == 0:
                    plansza[i][j] = 1


def reakcja_komputera():
    if not sprawdz_niebezpieczna_sytuacje():
        graj_strategie()


if __name__ == "__main__":

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