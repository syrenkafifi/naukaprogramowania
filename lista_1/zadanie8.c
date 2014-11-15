#include "stdio.h"

int main(){
	// taki formacik daty
	// dd/mm/rrrr

	// zmien rozmiar tych tablic znakowych zwanych stringami tak aby odpowiadal rozmiarom podanym w dd, mm i rrrr
	char dzien[2];
	char miesiac[2];
	char rok[4];
	char miesiacrok[7];

	// jaki rozmiar powinna miec zmienna data + uwzglednij znaki /
	char data[11];

	printf("podaj date (dd/mm/rrrr): ");

	// wczytaj zmienna date
	fgets(data, sizeof(data), stdin);

	// zmodyfikuj ta linie aby wczytala 3 zmienne dzien, miesiac rok i zmien znak dizelacy + na /
	sscanf(data, "%[^/]/%s", &dzien, &miesiacrok);
	/*
	data = "dd/mm/rrrr"
	dzien = "dd"
	miesiacrok = "mm/rrrr"
	miesiac = "mm"
	rok = "rrrr"
	*/
	// mm/rrrr
	sscanf(miesiacrok, "%[^/]/%s", &miesiac, &rok);

	// wyswietlam wynik
	/* %s sluzy do wyswietlenia zmiennej rok, wyswietl jeszcze za pomoca zmiennej %s miesiac i dzien*/
	printf("podales date: %s / %s / %s \n", rok, miesiac, dzien);
	
	return 0;
}