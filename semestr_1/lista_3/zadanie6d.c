#include <stdio.h>

int main(void){
	int i, j;


	for(i=0; i<5; i++){
		for(j=0; j<i; j++) {
			putchar(' ');
		}
		for(j=5; j>i; j--) {
			putchar('X');
		}
		putchar('\n');
	}

	

	return 0;
}