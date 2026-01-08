#include <stdio.h>
#include <ctype.h>
#include <string.h>

int validate_key(char *key);
void encrypt_text(char *plaintext, char *key);

int main(int argc, char *argv[]) {
    // Проверка корректности количества аргументов (Checking the correctness of the number of arguments)
    if (argc != 2) {
        printf("Ошибка: используйте ./substitution <ключ>\n");
        return 1;
    }

    // Валидация формата ключа (key format validation)
    if (!validate_key(argv[1])) {
        return 1;
    }

    // Ввод текста и удаление перевода строки (Get input and remove trailing newline)
    printf("Введите текст: ");
    char plaintext[1024];
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = '\0';

    // Вывод шифрования (print result)
    printf("Зашифрованный текст: ");
    encrypt_text(plaintext, argv[1]);
    printf("\n");

    return 0;
}

int validate_key(char *key) {
    // Проверка длины ключа (Validate key length)
    if(strlen(key) != 26) {
        printf("Ошибка: ключ должен состоять из 26 символов.\n");
        return 0;
    }

    int used[26] = {0};
    for (int i = 0; i < 26; i++) {
        //Проверка на небуквенных символов (Check for non-letter characters)
        if (!isalpha(key[i])) {
            printf("Ошибка: недопустимый символ в ключе.\n");
            return 0;
        }

        // Конвертация символа в индекс алфавита и проверка дубликатов (Convert to index and check duplicates)
        int index = toupper(key[i]) - 'A';
        if (used[index]) {
            printf("Ошибка: Повторяющиеся буквы в ключе.\n");
            return 0;
        }
        used[index] = 1;
    }
    return 1;
}

void encrypt_text(char *plaintext, char *key) {
    for (int i = 0; plaintext[i] != '\0'; i++) {
        if (isalpha(plaintext[i])) {
            // Определение позиции символа, для замены (Calculate substitution index)
            int offset  = toupper(plaintext[i]) - 'A';

            // Заменить, сохранив регистр. (Substitute preserving case)
            char cipher_char = key[offset];
            printf("%c", islower(plaintext[i]) ? tolower(cipher_char) : toupper(cipher_char)); 
        }
        else {
            printf("%c", plaintext[i]);
        }
    }
}