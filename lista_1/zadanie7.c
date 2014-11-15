#include "stdio.h"

int main(){
	char dwaulamki[21];
	char ulamek_1[10];
	char ulamek_2[10];

	int licznik_1;
	int mianownik_1;

	int licznik_2;
	int mianownik_2;

	int licznik_3;
	int mianownik_3;

	printf("podaj dwa ulamki oddzielone znakiem plus: ");

	// czytam to co wpisalas do zmiennej dwa ulamki
	fgets(dwaulamki, sizeof(dwaulamki), stdin);

	// dziele string dwa ulamki na 2 stringi ulamek_1 i ulamek_2
	sscanf(dwaulamki, "%[^+]+%s", &ulamek_1, &ulamek_2);

	// dziele zmienna typu string ulamek_1 na dwie zmienne calkowitoliczbowe licznik_1 i mianownik_1
	// zapis &licznik_1 oznacza ze do szuflady podpisanej licznik_1 wsadzamy wartosc liczbowa pierwsza przed /
	sscanf(ulamek_1, "%d/%d", &licznik_1, &mianownik_1);

	// jak wyzej dla ulamka 2
	sscanf(ulamek_2, "%d/%d", &licznik_2, &mianownik_2);

	// licze wspolny mianownik
	mianownik_3 = mianownik_1 * mianownik_2;

	// dodaje do siebie liczniki
	licznik_3 = licznik_1 * mianownik_2 + licznik_2 * mianownik_1;

	// wyswietlam wynik
	// %d sluzy do wyswietlenia licznik_3, a drugie do wyswietlenia mianownika_3, obie te liczby sa oddzielone /
	printf("suma ulamków wynosi: %d/%d \n", licznik_3, mianownik_3);
	
	return 0;
}