#include <stdio.h>

int  main(void){
	/*
		program na instrukcje warunkową if 

		instruckja if dziala nastepujaca:
		if(jakiś warunek np x==2){
			to wowczas robimy coś
		}

		może być też if else instrukcja
		if(warunek){
			robimy 1
		}else{
			robimy 2 // warunek z if nie zostal spelniony wiec wykonujemy cos innego
		}

		program nasz bedzie wygladać nastepujaco
		1. deklarujemy zmienna do ktorej zapiszemy to co nam uzytkownik poda
		2. prosimy uzytkownika za pomoca funkcji pritf aby podal jakas liczbe
		3. sprawdzamy
		if liczba wieksza od 999
			liczba sklada sie z wiekszej ilosci niz 3 cyfry
		else
			if liczba wieksza od 99
				liczba sklada sie z 3 cyfr
			else
				if liczba wieksza od 9
					liczba sklada sie z 2 cyfr
				else
					liczba sklada sie z 1 cyfry		
	*/

	int liczba; 


	//prosze uzytkownika o liczbe
	printf("Podaj liczbę : ");

	//czytam co uzytkownik wpisal analogicznie jak robilismy to w programach z listy numer jeden
	scanf("%d", &liczba);

	

	//tutaj sie uczysz instrukcji warunkowych wiec musisz sobie sama poradzić ;-) 


	// no ale jako kochajacy chlopak przygotowalem Ci dwa wyniki do wyswietlenia ;P
	printf("Liczba %d ma 1 cyfre.\n", liczba);
	printf("Liczba %d ma 2 cyfry.\n", liczba);
	printf("Liczba %d ma 3 cyfry.\n", liczba);
	printf("Liczba %d sklada się z wiecej niż 3 cyfr\n", liczba);		
	return 0;
};