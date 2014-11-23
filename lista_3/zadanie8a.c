#include <stdio.h>
#include <string.h>

int main(void){
	int ilosc_znakow;
	char *napis;
	printf("Wpisz wiadomość : ");
	scanf("%as", &napis);
	ilosc_znakow = sizeof(napis);
	printf("Liczba znaków : %d\n", ilosc_znakow);

}