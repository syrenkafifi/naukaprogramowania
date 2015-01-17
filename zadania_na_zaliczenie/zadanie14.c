#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomPrzedzialy(int n, int m){
	srand ( time(NULL) ); // ustawiamy generator
  	int random_number = rand(); // generujemy losowa liczbe
  	int przedzial = m - n; // ustawiamy przedzial np m=20 n = 13 czyli przedzial rowna 7
  	int pomocnik = random_number % przedzial; // losowa liczbe (bardzo duza) ustawiam tak by miescila mi sie  przedziale od 0 do 7
	return n+pomocnik; // do poczatkowego przedzialu (n) dodaje losowa wartosc pomocnika
}


int main(void){
	char tablica_znakow[] = "abcd";
	int dlugosc_tablicy = sizeof(tablica_znakow);
	int n=0; // bo pierwszy element jest indeksowany z 0
	int m=dlugosc_tablicy - 1; // bo liczymy od 0 czyli np dla tablicy o dlugosci 5 ostatni element ma indeks 4
	int losowowy_indeks = randomPrzedzialy(n,m); // z wykorzystaniem naszej funkcji szukamy losowego indeksu w przedziale od n=0 i m=liczba_znakow - 1
	char losowy_element = tablica_znakow[losowowy_indeks];
	// zwracamy losowy element
	printf("%c\n", losowy_element);

}
