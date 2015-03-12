#include <stdio.h>

void funkcja(int a){
	a++;
}

void tablica(int tab[])
{
	int i;
	for(i = 0; i < sizeof(tab); i++)
	{
		tab[i]++;
	}
}



int main(void){

	int a = 1;
	int b = 1;
	int tabliczka[] = {1,2};
	int i;
	for(i = 0; i<2; i++)
	{
		printf("%d \n", tabliczka[i]);
	}
	printf("zmienna a %d \n", a);
	printf("zmienna b %d \n", b);
	funkcja(a);
	printf("zmienna a %d \n", a);
	printf("zmienna b %d \n", b);
	tablica(tabliczka);
for(i = 0; i<2; i++)
	{
		printf("%d \n", tabliczka[i]);
	}
	
}
