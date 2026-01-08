#include <stdio.h>
#include <string.h>
#include <ctype.h>

int points_en[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int points_ru[33] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 2};

int compute_score(char word[]);

int main(void) {
    char word1[100];
    char word2[100];
    
    printf(" Игра \"Scrabble\"\n Правило игры:\n Каждый игрок поочередно вводит АНГЛИЙСКОЕ слово. Слово оце-\nнивается по очкам, которые зависят от букв (например, 'A' \nстоит 1 очко, 'B' — 3 очка и т. д.). Игрок, чье слово набра-\nло больше очков, побеждает. В случае равенства — ничья.\n\n");
    
    printf("Игрок 1, введите слово: ");
    scanf("%s", word1);
    for (int i = 0; i < strlen(word1); i++) {
        if (!isalpha(word1[i])) {
            printf("Ошибка, недопустимые символы !\n");
            return 1;
        }
    }
    printf("Игрок 2, введите слово: ");
    scanf("%s", word2);
    for (int i = 0; i < strlen(word2); i++) {
        if (!isalpha(word2[i])) {
            printf("Ошибка, недопустимые символы !\n");
            return 1;
        }
    }
    
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    
    if (score1 > score2) {
        printf("Игрок 1 победил !\n");
    } 
    else if (score1 < score2) {
        printf("Игрок 2 победил !\n");
    } else {
        printf("Ничья !\n");
    }
}

int compute_score(char word[]) {
    int score = 0;
    
    
    for (int i = 0, len = strlen(word); i < len; i++) {
        if (isupper(word[i])) {
            score += points_en[word[i] - 'A'];
        } else {
            score += points_en[word[i] - 'a'];
        }
        }
    return score;
}