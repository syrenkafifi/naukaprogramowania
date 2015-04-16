# -*- coding: utf-8 -*-
# to powyżej słuzy poprawnemu wyswietlaniu polskich znakow


#importuje biblioteke random slużącą do generowanie losowych wartośći/losowania etc
import random

# definiuje tuple skladającą się z tupli par
# mogłem użyć listy, ale użyłem tupli z tego względu, że nie będzie się zmieniać ten zbiór
# w sensie nie będę dodawał nowej pary etc.
pary = (
    ('OORO', 'OROO'),
    ('OROO', 'ROOO'),
    ('ROOO', 'OORO')
)

# definiuje liste skladajaca sie ze słowników. W zasadzie można było to zrobić jako lista list, albo cokolwiek, też tuple
# dałem liste słowników by później ładnie sie odwoływać w kodzie
# każdy słownik zawiera wyniki dla jednej gry i ma 2 pary wartość-klucz
# gracz_1 i gracz_2 co odpowiada liczbie wygranej tur dla gracza 1 i gracza 2.
# na początku każdy gracz ma 0 zwyciestw
wyniki_par = [
        {
            'gracz_1': 0,
            'gracz_2': 0,
        },
        {
            'gracz_1': 0,
            'gracz_2': 0,
        },
        {
            'gracz_1': 0,
            'gracz_2': 0,
        }
]

# tworze sobie tuple odpowiadająca monecie. użyłem tupli bo nie bede dodawał ani odejmował "strony monety
penney = ('O', 'R')

# petla iterujaca po zbiorze par. mogłem użyć pętli iterującej for each (tzn for para in pary:) ale przyda mi sie wartosc
# i do zapisyawnia wynikow
for i in range(0,3):
    #dla kazdego zbioru par gramy w sumie 1000 razy
    for j in range(0,1000):
        # zaczynamy gre
        #ustawiamy flage wygrana na false
        wygrana = False
        # ustawiamy zerowy ciag wynikow - tzn. zaczynamy gre i jescze nic nie wypadlo
        ciag = ''
        # dopoki ktoras ze stron nie wygra i nie ustawi flaga wygrana na true wykonuje sie petla while
        while not wygrana:
            #wykonujemy rzut monetą za pomocą funkcji choice z biblioteki random. funkcja to losuje element ze zbioru
            # ktory podalismy jej jako argument. w tym przypadku losujemy ze zbioru penney
            rzut = random.choice(penney)
            # dodajemy wynik rzutu do ciagu wynikow
            ciag += rzut
            # sprawdzamy ostatnie 4 znaki w ciagu. jest to tak jakby okno (taki techniczny slang) o szerokosci 4 znakow
            # ktore przesuwamy po kazdym rzucie
            # notacja ciag[-4:] zwroci nam co najwyzej 4 ostatnie elementy zbioru
            # w tym przypadku listy
            # jezeli przykladowo lista ma tylko 2 elementy to zwroci nam cala liste
            okno = ciag[-4:]
            # sprawdzamy czy wartosc okna rowna sie wartosci pary ktora odpowiada graczowi 1
            # jezeli odpowiada to zwiekszamy wynik gracza 1 dla odpowiedniej tury (dlatego uzywam tu i)
            # i ustawiam flage wygrana na true aby zakonczyc petle while
            if okno == pary[i][0]:
                wyniki_par[i]['gracz_1']+=1
                wygrana = True
            # analogicznie dla gracza 2
            if okno == pary[i][1]:
                wyniki_par[i]['gracz_2']+=1
                wygrana = True
            # jezeli zaden gracz nie wygrał to petla powroci do poczatku i wykona ponowny rzut i reszte

# wyswietlamy wyniki
print 'WYNIKI'

# a tutaj zeby bylo ciekawiej uzylem petli for each, ktora przejdzie po wsystkich elementach listy
for wynik in wyniki_par:
    print 'PARA ' + str(i) + ' - gracz_1: ' + str(wynik['gracz_1'])+'    - gracz_2: ' + str(wynik['gracz_2'])
