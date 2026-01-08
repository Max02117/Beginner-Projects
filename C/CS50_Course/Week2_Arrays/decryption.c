#include <stdio.h>
#include <ctype.h>
#include <wchar.h>

void decrypt(wchar_t *text, int key);

int main(void) {
    wchar_t text[256];
    wprintf(L"Введите текст: ");
    fgetws(text, sizeof(text) / sizeof(wchar_t), stdin);
    text[wcslen(text) - 1] = L'\0';
    
    int key;
    printf("Введите ключ: ");
    while (scanf("%d", &key) != 1 || key <= 0) {
        printf("Ошибка: введите положительное число\n");
        while (getchar() != '\n');  // Очистка буфера
        printf("Введите ключ: ");
    }
    
    // Вывод расшифрованного текста
    wprintf(L"Расшифрованный текст: ");
    decrypt(text, key);
    return 0;
}

void decrypt(wchar_t *text, int key) {
    for (int i = 0; text[i] != L'\0'; i++) {
        //Замена 'Ё' на 'Ж'
        if (text[i] == L'Ё' || text[i] == L'ё') {
            if (text[i] == L'Ё') {
                text[i] = L'Ж';
            } else {
                text[i] = L'ж';
            }
key --;
        }
        
        wchar_t offset;
        // Английский
        // Заглавные
        if (text[i] >= L'A' && text[i] <= L'Z') {
            offset = L'A';
            wprintf(L"%lc", ((text[i] - offset - key + 26) % 26) + offset);
        }
        // Строчные
        else if (text[i] >= L'a' && text[i] <= L'z') {
            offset = L'a';
            wprintf(L"%lc", ((text[i] - offset - key + 26) % 26) + offset);
        }
        
        // Русский
        // Заглавные
        else if (text[i] >= L'А' && text[i] <= L'Я') {
            offset = L'А';
            wprintf(L"%lc", ((text[i] - offset - key + 32) % 32) + offset);
        }
        // Строчные
        else if (text[i] >= L'а' && text[i] <= L'я') {
            offset = L'а';
            wprintf(L"%lc", ((text[i] - offset - key + 32) % 32) + offset);
        } else {
            wprintf(L"%lc", text[i]);
        }
    }
    printf("\n");
}