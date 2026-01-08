#include <stdio.h>

int main(void)
{
    int высота;
    do {
        printf("Введите высоту: ");
        scanf("%d", &высота);
    } while (высота <= 0);
    
    for(int i = 0; i < высота; i++) {
        for(int j = 0; j < высота - i - 1; j++) {
            printf(" ");
        }
        for(int k = 0; k <= i; k++) {
            printf("#");
        }
        printf("\n");
    }
}