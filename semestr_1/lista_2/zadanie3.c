#include <stdio.h>

int  main(void){
	// deklarujemy sobie zmienne w formacie 24 godzinnym
	int godzina_24;
	int minuta_24;

	// deklarujemy zmienne w formacie 12 godzinnym
	int godzina_12;
	int minuta_12;

	// prosimy użytkownika by podal nam liczby w formacie 24 godzinnym
	printf("Podaj godzinę w formacie 24 godzinnym (hh:mm): ");

	scanf("%d:%d", &godzina_24, &minuta_24);


	/* 
		teraz wchodza do akcji instrukcje warunkowe

		hmmm wiesz tak sobie mysle ze w zasadzie minuta_24 i minuta_12 to to samo wiec mozemy je przepisać do siebie

		minuta_12 = minuta_24

		tylko co z tymi godzinami hmmm

		jeżeli godzina_24 < 13
			to jestesmy w czasie AM
		w przeciwnym wypadku to
			w czasie PM	

	*/

	minuta_12 = minuta_24;
	// jezeli godzina_24 < 13
		godzina_12 = godzina_24;

		printf("Format 12 godzinny to: %d:%2d AM\n", godzina_12, minuta_12);
	// a jezeli nie to
		//pamietaj by od godziny 24 odjac 12 :)
		godzina_12 = godzina_24 - 12;
		printf("Format 12 godzinny to: %d:%2d PM\n", godzina_12, minuta_12);

			

	return 0;
};