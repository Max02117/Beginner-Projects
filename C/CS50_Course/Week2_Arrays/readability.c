//Программа анализирует текст, подсчитывая буквы, слова, предложения и символы. Затем вычисляет индекс читаемости по формуле Coleman-Liau для определения уровня образования.(только английский язык)

#include <stdio.h>
#include <ctype.h>
#include <math.h>

int main(void) {
    char text[1000];
    
    printf("Введите текст: ");
    fgets(text, 1000, stdin);
    
    int letters = 0; 
    
    int words = 0;
    int in_word = 0;
    
    int sentences = 0;
    
    int i = 0;
    for (; text[i] != '\0'; i++) {
        //Подсчет букв
        if (isalpha(text[i])) {
            letters ++;
        }
        //Подсчет слов
        if (isalpha(text[i]) && in_word == 0) {
            words ++;
            in_word = 1;
        }
        else if (!isalpha(text[i])) {
            in_word = 0;
        }
        //Подсчет предложений
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            sentences ++;
        }
    }
    printf("Количество символов: %d\n", i);
    printf("Букв: %d\n", letters);
    printf("Слов: %d\n", words);
    printf("Предложений: %d\n\n", sentences);
    
    //Индекс Coleman-Liau
   
    int L = letters * 100 / words; //букв на 100 слов
    int S = sentences * 100 / words; //предложений на 100 слов
    
    float index = 0.0588 * L - 0.296 * S - 15.8;
    index = round(index);
    
    if (i < 50) {
     printf("Текст меньше 50 Символов.\nУровень: Дошкольный");
    }
    else if (index >= 16) {
        printf("Уровень: выше 11 класса");
    }
    else if (index < 1) {
        printf("Уровень: дошкольный");
    } else {
        printf("Уровень: %d класс \n", (int)index);
    }
}