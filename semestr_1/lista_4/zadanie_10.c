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
	int wynik_rzutu = rzut();

	printf("wynik rzutu na sześciennej kostce wynosi: %d.\n", wynik_rzutu);
}
