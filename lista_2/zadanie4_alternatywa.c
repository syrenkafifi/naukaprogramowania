#include <stdio.h>

int  main(void){

	// deklarujemy zmienne:

	int dzien;
	int miesiac;
	int rok;
	// deklaruję tablicę stringów
	char miesiac_slowem[12][20] = {"stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "wrzesnia", "pazdziernika", 
		"listopada", "grudnia"};
	

	// czytamy dzien miesiąc i rok
	printf("Podaj date (dd/mm/rrrr): ");
	scanf("%d/%d/%d", &dzien, &miesiac, &rok);

	printf("Zapis urzędowy: %d %s %d r.\n", dzien, miesiac_slowem[miesiac], rok);

	// odpal program i zobacz jak dziala.... hmmm jakby o jeden miesiac przesuniety do przodu. czy wiesz moze dlaczego?:> 

	//podpowiedz: zaczynamy liczyć od 1 czy zera ?:>

};