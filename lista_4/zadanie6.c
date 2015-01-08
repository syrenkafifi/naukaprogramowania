#include <stdio.h>

int sumTab(*int tablica){
	int i;
	int suma=0;
	for(int i = 0; i<sizeof(tablica); i++)
	{
		suma = suma + tablica[i];
	}
	return suma;
}

int main(void){
	int tablica[] = {1,2,3};
	int suma = sumTab(tablica);
	printf("%d\n", suma);
	return 0;
}