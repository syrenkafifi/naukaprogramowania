#include <stdio.h>

int  main(void){
	/*
		instrukcja do while wyglda tak
		do{
			cos tam cos tam
		}while(warunek)

		jest bardzo podobna do funkcji while z ta roznica ze petla chociaz raz sie wykona nawet jezeli warunek
		nie jest spelniony. poprostu cos robi a pozniej sprawdza czy jeszcze raz moze ruszyc

		warunek bedzie wygladal nastepujaco
		napoczatku i = 1
		wchodzimy do ciala petli
		zwiekszamy i o 1 poprzez i++
		dokonujemy dzielenia liczby
		bedziemy dokonywac dzielenia liczby
		jezeli wynik dzielenia musiny jeszcze raz wykonac te funkcje
		jezeli nie to wypisujemy wynik

		ten program jest kompletnym :)

	*/
	int liczba;
	int wynik_dzielenia;
	int i=1;

	printf("Podaj liczbę.\n");

	scanf("%d", &liczba);
	wynik_dzielenia=liczba;

	do{
		i++;
		wynik_dzielenia = wynik_dzielenia / 10;
	}while(wynik_dzielenia>10);

	printf("Liczba %d jest %d-cydrowa :D\n", liczba, i);

	return 0;
};