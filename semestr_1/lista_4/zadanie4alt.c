#include <stdio.h>



int main(void)
{
	char *liczba;
	int wystapienia[10] = {0,0,0,0,0,0,0,0};
	int i;

	printf("Podaj liczbe\t:\t");
	scanf("%ms", &liczba);
	//liczba = "6233209";

	for(i=0; i<sizeof(liczba)-1; i++)
	{
		printf("%i - %i\n", i, liczba[i]-48);

		wystapienia[liczba[i]-48]++;
	}


	printf("Cyfra\t\t:\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n");
	printf("Wystąpienia\t:");
	for(i=0; i<10; i++){
		printf("\t%d", wystapienia[i]);
	}
	printf("\n");


}