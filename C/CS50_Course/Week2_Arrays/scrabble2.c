#include <stdio.h>
#include <wchar.h>

int points_en[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int points_ru[33] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 1};

int compute_score(wchar_t word[]);

int main(void) {
    wchar_t word1[100];
    wchar_t word2[100];
    
    printf("Игрок 1, введите слово: ");
    wscanf(L"%ls", word1);
    printf("Игрок 2, введите слово: ");
    wscanf(L"%ls", word2);
    
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    
    printf("У игрока 1: %d очков\n", score1);
    printf("У игрока 2: %d очков\n", score2);
    
    if (score1 > score2) {
        printf("Игрок 1 победил !\n");
    }
    else if (score1 < score2) {
        printf("Игрок 2 победил !\n");
    } else {
        printf("Ничья !\n");
    }
}

int compute_score(wchar_t word[]) {
    int score = 0;
    
    for (int i = 0; i < wcslen(word); i++) {
        //Английские буквы
        if (word[i] >= L'A' && word[i] <= L'Z') {
            score += points_en[word[i] - L'A'];
        }
        else if (word[i] >= L'a' && word[i] <= L'z') {
            score += points_en[word[i] - L'a'];
        }
        
        //Русские буквы 
        else if (word[i] >= L'А' && word[i] <= L'Я') {
            score += points_ru[word[i] - L'А'];
        }
        else if (word[i] >= L'а' && word[i] <= L'я') {
            score += points_ru[word[i] - L'а'];
        }
        else if (word[i] == L'Ё' || word[i] == L'ё') {
            score += points_ru[6];
        }
    }
    return score;
}