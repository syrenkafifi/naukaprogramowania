#include <stdio.h>

int  main(void){
	/*
		for juz poznalas :)

	*/
	int liczba;
	int wynik_dzielenia;
	int i=1;

	printf("Podaj liczbę.\n");

	scanf("%d", &liczba);
	wynik_dzielenia=liczba;


	for(i=1; wynik_dzielenia > 10; i++){
		wynik_dzielenia = wynik_dzielenia / 10;
	}

	printf("Liczba %d jest %d-cydrowa :D\n", liczba, i);

	return 0;
};