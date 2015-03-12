#include <stdio.h>

int  main(void){
	int liczba_dni_w_miesiacu;
	int start_miesiaca;
	int i;

	printf("Podaj liczbe dni w miesiacu: ");
	scanf("%d", &liczba_dni_w_miesiacu);
	printf("Podaj dzien od ktorego zaczyna się miesiąc (1-Poniedzielek, 7-Niedziela): ");
	scanf("%d", &start_miesiaca);

	// najpierw wypiszemy puste dni
	// jezeli miesiac zaczyna sie od poniedzialku to zadnego pustego dnia nie wypiszemy, a jezeli od niedzieli to wczesniej 
	// musimy napisac 6 pustych tabow

	for(i=start_miesiaca;i>1;i--){
		printf("\t");
	}

	//teraz wypisujemy cyfry
	for(i=1; i<=liczba_dni_w_miesiacu; i++){
		printf("\t%d", i);
		//musimy sprawdzic czy weekend nam sie nie konczy i przejsc do nowej linii, uzyjemy dzielenia modulo czyli
		// %
		if(((i+start_miesiaca-1) % 7) == 0){
			printf("\n");
		}
	}

	return 0;
};