#include <stdio.h>

int  main(void){
	// deklarujemy zmienne
	int liczba;
	int suma_liczb=0; // bedziemy do tej zmiennej dodawać liczby co kazde odpalenie petli wiec odrazu ustawiamy warunek
	// poczatkowy na zero

	printf("Podaj liczby (0 konczy szereg).\n");

	scanf("%d", &liczba);
	suma_liczb = suma_liczb + liczba;

	/*
		musisz 2 powyzsze linijki kodu urac w funkcje while
		jako warunek daj liczba==0

		do dziela :)
	*/
	printf("Suma liczb wynosi %d\n", suma_liczb);


	return 0;
};