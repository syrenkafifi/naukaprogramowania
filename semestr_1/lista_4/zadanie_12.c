#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomPrzedzialy(int n, int m){
	srand ( time(NULL) );
  	int random_number = rand();
  	int przedzial = m - n;
  	int pomocnik = random_number % przedzial;
	return n+pomocnik;
}

int rzut(void){

	return randomPrzedzialy(1,6);
}

int main(void){
	int wyniki[7] = {0,0,0,0,0,0,0};
	int i;

	for(i = 0; i < 6000; i++){

		int pojedynczy_rzut = rzut();
		wyniki[pojedynczy_rzut-1] = wyniki[pojedynczy_rzut-1] + 1;
	}

	printf("1 wypadla %d razy.\n", wyniki[1]);
	printf("2 wypadla %d razy.\n", wyniki[2]);
	printf("3 wypadla %d razy.\n", wyniki[3]);
	printf("4 wypadla %d razy.\n", wyniki[4]);
	printf("5 wypadla %d razy.\n", wyniki[5]);
	printf("6 wypadla %d razy.\n", wyniki[6]);
}
