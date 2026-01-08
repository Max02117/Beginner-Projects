// Upd 2.0: 1) Добавлена поддержка русского языка; 2) Добавлена обработка ошибки отсутствия знака препинания в конце; 3) Исправлен подсчет предложений; 4) увеличен массив до 1500 символов.

#include <stdio.h>
#include <wchar.h>
#include <wctype.h>
#include <math.h>

int main(void) {
    wchar_t text[1500];
    
    wprintf(L"Введите текст: ");
    fgetws(text, 1500, stdin);
    
    int letters = 0;
    int words = 0;
    int in_word = 0;
    int sentences = 0;
    int i = 0;
    int last_punctuation = 0;
    
    for (; text[i] != L'\0'; i++) {
        // Подсчет букв
        if (iswalpha(text[i])) {
            letters ++;
        }
        // Подсчет слов
        if (iswalpha(text[i]) && in_word == 0) {
            words ++;
            in_word = 1;
        }
        else if (!iswalpha(text[i])) {
            in_word = 0;
        }
        // Подсчет предложений
        if ((text[i] == L'.' || text[i] == L'!' || text[i] == L'?' || text[i] == L'…') && (last_punctuation == 0)) {
            sentences ++;
            last_punctuation = 1;
        }
        else if (iswspace(text[i])) {
            last_punctuation = 0;
        }
    }
    
    int punctuation = 0;
    if (sentences == 0 && letters > 0) {
        sentences ++;
        punctuation = 1;
    }
    
    printf("Символов: %d\n", i - 1);
    printf("Букв: %d\n", letters);
    printf("Слов: %d\n", words);
    printf("Предложений: %d\n\n", sentences);
    
    if (punctuation == 1) {
        printf("Грамматическая ошибка: отсуствует знак препинания в конце.\n\n");
    }
    
    if (i < 50) {
        printf("Текст меньше 50 символов.\nУровень: Дошкольный.\n");
        return 0;
    }
    
    float L = letters * 100 / words; // Букв на 100 слов
    float S = sentences * 100 / words; // Предложений на 100 слов
    
    float index = 0.0588 * L - 0.296 * S - 15.8;
    index = round(index);
    
    if (index > 16) {
        printf("Уровень: выше 11 класса.\n");
    }
    else if (index < 1) {
        printf("Уровень: Дошкольный.\n");
    } else {
        printf("Уровень: %d.\n", (int)index);
    }
}