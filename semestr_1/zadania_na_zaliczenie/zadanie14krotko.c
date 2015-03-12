#include <stdio.h>
#include <stdlib.h>


int main(void){
	char tablica_znakow[] = "abcd";
	srand ( time(NULL) );
	char losowy_element = tablica_znakow[rand()%(sizeof(tablica_znakow)-1)];
	// zwracamy losowy element
	printf("%c\n", losowy_element);

}
