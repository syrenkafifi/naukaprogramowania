#include <stdio.h>

float poleTr(int a, int h){
	float pole;
	pole = 0.5 * a * h;

	return pole;
}

int main(void){
	int a;
	int h;
	float pole;

	printf("Program obliczający pole trojkąta\n");
	printf("Podaj długość podstawy : ");
	scanf("%i", &a);
	printf("Podaj wysokość : ");
	scanf("%i", &h);

	//tutaj policzymy pole
	
	pole = poleTr(a,h);

	printf("Pole tego trojkąta jest równe: %.3f\n", pole);
	return 1;
}