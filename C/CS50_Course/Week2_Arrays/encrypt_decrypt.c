#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>

#define BUFFER_SIZE 1024
#define ENG_ALPHABET_SIZE 26
#define RUS_ALPHABET_SIZE 33

void decrypt(wchar_t *text, int key);
void encrypt(wchar_t *text, int key);

int main(void) {
    setlocale(LC_ALL, "");
    int choice;
    wprintf(L"1. Зашифровать текст.\n2. Расшифровать текст.\nВыберите '1' или '2': ");

    while (wscanf(L"%d", &choice) != 1 || (choice != 1 && choice != 2)) {
        wprintf(L"Ошибка: Введите '1' или '2': ");
        wint_t c;
        while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера
    }

    wint_t c;
    while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера после выбора

    // Динамическое выделение памяти
    wchar_t *text = (wchar_t *)malloc(BUFFER_SIZE * sizeof(wchar_t));
    if (!text) {
        wprintf(L"Ошибка: не удалось выделить память!\n");
        return 1;
    }

    if (choice == 1) {
        wprintf(L"Введите текст: ");
        fflush(stdout);
        if (fgetws(text, BUFFER_SIZE, stdin) == NULL) {
            wprintf(L"Ошибка: не удалось прочитать текст!\n");
            free(text);
            return 1;
        }
        size_t len = wcslen(text);
        if (len > 0 && text[len - 1] == L'\n') {
            text[len - 1] = L'\0'; // Удаление символа новой строки
        }

        int key;
        wprintf(L"Введите ключ: ");
        while (wscanf(L"%d", &key) != 1 || key <= 0) {
            wprintf(L"Ошибка: введите положительное число\n");
            while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера
            wprintf(L"Введите ключ: ");
        }
        while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера

        wprintf(L"Зашифрованный текст: ");
        encrypt(text, key);
    } else {
        wprintf(L"Введите зашифрованный текст: ");
        fflush(stdout);
        if (fgetws(text, BUFFER_SIZE, stdin) == NULL) {
            wprintf(L"Ошибка: не удалось прочитать текст!\n");
            free(text);
            return 1;
        }
        size_t len = wcslen(text);
        if (len > 0 && text[len - 1] == L'\n') {
            text[len - 1] = L'\0'; // Удаление символа новой строки
        }

        int key;
        wprintf(L"Введите ключ: ");
        while (wscanf(L"%d", &key) != 1 || key <= 0) {
            wprintf(L"Ошибка: введите положительное число\n");
            while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера
            wprintf(L"Введите ключ: ");
        }
        while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера

        wprintf(L"Расшифрованный текст: ");
        decrypt(text, key);
    }

    free(text);
    return 0;
}

// Шифрование
void encrypt(wchar_t *text, int key) {
    wchar_t result[BUFFER_SIZE] = {0};
    int index = 0;
    int flag = 0;

    for (int i = 0; text[i] != L'\0'; i++) {
        // Замена 'Ё' на 'Е'
        if (text[i] == L'Ё' || text[i] == L'ё') {
            if (text[i] == L'Ё') {
                text[i] = L'Е';
            } else {
                text[i] = L'е';
            }
            flag = 1;
        }

        // Английский алфавит
        if ((text[i] >= L'A' && text[i] <= L'Z') || (text[i] >= L'a' && text[i] <= L'z')) {
            int keyTemp = (key % ENG_ALPHABET_SIZE + ENG_ALPHABET_SIZE) % ENG_ALPHABET_SIZE;
            wchar_t offset = (text[i] >= L'a') ? L'a' : L'A';
            result[index++] = ((text[i] - offset + keyTemp) % ENG_ALPHABET_SIZE) + offset;
        }
        // Русский алфавит (заглавные)
        else if (text[i] >= L'А' && text[i] <= L'Я') {
            wchar_t offset = L'А';
            wchar_t formula = ((text[i] - offset + key + RUS_ALPHABET_SIZE) % RUS_ALPHABET_SIZE) + offset;

            if (formula == L'а') { // 'а' идет после 'Я' в Unicode
                formula = L'А';
                formula--;
            }

            if (flag == 1) { // Если была замена 'Ё'
                formula++;
                flag = 0;
            }

            int j = 0;
            if (text[i] > L'Е' && text[i] + key > L'Я') {
                formula++;
                j = 1;
            }

            if (formula == L'Ж') {
                formula = L'Ё';
            } else if ((text[i] < L'Ж' || j == 1) && formula >= L'Ж') {
                formula--;
            }
            if (formula == L'Џ') { // Перед 'А' идет 'Џ'
                formula = L'Я';
            }

            result[index++] = formula;
        }
        // Русский алфавит (строчные)
        else if (text[i] >= L'а' && text[i] <= L'я') {
            wchar_t offset = L'а';
            wchar_t formula = ((text[i] - offset + key + RUS_ALPHABET_SIZE) % RUS_ALPHABET_SIZE) + offset;

            if (formula == L'ѐ') { // 'ѐ' идет после 'я' в Unicode
                formula = L'а';
                formula--;
            }

            if (flag == 1) { // Если была замена 'ё'
                formula++;
                flag = 0;
            }

            int j = 0;
            if (text[i] > L'е' && text[i] + key > L'я') {
                formula++;
                j = 1;
            }

            if (formula == L'ж') {
                formula = L'ё';
            } else if ((text[i] < L'ж' || j == 1) && formula >= L'ж') {
                formula--;
            }
            if (formula == L'Я') { // Перед 'а' стоит 'Я' в Unicode
                formula = L'я';
            }

            result[index++] = formula;
        } else {
            result[index++] = text[i];
        }
    }
    wprintf(L"%ls\n", result);
}

// Расшифрование
void decrypt(wchar_t *text, int key) {
    wchar_t result[BUFFER_SIZE] = {0};
    int index = 0;
    int flag = 0;

    for (int i = 0; text[i] != L'\0'; i++) {
        // Замена 'Ё' на 'Ж'
        if (text[i] == L'Ё' || text[i] == L'ё') {
            if (text[i] == L'Ё') {
                text[i] = L'Ж';
            } else {
                text[i] = L'ж';
            }
            flag = 1;
        }

        // Английский алфавит
        if ((text[i] >= L'A' && text[i] <= L'Z') || (text[i] >= L'a' && text[i] <= L'z')) {
            int keyTemp = (key % ENG_ALPHABET_SIZE + ENG_ALPHABET_SIZE) % ENG_ALPHABET_SIZE;
            wchar_t offset = (text[i] >= L'a') ? L'a' : L'A';
            result[index++] = ((text[i] - offset - keyTemp + ENG_ALPHABET_SIZE) % ENG_ALPHABET_SIZE) + offset;
        }
        // Русский алфавит (заглавные)
        else if (text[i] >= L'А' && text[i] <= L'Я') {
            wchar_t offset = L'А';
            wchar_t formula = ((text[i] - offset - (key % RUS_ALPHABET_SIZE) + RUS_ALPHABET_SIZE) % RUS_ALPHABET_SIZE) + offset;

            if (formula == L'а') { // 'а' идёт после 'Я' в Unicode
                formula = L'А';
                formula--;
            }

            if (flag == 1) { // Если была замена 'Ё'
                formula--;
                flag = 0;
            }

            int j = 0;
            if (text[i] <= L'Е' && text[i] - key < L'А') {
                formula--;
                j = 1;
            }

            if (formula == L'Е') {
                formula = L'Ё';
            } else if ((text[i] >= L'Ж' || j == 1) && formula <= L'Е') {
                formula++;
            }

            if (formula == L'Џ') { // 'Џ' находится перед 'А'
                formula = L'Я';
            }

            result[index++] = formula;
        }
        // Русский алфавит (строчные)
        else if (text[i] >= L'а' && text[i] <= L'я') {
            wchar_t offset = L'а';
            wchar_t formula = ((text[i] - offset - (key % RUS_ALPHABET_SIZE) + RUS_ALPHABET_SIZE) % RUS_ALPHABET_SIZE) + offset;

            if (formula == L'ѐ') { // 'ѐ' идет после 'я'
                formula = L'а';
                formula--;
            }

            if (flag == 1) {
                formula--;
                flag = 0;
            }

            int j = 0;
            if (text[i] < L'ж' && text[i] - key < L'а') {
                formula--;
                j = 1;
            }

            if (formula == L'е') {
                formula = L'ё';
            } else if ((text[i] >= L'ж' || j == 1) && formula <= L'е') {
                formula++;
            }

            if (formula == L'Я') { // 'я' находится перед 'А'
                formula = L'я';
            }

            result[index++] = formula;
        } else {
            result[index++] = text[i];
        }
    }
    wprintf(L"%ls\n", result);
}