#include "stdio.h"

int main(){
	int kwota;
	int nominal_20;
	int nominal_10;
	int nominal_5;
	int nominal_1;
	int reszta;


	printf("podaj kwote: ");
	scanf("%d", &kwota);

	nominal_20 = kwota/20;
	reszta = kwota - nominal_20 * 20;

	nominal_10 = reszta/10;
	reszta = reszta - nominal_10 * 10;


	nominal_5 = reszta/5;
	reszta = reszta - nominal_10 * 5;


	nominal_1 = reszta;
	

	printf("nominal 20 : %d \n" , nominal_20);
	printf("nominal 10 : %d \n" , nominal_10);
	printf("nominal 5 : %d \n" , nominal_5);
	printf("nominal 1 : %d \n" , nominal_1);

	return 0;
}