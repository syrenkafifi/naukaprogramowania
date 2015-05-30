# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow

import copy

a = 53.15
b = -32.97
c = -43.33
d = 24.61
e = -26.26
f = 1.04

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

tablica_wartosci = [
    # [a, b, c, d, e, f, g, h],
    [a, b, d, d, d, d, b, a],  # 1
    [b, c, e, e, e, e, c, b],  # 2
    [d, e, f, f, f, f, e, d],  # 3
    [d, e, f, f, f, f, e, d],  # 4
    [d, e, f, f, f, f, e, d],  # 5
    [d, e, f, f, f, f, e, d],  # 6
    [b, c, e, e, e, e, c, b],  # 7
    [a, b, d, d, d, d, b, a],  # 8
]


def funkcja_celu(plansza):
    suma = 0
    for i in range(0, 8):
        for j in range(0, 8):
            suma += plansza[i][j] * tablica_wartosci[i][j]
    return suma


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
    wyswietlana_plansza = copy.deepcopy(plansza)
    lista_mozliwych_ruchow = mozliwe_ruchy(gracz=-1, plansza=plansza)
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
                rzad += ' X |'
            elif kolumna == 1:
                rzad += ' O |'
            elif kolumna == 'm':
                rzad += ' . |'
            else:
                rzad += '   |'
        rzad += ' ' + str(i)
        if i == 3:
            rzad += '        ilość możliwych ruchów (.) --- ' + str(len(lista_mozliwych_ruchow))
        if i == 4:
            rzad += '        GRACZ (X) -------------------- ' + str(liczba_kolek)
        if i == 5:
            rzad += '        KOMPUTER (O) ----------------- ' + str(liczba_krzyzykow)
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
    mozliwe_ruchy_komputera = mozliwe_ruchy(gracz=1, plansza=plansza)
    if len(mozliwe_ruchy_komputera)>0:
        najlepszy_ruch = mozliwe_ruchy_komputera[0]
        najwieksza_funkcja_celu = 0
        for ruch in mozliwe_ruchy_komputera:
            kopia_planszy = copy.deepcopy(plansza)
            kopia_planszy[ruch[0]][ruch[1]] = 1
            przetwarzanie_planszy(gracz=1, wiersz=ruch[0], kolumna=ruch[1], plansza=kopia_planszy)
            fc = funkcja_celu(plansza=kopia_planszy)
            if fc >najwieksza_funkcja_celu:
                najwieksza_funkcja_celu =fc
                najlepszy_ruch = ruch

        plansza[ruch[0]][ruch[1]] = 1
        przetwarzanie_planszy(gracz=1, wiersz=ruch[0], kolumna=ruch[1], plansza=plansza)



def postaw_krzyzyk(kolumna, wiersz):
    plansza[wiersz][kolumna] = -1


def postaw_kolko(wiersz, kolumna):
    plansza[wiersz][kolumna] = 1


def przetwarzanie_planszy(gracz, wiersz, kolumna, plansza):
    # 0 +1
    i = wiersz
    k = kolumna + 1
    if k < 8 and plansza[i][k] == gracz * (-1):
        while k < 8:
            if plansza[i][k] == gracz:
                for x in range(kolumna, k):
                    plansza[i][x] = gracz
                break
            k += 1
    # 0 -1
    i = wiersz
    k = kolumna - 1
    if k > 0 and plansza[i][k] == gracz * (-1):
        while k > 0:
            if plansza[i][k] == gracz:
                for x in range(k, kolumna):
                    plansza[i][x] = gracz
                break
            k -= 1
    # +1 0
    i = wiersz + 1
    k = kolumna
    if i < 8 and plansza[i][k] == gracz * (-1):
        while i < 8:
            if plansza[i][k] == gracz:
                for y in range(wiersz, i):
                    plansza[y][k] = gracz
                break
            i += 1
    # -1 0
    i = wiersz - 1
    k = kolumna
    if i > 0 and plansza[i][k] == gracz * (-1):
        while i > 0:
            if plansza[i][k] == gracz:
                for y in range(i, wiersz):
                    plansza[y][k] = gracz
                break
            i -= 1
    # +1 +1
    i = wiersz + 1
    k = kolumna + 1
    if i < 8 and k < 8 and plansza[i][k] == gracz * (-1):
        while i < 8 and k < 8:
            if plansza[i][k] == gracz:
                for q in range(0, 8):
                    if i + q < 8 and k + q < 8:
                        plansza[i + q][k + q] = gracz
                break
            i += 1
            k += 1
    # -1 +1
    i = wiersz - 1
    k = kolumna + 1
    if i > 0 and k < 8 and plansza[i][k] == gracz * (-1):
        while i > 0 and k < 8:
            if plansza[i][k] == gracz:
                for q in range(0, 8):
                    if i - q > 0 and k + q < 8:
                        plansza[i - q][k + q] = gracz
                break
            i -= 1
            k += 1
    # +1 -1
    i = wiersz + 1
    k = kolumna - 1
    if i < 8 and k > 0 and plansza[i][k] == gracz * (-1):
        while i < 8 and k > 0:
            if plansza[i][k] == gracz:
                for q in range(0, 8):
                    if i + q < 8 and k - q > 0:
                        plansza[i + q][k - q] = gracz
                break
            i += 1
            k -= 1
    # -1 -1
    i = wiersz - 1
    k = kolumna - 1
    if i > 0 and k > 0 and plansza[i][k] == gracz * (-1):
        while i > 0 and k > 0:
            if plansza[i][k] == gracz:
                for q in range(0, 8):
                    if i - q > 0 and k - q > 0:
                        plansza[i - q][k - q] = gracz
                break
            i -= 1
            k -= 1


def reakcja_uzytkownika():
    wyswietl_plansze()
    mozliwe_ruchy_gracza = mozliwe_ruchy(gracz=-1, plansza=plansza)
    wiersz = input("Podaj numer wiersza: ") - 1
    kolumna = input("Podaj numer kolumny: ") - 1
    if (wiersz, kolumna) in mozliwe_ruchy_gracza:
        postaw_krzyzyk(kolumna, wiersz)
        przetwarzanie_planszy(gracz=-1, wiersz=wiersz, kolumna=kolumna, plansza=plansza)
    else:
        print
        print 'To pole jest niedozwolne'
        print
        reakcja_uzytkownika()


def mozliwe_ruchy(gracz, plansza):
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
                    if gracz * (-1) == plansza[i - 1][j]:  # sprawdzenie czy pionek obok jest przeciwnika
                        k = i - 1
                        while k > 0 and plansza[k][j] == gracz * (-1):
                            if plansza[k - 1][j] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                            k -= 1
                # 0 -1
                if j - 1 > 0:
                    if gracz * (-1) == plansza[i][j - 1]:  # sprawdzenie czy pionek obok jest przeciwnika
                        k = j - 1
                        while k > 0 and plansza[i][k] == gracz * (-1):
                            if plansza[i][k - 1] == gracz:
                                flaga_czy_mozna = True
                                k = 0
                            k -= 1
                # +1 +1
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
                # +1 -1
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
                # -1 +1
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
                # -1 -1
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


def analiza_sytuacji():
    if len(mozliwe_ruchy(gracz=-1, plansza=plansza)) == 0 and len(mozliwe_ruchy(gracz=1, plansza=plansza)) == 0:
        liczba_kolek, liczba_krzyzykow = podlicz_plansze()
        if liczba_kolek > liczba_krzyzykow:
            return -1
        elif liczba_kolek < liczba_krzyzykow:
            return 1
        return 7
    return 0


if __name__ == "__main__":
    zaczynamy()
    wygrana = 0

    while wygrana == 0 or wygrana == 7:
        if wygrana == 0 or wygrana == 7:
            reakcja_uzytkownika()
            wygrana = analiza_sytuacji()
        if wygrana == 0 or wygrana == 7:
            reakcja_komputera()
            wygrana = analiza_sytuacji()

    wyswietl_plansze()
    if wygrana == -1:
        print 'wygrał gracz'
    if wygrana == 1:
        print 'wygrał komputer'
    if wygrana == 7:
        print 'remis'

