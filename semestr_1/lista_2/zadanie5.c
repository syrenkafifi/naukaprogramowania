#include <stdio.h>

int  main(void){
	// deklarujemy zmienne
	int liczba_kwadratow;
	// zmienna pomocnicza do petli
	int i;

	printf("Program wypisuje tabele kwadratow.\n");
	printf("Podaj liczbe wierszy tabeli: ");
	scanf("%d", &liczba_kwadratow);

	/*
		petla while bedzie wykonywac się tak dlugo dopoki bedzie spelniony warunek
		while(warunek){
			robimy cos
		}

		w naszym przypadku bedzie to tak
		najpierw ustawiamy zmienna i na 1
			i = 1;

		dopoki i bedzie mniejsze lub rowne od liczby kwadratow
		wyswietlaj taki napis
		printf("\t%d\t%d\n", i, i*i);
		pamietaj tylko aby co kazde przejscie petli zwiekszyc rozmiar i o 1 np poprzez i++

		ten program mozesz tez tez rozwiazac za pomoca funkcji for
	*/




	return 0;
};