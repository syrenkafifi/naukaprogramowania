#include <stdio.h>

int  main(void){
	int n;
	int i;

	printf("Podaj liczbę.\n");

	scanf("%d", &n);


	/* w funkcji for mozesz wrzuca bardziej skomplikowane przypadki :)

		nie i rowna sie 2

		warunek bedzie i * i <= n

		nie musimy skakać co jeden za pomoca i++

		mozemy skakać co pięć za pomocą i = i +5

		no ale my mamy skakać co parzyste wartosci wiec 5 sie nie nada :()
	*/
	for(stan poczatkowy; warunek ; skok ){
		printf("%d\t%d\n",i, i*i);
	}

	

	return 0;
};