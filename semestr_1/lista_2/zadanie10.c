#include <stdio.h>

int  main(void){
	//program dziala na floatach bo widze ze prowadzacy z rozpedu tez dal zmienno przecikonwe liczby
	float liczba;
	float najwieksza_liczba = 0.0;



	/* przypomnijmu funcke while

		while(warunek){
			cos tam cos tam
		}

		jezeli warunek dam 1 to zeewaluuje sie to <- takie madre slowo, poprostu chodzi o to ze program to potraktuje jako
		prawde

		jest tu stala (1) i ona sie nie zmienia czyli zawsze bedzie to prawda i petla bedzie nie skonczona
		aby wyjsc z tej petli bedziemy musieli zastosowac instrukcje break;
		odpalamy ja tylko w sytuacji gdy liczba jest mniejsza lub rowna zero (czyli pakujemy tu if)
		podobnie pakujemy if aby sprawdzic czy najwieksza liczba jaka do tej pory przechowujemy jest wieksza od liczby
		ktora wlasnie wpisalismy (znowu if) jezeli wpisana liczba jest wieksza to zmieniamy wartosc ktora przechowywalismy
		w zmiennej najwieksza_liczba

		usunalem ify z programu tak ze petla obecnie wykona sie tylko raz

		popraw :)
	*/

	while(1){
		printf("Podaj liczbę: ");
		scanf("%f", &liczba);
		najwieksza_liczba = liczba;
		break;
	}

	printf("Najwieksza liczba z ciagu to: %f\n", najwieksza_liczba);

	

	return 0;
};