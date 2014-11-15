#include <stdio.h>

int  main(void){

	// deklarujemy zmienne:

	int dzien;
	int miesiac;
	int rok;
	
	// do tej zmiennej zapiszemy miesiac, jest to wskaznik na zmienna typu char// narazie nie zaprzataj sobie tym glowy, wskazniki w C
	// to grubszy temat i razem przerobimy, szczerze mówiąc sam bym musial sobie troche przypomnieć. w normalnych jezykach jak java czy
	// python nie ma takich problemow :)
	char * miesiac_slowem;

	// czytamy dzien miesiąc i rok
	printf("Podaj date (dd/mm/rrrr): ");
	scanf("%d/%d/%d", &dzien, &miesiac, &rok);

	/*
		instrukcja switch to taki przelacznik. mamy jakis warunek i patrzymy czy co zrobic dla konkretnego przypadku
		http://pl.wikipedia.org/wiki/C_(j%C4%99zyk_programowania)

		np.
		int x=1
		switch(x){
  			case 0:
  				printf("zero");
  			case 1:
    			printf("jeden");
    			prinft("trololo");
    			break;
  			case 2:
    			printf("dwa");
    			break;
  			default:
  				TUTAJ WEJDZIEMY JAK SIE NIE DOPASUJEMY DO WZORCA
    			printf("coś innego");
    			break;
    	}

    	innymi slowy probujemy dopasować się wzorca a jak nie to trololo :P
}
	*/

	switch(miesiac){
		case 1:
			miesiac_slowem = "stycznia";
			break;
		case 2:
			miesiac_slowem = "lutego";
			break;
		// dopisz resztę
		default:
			miesiac_slowem = "trololo:P";
			break;
	}

	printf("Zapis urzędowy: %d %s %d r.\n", dzien, miesiac_slowem, rok);

	// jezeli chcesz zobaczyć jak można to było zrobić bez switcha to otwórz brogram zadanie4_alternatywa.c
};