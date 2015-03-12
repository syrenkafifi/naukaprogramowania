#include <stdio.h>

// deklaruję stałą N
#define N 5

int main(void)
{
	int tablica_a[N];
	int tablica_b[N];
	int i;
	printf("Podaj %d liczb dla tablicy a: \n",N);
	// jakiś szacher macher do wczytania // pomyslimy po
	for(i=0; i<N; i++)
	{
		 scanf("%i", &tablica_a[i]);
	}
	printf("\nWczytałem\n");
	printf("Kopiuje\n");
	// kopiowanie moja Krolewno // mamanama :P
	for(i=0; i<N; i++)
	{
		tablica_b[i] = tablica_a[i];
	}

		

	// szacher macher do wyswietlenia
	printf("Liczby z tablicy A : ");
	for(i=0; i<N; i++){
		printf("%d ", tablica_a[i]);
	}
	printf("\n");
	printf("Liczby z tablicy B : ");
	for(i=0; i<N; i++){
		printf("%d ", tablica_b[i]);
	}
	printf("\n");


}