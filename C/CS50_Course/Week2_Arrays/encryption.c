#include <stdio.h>
#include <ctype.h>
#include <wchar.h>

void encrypt(wchar_t *text, int key);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Ошибка: введите в терминале: ./Caesar *key*.\n");
        return 1;
    }
    for (int i = 0; argv[1][i] != '\0'; i++) {
        if (!isdigit(argv[1][i])) {
            printf("Ошибка: введите положительно число");
            return 1;
        }
    }
    int key = atoi(argv[1]);
    
    wchar_t plaintext[256];
    wprintf(L"Введите текст: ");
    fgetws(plaintext, sizeof(plaintext) / sizeof(wchar_t), stdin);
    plaintext[wcslen(plaintext) - 1] = L'\0';
    
    // Вывод зашифрованного текста
    wprintf(L"Зашифрованный текст: ");
    encrypt(plaintext, key);
    return 0;
}

void encrypt(wchar_t *text, int key) {
    for (int i = 0; text[i] != L'\0'; i++) {
        // Проверка на язык
        wchar_t offset;
        // Английский
        if (text[i] >= L'A' && text[i] <= L'z') {
            offset = isupper(text[i]) ? L'A' : L'a';
            wprintf(L"%lc", (text[i] - offset + key) % 26 + offset);
        }
        // Русский
        else if ((text[i] >= L'А' && text[i] <= L'я') || text[i] == L'Ё' || text[i] == L'ё') {
            // Замена Ё на Е
            if (text[i] == L'ё') {
                text[i] = L'е';
            }
            else if (text[i] == L'Ё') {
               text[i] = L'Е';
            }
            offset = isupper(text[i]) ? L'А' : L'а';
            wprintf(L"%lc", (text[i] - offset + key) % 32 + offset);
        }
    }
    printf("\n");
}