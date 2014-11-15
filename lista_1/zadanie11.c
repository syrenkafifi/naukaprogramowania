#include "stdio.h"

//skopiowane zadanie 10 musisz pozmieniac
int main(){
	//deklaruje zmienna na znaki o rozmiarze 2 (nawiasem mowiac to tablica)
	//! zmien rozmiar zmiennej
	char liczba[2];

	//! zmien stringa (nie stringi):P
	printf("Podaj liczbe 2 cyfrową: ");

	//zapisuje 2 znaki
	//! a moze jednak 3 znaki?
	scanf("%2s", liczba);

	//wyswietlam po znaku ale liczac od konca (koniec ale liczymy od zera wiec dostep do elementow mam po 0 i 1, a wskapk 1, 0)
	//! zmien to i wyswietl 3 znaki wspak
	printf("wspak: %c%c\n",liczba[1], liczba[0]);	
	return 0;
}