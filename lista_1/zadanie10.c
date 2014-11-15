#include "stdio.h"

int main(){
	//deklaruje zmienna na znaki o rozmiarze 2 (nawiasem mowiac to tablica)
	char liczba[2];

	printf("Podaj liczbe 2 cyfrową: ");

	//zapisuje 2 znaki
	scanf("%2s", liczba);

	//wyswietlam po znaku ale liczac od konca (koniec ale liczymy od zera wiec dostep do elementow mam po 0 i 1, a wskapk 1, 0)
	printf("wspak: %c%c\n",liczba[1], liczba[0]);	
	return 0;
}