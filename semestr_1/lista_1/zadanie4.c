#include "stdio.h"

int main(){
	float netto;
	float brutto;


	printf("podaj kwote: ");
	scanf("%f", &netto);

	brutto = netto * 1.05;

	printf("z podatkiem: %.2f \n" , brutto);

	return 0;
}