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
		instrukcja for
		for(ustalam warunki poczatkwowe np i = 1; warunek warunkujacy wykonanie funckji np i <3; co robie z licznikiem i np i++)
	*/
	for(i = 1; i <= liczba_kwadratow; i++){
		printf("\t%d\t%d\n", i, i*i);
	}

	return 0;
};