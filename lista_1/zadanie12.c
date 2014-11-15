#include "stdio.h"

int main(){
	int liczba;
	printf("Podaj liczbe pomiedzy 0 i 32767: ");
	scanf("%i", &liczba);

	// nie wiem jak to zrobic ale zapytalem googla
	//http://stackoverflow.com/questions/3649026/how-to-display-hexadecimal-numbers-in-c

	// ogolnie rzecz biorac inaczej sformatowalem ta liczbe :)
	printf("W zapisie ósemkowym to: %05x\n", liczba);	
	return 0;
}