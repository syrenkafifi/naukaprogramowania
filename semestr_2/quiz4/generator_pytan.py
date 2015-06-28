#importujemy pickle
import pickle

if __name__ == "__main__":
    # prosimy o nazwe pliku gdzie zapiszemy wygenerowane pytania
    sciezka_do_pliku = input("Podaj nazwe pliku gdzie zapiszesz pytania: ")
    # sciezka_do_pliku = 'pytania'

    lista_pytan = []
    #dopoki nie wcisniemy k bedziemy generowac pytania
    while True:
        # w pojedynczym przejsciu petli generujemy pojedynczy blok pytania
        kategoria = input('Podaj nazwe kategorii (aby przerwać wpisz k): ')
        if kategoria == 'k':
            break
        pytanie = input('Zadaj pytanie (aby przerwać wpisz k): ')
        if pytanie == 'k':
            break
        odpowiedz_1 = input('Podaj odpowiedź 1 (aby przerwać wpisz k): ')
        if odpowiedz_1 == 'k':
            break
        odpowiedz_2 = input('Podaj odpowiedź 2 (aby przerwać wpisz k): ')
        if odpowiedz_2 == 'k':
            break
        odpowiedz_3 = input('Podaj odpowiedź 3 (aby przerwać wpisz k): ')
        if odpowiedz_3 == 'k':
            break
        odpowiedz_4 = input('Podaj odpowiedź 4 (aby przerwać wpisz k): ')
        if odpowiedz_4 == 'k':
            break
        prawidlowa_odpowiedz = input('Podaj numer prawidlowej odpowiedzi (aby przerwać wpisz k): ')
        if prawidlowa_odpowiedz == 'k':
            break
        wyjasnienie = input('Podaj wyjasnienie (aby przerwać wpisz k): ')
        if wyjasnienie == 'k':
            break

        # skladamy blok pytania
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
        #dodajemy blok na liste pytan
        lista_pytan.append(pojedynczy_blok)
        # czy chcemy dalej generowac
        dalej = input('Czy chcesz kontynuować przygotowywanie pytań (wpisz tak): ')
        if dalej != 'tak':
            break
    # serializujemy (czyli jakby to powiedziec zakodowujemy pytania, po czym to co zakodzilismy wrzucamy do wczesniej wybranego pliku
    pickle.dump(lista_pytan, open(sciezka_do_pliku, 'wb'))






