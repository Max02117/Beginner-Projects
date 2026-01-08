#include <stdio.h>

int collatz(int n);

int main(void) {
    int n = 0;
    printf("Введите n: ");
    scanf("%d", &n);
    int steps = collatz(n);
    printf("Количество шагов: %d\n", steps);
    return 0;
}

int collatz(int n) {
    if (n == 1)
        return 0;
    else if (n % 2 == 0) 
        return 1 + collatz(n/2);
    else 
        return 1 + collatz(3 * n + 1);
}