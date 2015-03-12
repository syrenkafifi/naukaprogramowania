#include <stdio.h>
#define PI 3.14159

int main (void){
	float r;
	float pole_kola;

printf("podaj promien koła : "); 
scanf("%f", &r);
pole_kola = PI * r * r;

printf("pole koła o promieniu %2.f wynosi : %1.2f \n" , r, pole_kola );

return 0;
}
