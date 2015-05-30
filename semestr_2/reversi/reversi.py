# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

plansza = [
    # [a, b, c, d, e, f, g, h],
    [0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, -1, 1, 0, 0, 0],  # 4
    [0, 0, 0, 1, -1, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0],  # 8
]


def podlicz_plansze():
    liczba_kolek = 0
    liczba_krzyzykow = 0

    for i in range(0, 8):
        for j in range(0, 8):
            if plansza[i][j] == -1:
                liczba_krzyzykow += 1
            if plansza[i][j] == 1:
                liczba_kolek += 1

    return liczba_kolek, liczba_krzyzykow


def wyswietl_plansze():
    liczba_kolek, liczba_krzyzykow = podlicz_plansze()
    wyswietlana_plansza = plansza
    lista_mozliwych_ruchow = mozliwe_ruchy(-1)
    for ruch in lista_mozliwych_ruchow:
        wyswietlana_plansza[ruch[0]][ruch[1]] = 'm'

    # print '    a   b   c   d   e   f   g   h'
    print '    1   2   3   4   5   6   7   8'

    print '  ---------------------------------'
    i = 1
    for wiersz in wyswietlana_plansza:
        rzad = str(i) + ' |'
        for kolumna in wiersz:
            if kolumna == -1:
                rzad += ' x |'
            elif kolumna == 1:
                rzad += ' o |'
            elif kolumna == 'm':
                rzad += ' . |'
            else:
                rzad += '   |'
        rzad += ' ' + str(i)
        if i == 4:
            rzad += '        kolka\t: ' + str(liczba_kolek)
        if i == 5:
            rzad += '        krzyzyki\t: ' + str(liczba_krzyzykow)
        print rzad
        print '  ---------------------------------'
        i += 1
        # print '    a   b   c   d   e   f   g   h'
    print '    1   2   3   4   5   6   7   8'
    print '\n'


def zaczynamy():
    kolejnosc = raw_input("Kto zaczyna (k)omputer-kolka czy (u)zytkonik-krzyzyki? ")
    if kolejnosc == 'k':
        reakcja_komputera()
    elif kolejnosc == 'u':
        pass
    else:
        zaczynamy()


def reakcja_komputera():
    pass


def postaw_krzyzyk(kolumna, wiersz):
    plansza[wiersz][kolumna] = -1


def postaw_kolko(wiersz, kolumna):
    plansza[wiersz][kolumna] = 1


def reakcja_uzytkownika():
    wiersz = input("Podaj numer wiersza: ") - 1
    kolumna = input("Podaj numer kolumny: ") - 1
    if pole_jest_wolne(wiersz, kolumna):
        postaw_krzyzyk(kolumna, wiersz)
    else:
        print 'To pole jest niedozwolne'
        reakcja_uzytkownika()


def mozliwe_ruchy(gracz):
    lista = []

    for i in range(0, 8):
        for j in range(0, 8):  # podwójna petla sprawdzaj¹ca wszystkie pola
            flaga_czy_mozna = False
            if plansza[i][j] == 0:  # by sprawdzane by³y tylko puste pola
                # +1 0
                if i + 1 < 8:
                    if gracz * (-1) == plansza[i + 1][j]:  # sprawdzenie czy pionek obok jest przeciwnika
                        k = i + 1
                        while k < 8 and plansza[k][j] == gracz * (-1):
                            if plansza[k + 1][j] == gracz:
                                flaga_czy_mozna = True
                                k = 8
                            k += 1
                # 0 +1
                if j + 1 < 8:
                    if gracz * (-1) == plansza[i][j + 1]:  # sprawdzenie czy pionek obok jest przeciwnika
                        k = j + 1
                        while k < 8 and plansza[i][k] == gracz * (-1):
                            if plansza[i][k + 1] == gracz:
                                flaga_czy_mozna = True
                                k = 8
                            k += 1
                # -1 0
                if i - 1 > 0:
                    if gracz * (-1) == plansza[i - 1][j]:  #sprawdzenie czy pionek obok jest przeciwnika
                        k = i - 1
                        while k > 0 and plansza[k][j] == gracz * (-1):
                            if plansza[k - 1][j] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                            k -= 1
                # 0 -1
                if j - 1 > 0:
                    if gracz * (-1) == plansza[i][j - 1]:  #sprawdzenie czy pionek obok jest przeciwnika
                        k = j - 1
                        while k > 0 and plansza[i][k] == gracz * (-1):
                            if plansza[i][k - 1] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                            k -= 1
                #+1 +1
                if i + 1 < 8 and j + 1 < 8:
                    if gracz * (-1) == plansza[i + 1][j + 1]:
                        k = i + 1
                        g = j + 1
                        while k < 8 and g < 8 and plansza[k][g] == gracz * (-1):
                            if plansza[k + 1][g + 1] == gracz:
                                flaga_czy_mozna = True
                                k = 8
                                g = 8
                            k += 1
                            g += 1
                #+1 -1
                if i + 1 < 8 and j - 1 > 0:
                    if gracz * (-1) == plansza[i + 1][j - 1]:
                        k = i + 1
                        g = j - 1
                        while k < 8 and g > 0 and plansza[k][g] == gracz * (-1):
                            if plansza[k + 1][g - 1] == gracz:
                                flaga_czy_mozna = True
                                k = 8
                                g = 0
                            k += 1
                            g -= 1
                #-1 +1
                if i - 1 > 0 and j + 1 < 8:
                    if gracz * (-1) == plansza[i - 1][j + 1]:
                        k = i - 1
                        g = j + 1
                        while k > 0 and g < 8 and plansza[k][g] == gracz * (-1):
                            if plansza[k - 1][g + 1] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                                g = 8
                            k -= 1
                            g += 1
                #-1 -1
                if i - 1 > 0 and j - 1 > 0:
                    if gracz * (-1) == plansza[i - 1][j - 1]:
                        k = i - 1
                        g = j - 1
                        while k > 0 and g > 0 and plansza[k][g] == gracz * (-1):
                            if plansza[k - 1][g - 1] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                                g = 0
                            k -= 1
                            g -= 1
            if flaga_czy_mozna:
                lista.append((i, j))
    return lista




def pole_jest_wolne(wiersz, kolumna):
    if plansza[wiersz][kolumna] == 0:
        return True
    return False


if __name__ == "__main__":
    zaczynamy()

    wyswietl_plansze()
    while wygrana == 0:
        if wygrana == 0:
            reakcja_uzytkownika()
            wygrana = analiza_sytuacji()
            wyswietl_plansze()
    if wygrana == 0:
        reakcja_komputera()
        wygrana = analiza_sytuacji()
        wyswietl_plansze()


