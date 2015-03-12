#include "stdio.h"

int main(){
	
	/*deklaruje zmienne
		zakladam ze numer towaru to 3 cyfrowy numer np. 321, = wiec definiuje zmienna o jeden znak wieksza
		tak na wszelki wypadek a wiec 4

		podobnie z cena jestnostkowa i data
	*/	
	char numer_towaru[4];
	char cena_jednostkowa[11];
	char data[11];
	int i;


	/* korzystam z funckji scanf ktora jest ladniejsza :-), aby bezpiecnzie jej uzywac czyli nie sprobowac 
	za jej pomoca zapisac wartosci skladajacej sie z 5 znakow do zmiennej majacej 4 znaki ograniczam ja podajac 
	cyfre np %4s <- wowczas zapisze tylko 4 piersze znaki do znaki */
	printf("podaj numer towaru : ");
	scanf("%3s", numer_towaru);

	
	printf("podaj cene jednostkowa : ");
	scanf("%10s", cena_jednostkowa);

	printf("podaj date (dd/mm/rrrr): ");
	scanf("%10s", data);
	
	/* wykorzystaujac tabulatury \t formatuje tak jak chcial prowadzacy */
	printf("towar\t\tcena\t\tdata\n");
	printf("\t\tjedn.\t\tzakupu\n\n");
	printf("%s\t\tPLN %s\t%s\n", numer_towaru, cena_jednostkowa, data );	


	// wiecej na stronie 463 w ksiazce
	return 0;
}