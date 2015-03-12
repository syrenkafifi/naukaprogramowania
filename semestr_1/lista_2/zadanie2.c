#include <stdio.h>

int  main(void){
	/*
		zmodyfikujemy program z poprzedniego zadania
		tylko jak tu sprawdzic by pracowac na liczbach ujemnych?:O

	*/

	int liczba; 
	int wartosc_absolutna;

	//prosze uzytkownika o liczbe
	printf("Podaj liczbę : ");

	//czytam co uzytkownik wpisal analogicznie jak robilismy to w programach z listy numer jeden
	scanf("%d", &liczba);

	/*
		mamy liczbę
		nasza logika z poprzedniego zadania działa tylko dla liczb dodatnich

		ojej a teraż może być ujemna liczba :O

		co zrobić ?:>

		zdradzę Ci moja droga Magdaleno solucje tudzież pomysł jak to się mówi
		
		skorzystamy z wartosci absolutnej. Liczy się ją tak
		Jeżeli liczba jest mniejsza od zera pomnóż ją przez minus jeden
		o np. tak liczba = liczba * (-1)

		ale pamietaj tylko ze mozesz to zastosować tylko dla liczb ujemnych

		jak wpiszesz dotatnią to popsujesz. Co w zwiazku z tym?

		musisz użyć instrukcji warunkowej i jezeli jest ujemna to mnoz
		jak jest dotatnia to nic nie rob tylko przepisz wartosc_absolutna = liczba

		pojedynczy if else:)
	*/

	if (liczba < 0){
		wartosc_absolutna = liczba * (-1);
	}else
	{
		wartosc_absolutna = liczba;
	}

	// to jest w zasadzie cala logika potrzebna do programu numer 1
	// wszedzie tam gdzie bedzie potrzeba wykorzystać kod z poprzedniego zadania ten kod będzie napisany przeze mnie
	// mozesz sobie siedzac nad jednym zadaniem zobaczyć jak powinno się je rozwiązać, ale lepiej próbuj sama
	// przy czym jeżeli Twoje rozwiazanie jest dobre i też działa to ok. JEST OK. JEEESTTT BARDZO OK :)
	// z reguły istnieje kilka różnych rozwiązań :)
	// jedyna roznica ze zamiast liczby sprawdzam wartosc absolutna

	if(wartosc_absolutna > 999){
		printf("Liczba %d sklada się z wiecej niż 3 cyfr\n", liczba);	
	}else {
		if(wartosc_absolutna > 99){
			printf("Liczba %d ma 3 cyfry.\n", liczba);
		}else{
			if(wartosc_absolutna > 9){
				printf("Liczba %d ma 2 cyfry.\n", liczba);
			}else{
				printf("Liczba %d ma 1 cyfre.\n", liczba);
			}
		}
	}
	return 0;
};