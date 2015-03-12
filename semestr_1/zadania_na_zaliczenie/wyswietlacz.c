#include <stdio.h>
#define MAX_DIGITS 2 // maksymalna liczba znakow na wyswietlaczu

int main(void){
	// deklarujemy zmienna tekstowa w ktorej przechowamy liczba do wyswietlenia 
	// jest to zmienna nie obrobiona dlatego ma prefix raw_ poniewaz moze zawierac jakies litery lub znaki specjalne
    char *raw_liczba; 

    // deklarujemy zmienna gdzie bedziemy trzymac juz czysty tekst z cyframi
    char liczba[MAX_DIGITS];

    // tworzymy zmienna mowiaca nam ile jest w sumie liczb w tablicy liczba
	int liczba_cyfr;

    // zmienne iteracyjne (taki liczniki) -- pomocnik przy petli for
    int i; 

    /* 	tworzymy tablice do wyswietlania poszczegolnych segmentow liczby
		liczby skladaja sie ze znaków _ i | ktore sa wyswietlane w odpowiednich segmentach
		jezeli pod danym indeksem w wewnetrznej tablicy jest 1 tzn ze ten segmen bedziemy wyswietlac
		i tak np 8 sklada sie zapalonych wszstkich segmentow
		segmenty ukladaja sie tak
		 _			segment 0
		|_|			segment 1 segment 2 segment 3
		|_|			segment 4 segment 5 segment 6

		a 3

		_			segment 0
		_|			segment 2 segment 3 (segment 1 nieaktywny)
		_|			segment 5 segment 6 (segment 4 nieaktywny)

	*/
    int segm[10][7] = {
    	//	{0,1,2,3,4,5,6} --- takie segmenty
        	{1,1,0,1,1,1,1}, //0
        	{0,0,0,1,0,0,1}, //1
        	{1,0,1,1,1,1,0}, //2
        	{1,0,1,1,0,1,1}, //3
        	{0,1,1,1,0,0,1}, //4
        	{1,1,1,0,0,1,1}, //5
        	{1,1,1,0,1,1,1}, //6 
        	{1,0,0,1,0,0,1}, //7 
        	{1,1,1,1,1,1,1}, //8
        	{1,1,1,1,0,1,1}  //9
    };

    // informujemy o rozdzielczosci wyswietlacza
    printf("MAX_DIGITS - %d\n", MAX_DIGITS);
	//prosimy o podanie liczby ktora chcemy wyswietlic
    printf("Podaj liczbę: ");
    scanf("%ms", &raw_liczba); // zapisujemy liczbe


    // filtrujemy tekst z liter i znakow specjalnych
    // tylko cyfry ktore w kodzie ascii maja wartosc od 48 dla zera i 57 dla 9
    // warunkiem zakonczenia tej petli jest przejscie przez wszystkie znaki z raw liczba i<sizeof(raw_liczba)
    // lub przekroczenie maksymalnej wartosci cyfr dla wyswietlacza j<MAX_DIGITS
    // co kazda iteracje petli zwiekszamy licznik i
    for(i = 0, liczba_cyfr=0; i<sizeof(raw_liczba) && liczba_cyfr<MAX_DIGITS; i++) 
    {
    	// jezeli znak jest w przedziale od 48 do 57 to jest to liczba
    	if(48<=raw_liczba[i] && raw_liczba[i]<=57){
    		liczba[liczba_cyfr] = raw_liczba[i];	// do tablicy liczba wpisujemy znak z raw_liczba
    		liczba_cyfr++; // zwiekszamy licznik j ktory pomaga nam sie odwolywac do tablicy liczba, tak aby zapisywac na kolejnym wolnym miejscu
    	}
    }

    // zapalamy ewentualne segment 0
	for(i=0; i<liczba_cyfr; i++){
			printf(" ");
			// w jezyku c 1 jest rowniez rownoznaczne z wartoscia true a 0 jako false
			// liczba[i] -48 powoduje ze z wartosci ascii przechodzimy do zwyklej liczby
			// segm[liczba[i]-48] bieremy tablice dla itej cyfry z tablicy liczba np jezeli i=1 a liczba = "13" to wezmiemy 2 cyfre a wiec znak '3' co w ascii rowna sie 51
			// po odjeciu 48 otrzymamy 3
			// dla segm[3] pierwszy element wewnetrznej tablicy jest 1 a wiec true czyli wyswietlmy segment
    		if(segm[liczba[i]-48][0])
    		{
    			printf("_"); // jezeli w liczbie wyswietlamy dany segment if jest 1 czyli true i wyswietlamy segment - w tym przypadkud dla segmentu 0 bedzie to _
    		}
    		else
    		{
    			printf(" "); // jak nie to zostawiamy puste miejsce
    		}
    		printf(" ");
    		printf(" ");
	}
	printf("\n");

	// zapalamy ewentualne segmenty 1 2 3
	for(i=0; i<liczba_cyfr; i++){
    		if(segm[liczba[i]-48][1]){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][2]){
    			printf("_");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][3]){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		printf(" ");
    		
	}


	printf("\n");

	// zapalamy ewentualne segment 4 5 6
	for(i=0; i<liczba_cyfr; i++){
    		if(segm[liczba[i]-48][4]){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][5]){
    			printf("_");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][6]){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		printf(" ");
	}



	printf("\n");



	return 1;
}