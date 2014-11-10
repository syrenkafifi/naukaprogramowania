#include "stdio.h"
#define PI 3.14159 

int main(){
	float objetosc;
	float promien;

	printf("podaj promień : \n");
	scanf("%f", &promien);

	objetosc = 4/3*PI*promien*promien*promien;
	printf("Objętość kuli o promieniu %.2f wynosi : %.2f \n", promien, objetosc);

	return 0;
}