#include <stdio.h>
#define MAX_DIGITS 18

int main(void){
    char *raw_liczba; // deklarujemy zmienna tekstowa w ktorej przechowamy liczba do wyswietlenia do zaszyfrowania
    int i,j; // zmienna iteracyjna (taki licznik) -- pomocnik przy petli for

	// prosimy o podanie liczby ktora chcemy wyswietlic
    //printf("Podaj liczbę: ");
    //scanf("%ms", &raw_liczba); // zapisujemy liczbe

    raw_liczba = "321-0479";
    char liczba[MAX_DIGITS];
    for(i = 0, j=0; i<sizeof(raw_liczba) && j<MAX_DIGITS; i++)
    {
    	if(48<=raw_liczba[i] && raw_liczba[i]<=57){
    		liczba[j] = raw_liczba[i];
    		j++;
    	}
    }
    int liczba_cyfr = j;
    i=j;
    for(;i<=MAX_DIGITS; i++)
    {
    	liczba[i] = 'n';
    }



        int segm[10][7] = {
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


    printf("%s\n", liczba);




	for(i=0; i<liczba_cyfr; i++){
			printf(" ");
    		if(segm[liczba[i]-48][0]==1)
    		{
    			printf("_");
    		}
    		else
    		{
    			printf(" ");
    		}
    		printf(" ");
    		printf(" ");
	}
	printf("\n");

	for(i=0; i<liczba_cyfr; i++){
    		if(segm[liczba[i]-48][1]==1){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][2]==1){
    			printf("_");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][3]==1){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		printf(" ");
    		
	}


	printf("\n");

	for(i=0; i<liczba_cyfr; i++){
    		if(segm[liczba[i]-48][4]==1){
    			printf("|");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][5]==1){
    			printf("_");
    		}
    		else{
    			printf(" ");
    		}
    		if(segm[liczba[i]-48][6]==1){
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