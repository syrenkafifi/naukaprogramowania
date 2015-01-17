#include <stdio.h>

// program do sortowania babelkowego
// napisany metoda kopiego pejsta z wiki
void sortowanie_babelkowe(int tablica[], int rozmiar_tablicy)
{
	int i, j, pomocnik;
	for (i = 0; i<rozmiar_tablicy-1; i++)
        {
		for (j=0; j<rozmiar_tablicy-1-i; j++)
		{
			if (tablica[j] > tablica[j+1])
			{
				pomocnik = tablica[j+1];
				tablica[j+1] = tablica[j];
				tablica[j] = pomocnik;
			}
		}
        }
}

/*
mamy t[] ={2,3,1}
pierwszy for zewnetrzny
i = 0
iterujemy w forze wewnetrznym
j = 0
porownujemy
t[0] > t[1]
2 > 3
jezeli to prawda to wchodzimy do ifa a jak nie to idziemy
przy j = 0 jest to nieprawda
wiec idziemy dalej
j = 1
sprawdzamy t[1] > t[2]
czyli czy 3 > 1
prawda a wiec idziemy wewnatrz ifa
do pomocnika zapisujemy t[j+1] czyli t[2] a wiec 1
do t[j+1] a wiec t[2] wpisujemy t[j] czyli t[1] czyli wspisujemy 3 tam gdzie byla 1
tablica wyglada teraz 2,3,3
na miejsce t[j] czyli t[1] wpisujemy dawna wartosc t[j+1] czyli t[2] a wiec 1
ten caly if sluzy zamianie kolejnosci elementow 
tablica jest 2,1,3
dla j=2 warunek nie wewnetrznego fora nie jest juz wykonwyany bo 2 < 3(rozmiar_tablicy) - 1 - 0 (bo i =0)

robimy druga iteracje (czyli drugie przejscie zewnetrznego fora)
i = 1
wchdozimy do wewnetrznego fora ktory bedzie sie wykonywal dla j < rozmiar tablicy - 1 i minus i a wiec j < 3(rozmiar tablicy) -1 -1 (aktualna wartosc i) j < 1
j = 0 czyli wykonujemy raz
sprawdzamy tak jak poprzednio
czy t[j] > t[j+1] a wiec t[0] > t[1]
czy 2 > 1 

no jest :D
ponownie dokokujemy zamiany
zwiekszamy j o jeden a wiec j=1 ... no ale dla j rownego 1 nie wykonujemy juz wewnetrznego fora
kolejna iteracja
i zwiekszamy o 1 czyli teraz i = 2
ale w zewnetrznym forze mamy warunek ze i < rozmiar tablicy -1 a arozmair tablicy wynosi 3 czyli i musi byc mniejsze od 3 od 1 a wiec od 2
i = 2 a wiec nie wykonujemy juz wiecej tej petli

koniec



*/

// nie tlumacze
void tablico_wyswietlacz(int tablica[], int rozmiar_tablicy){
	int i;
	for(i=0; i<rozmiar_tablicy; i++)
	{
		printf("%d  ", tablica[i]);
	}
	printf("\n");
}

int main(void){
	// definiuje sobie nieposortowana tablice
	int nieposortowana_tablica[] = {1,4,2,7,3,6,5,8,9,0};
	// sortowanie babelkowe 
	// http://pl.wikipedia.org/wiki/Sortowanie_b%C4%85belkowe

	// wyswietlam tablice nieposortowana za pomoca funkcji ktora sobie napisalem
	tablico_wyswietlacz(nieposortowana_tablica, 10);

	// dokonuje sortowania tablicy za pomoca funkcji sortowanie babelkowe
	sortowanie_babelkowe(nieposortowana_tablica, 10);

	// ponownie wyswietlam
	tablico_wyswietlacz(nieposortowana_tablica, 10);
	
	
}
