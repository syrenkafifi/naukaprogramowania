#include <stdio.h>
#include <ctype.h>

int main(void){
	// deklarujemy zmienne
    int przesuniecie = 1; // deklarujemy przesyniecie
    char *napis; // deklarujemy zmienna w ktorej przechowamy napis do zaszyfrowania
	int ilosc_znakow; // zmienna przechowująca dlugosc napisu - przyda się przy petli for
    int i; // zmienna iteracyjna (taki licznik) -- pomocnik przy petli for
	char znak; // zmienna robocza ktora bedziemy wykorzystywac w funkcji for
	char znak_po_przesunieciu; // j.w.

	// prosimy o podania przesuniecia
    printf("Program koduje szyfrem cezara\n ---podaj dlugosc przesuniec (domyslnie=1):\n");
    scanf("%d", &przesuniecie); // zapisujemy przesuniecie


	// prosimy o podanie tekstu do zakdowoania
    printf("Podaj tekst do zakodowania:\n");
    scanf("%ms", &napis); // zapisujemy tekst do zakodowania

	// napis = "magda" 
	// napis[0] = 'm'
	// napis[1] = 'a'
	// napis[2] = 'g'

    ilosc_znakow = sizeof(napis); // sprawdzamy dlugosc tekstu do zakodowania zeby wiedziec ile razy musimy wykonac szacher macher w forze (ile razy petla ma przejsc)
    for(i=0; i<ilosc_znakow; i++)
	{
		znak = napis[i]; // zapisujemy sobie jedna z napisu do zmiennej znak
		// porownujemy znak z tablica ascii 
		// http://pl.wikipedia.org/wiki/ASCII
		// sprawdzamy czy znak miesci sie w zakresie dla znaków od A (A=65) do Z (Z=90)
		if( (65<=znak) && (znak<=90) )
		{
			// jezeli znak jest w zakresie to dodajemy do niego przesuniecie 
	    	znak_po_przesunieciu = znak + przesuniecie; // o tu
			// moze zdarzyc sie sytuacja ze po przesunieciu wyjdziemy po za zakres 
			//(np znak= Z czyli 90 a przesuniecie bylo 1 i mamy znak_po_przesunieciu=91 co rowna sie klamerka i tu mozesz skonczyc)
			// jak dla goscia to mozesz to dale usunac
	    	if(znak_po_przesunieciu > 90)
			{
				// ambitny wariant
				znak_po_przesunieciu = 64 + znak_po_przesunieciu % 90; // 91 % (modulo - reszta z dzielenia) 90 = 1
				// czyli przesuniecie o 1 w tym przypadku, ale ze nie startujemy od zera a od 65 to daje 64
            }
			else
			{
				// w przypadku dekodowania (ujemnego przesuniecia)
				if(znak_po_przesunieciu < 65)
				{
					znak_po_przesunieciu = 91 - (65-znak_po_przesunieciu); // wracamy na gore zakresu
				}
			}
        }
		else
		{
			// tak jak wyzej tylko dla malych liter
			// dla znakow od a=97 do z=122
			if((97<=znak)&&(znak<=122))
			{
	    		znak_po_przesunieciu = znak + przesuniecie;
	    			if(znak_po_przesunieciu > 122)
					{
    					znak_po_przesunieciu = 96 + znak_po_przesunieciu % 122; 
            		} 
					else
					{
						// w przypadku dekodowania (ujemnego przesuniecia)
						if(znak_po_przesunieciu < 97)
						{
							znak_po_przesunieciu = 123 - (97-znak_po_przesunieciu); // wracamy na gore zakresu
						}
					}
    		}
			else
			{
				// dla pozostałych, specjalnych i liczb nic nie robimy
				znak_po_przesunieciu = znak;
			}	
		}
		// nie chcialo mi sie deklarowac drugiej tablicy i zapisuje na miejscu starego znaku znak "zakdoowany"
		napis[i] = znak_po_przesunieciu;
	}
	printf("Tekst po przesunieciu znaków o %d z uwzględnieniem zakresów znaków ascii:\n", przesuniecie);
	printf("%s\n",napis);
    return 1;
}
