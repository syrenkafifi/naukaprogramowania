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
                    if gracz * (-1) == plansza[i + 1][j + 1]:
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
                    if gracz * (-1) == plansza[i + 1][j + 1]:
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