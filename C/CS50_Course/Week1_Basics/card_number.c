#include <stdio.h>
#include <string.h>

int main(void) {
    long number;
    printf("Введите номер карты: ");
    scanf("%ld", &number);
    int count = 0;
    long orig_number = number;
    
    while (number > 0) {
        number = number / 10;
        count++;
    }
    
    // Проверка длины номера карты
    if (count != 13 && count != 15 && count != 16) {
        printf("Номер %ld не существует\n", orig_number);
        return 0;
    }
    
    char card[12];
    long temp_number = orig_number;
    
    // Visa 13
    if (count == 13) {
        if (temp_number  / 1000000000000 == 4) {
            strcpy(card, "Visa");
        } else {
            printf("Номер %ld не существует\n", orig_number);
            return 0;
        }
    }
    // Visa 16
    else if (count == 16) {
        if (temp_number / 1000000000000000 == 4) {
            strcpy(card, "Visa");
        } 
        // MasterCard 16
        else if (temp_number / 100000000000000 >= 51 && temp_number / 100000000000000 <= 55) {
            strcpy(card, "MasterCard");
        } 
        // МИР 16
        else if (temp_number / 100000000000000 == 22) {
            strcpy(card, "МИР");
        } else {
            printf("Номер %ld не существует\n", orig_number);
            return 0;
        }
    }
    // American Express 15
    else if (count == 15) {
        if (temp_number / 10000000000000 == 34 || temp_number / 10000000000000 == 37) {
            strcpy(card, "AmericanExpress");
        } else {
            printf("Номер %ld не существует\n", orig_number);
            return 0;
        }
    }

    // Алгоритм луна
    int sum = 0;
    int pos = 1;
    int digit;
    
    for(; temp_number > 0; temp_number /= 10) {
        digit = temp_number % 10;
        
        if(pos % 2 == 0) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        pos++;
    }
    if (sum % 10 == 0) { 
        printf("Карта %s действительна\n", card);
    } else {
        printf("Номер %ld не существует\n", orig_number);
    }
    return 0;
}