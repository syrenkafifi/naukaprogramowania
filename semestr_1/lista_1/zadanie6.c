#include "stdio.h"

int main(){
	char ulamek_1[10];
	char ulamek_2[10];

	int licznik_1;
	int mianownik_1;

	int licznik_2;
	int mianownik_2;

	int licznik_3;
	int mianownik_3;

	printf("podaj ulamek pierwszy: ");
	fgets(ulamek_1, sizeof(ulamek_1), stdin);
	// ulamek_1 = "73/2" ;
	// ulamek_1 = ['7', '3', '/', '2'];
    sscanf(ulamek_1, "%d/%d", &licznik_1, &mianownik_1);

	printf("podaj ulamek drugi: ");
	fgets(ulamek_2, sizeof(ulamek_2), stdin);
	sscanf(ulamek_2, "%d/%d", &licznik_2, &mianownik_2);

	mianownik_3 = mianownik_1 * mianownik_2;
	licznik_3 = licznik_1 * mianownik_2 + licznik_2 * mianownik_1;

	printf("suma ulamków wynosi: %d/%d \n", licznik_3, mianownik_3);
	
	return 0;
}