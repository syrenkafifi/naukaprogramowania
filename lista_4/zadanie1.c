#include <stdio.h>

// deklaruję stałą N
#define N 5

int main(void)
{
	int tablica[N];
	int i;
	tablica[0] = 12;
	tablica[1] = 45;
	tablica[2] = 63;
	tablica[3] = 8;
	tablica[4] = 1;
	printf("Podaj %d liczb : \n",N);
	// jakiś szacher macher do wczytania // pomyslimy po
	for(i=0; i<N; i++)
	{
		 scanf("%i", &tablica[i]);
	}

	// szacher macher do wyswietlenia
	printf("Liczby wspak : ");
	for(i=N-1; i>=0; i--){
		printf("%d ", tablica[i]);
	}
	printf("\n");


}