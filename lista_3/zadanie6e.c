#include <stdio.h>

int main(void){
	int i, j;

	for(j=0; j<5; j++){
		for(i=0+j; i-j<7; i++){
			if(i%2==0){
				putchar('X');	
			}else{
				putchar(' ');
			}
		}
		putchar('\n');
	}

	// for(i=0; i<5; i++){
	// 	for(j=0; j<i; j++) {
	// 		putchar(' ');
	// 	}
	// 	for(j=5; j>i; j--) {
	// 		putchar('X');
	// 	}
	// 	putchar('\n');
	// }

	

	return 0;
}