#include <stdio.h>

int main(void){
	int i, j;

	for(i=5; i>0; i--){
		for(j=0; j<i; j++) {
			putchar('X');
		}
		putchar('\n');
	}

	return 0;
}