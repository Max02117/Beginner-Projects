#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Структура для хранения кандидата
typedef struct {
    char *name;
    int votes;
} Candidate;

int main(int argc, char *argv[]) {
    // Проверка количества аргументов
    if (argc < 2) {
    printf("Ошибка ! Используйте:\nmake plurality.c\n./plurality [кандидат1] [кандидат2] ...\n");
    return 1;
    }
    
    // Динамическое выделение памяти под массив
    int candidate_count = argc - 1;
    Candidate *candidates = malloc(candidate_count * sizeof(Candidate));
    if (candidates == NULL) {  
        printf("Ошибка выделения памяти!\n");  
        exit(1);  
    }

    // Инициализация кандидатов
    for (int i = 0; i < candidate_count; i++) {
        candidates[i].name = argv[i+1];
        candidates[i].votes = 0;
    }

    // Получение голосов
    int voter_count;
    printf("Количество голосующих: ");
    if (scanf("%d", &voter_count) != 1 || voter_count < 1) {
        printf("Ошибка: введите целое число больше 0\n");
        free(candidates);
        return 1;
    }

    for (int i = 0; i < voter_count; i++) {
        char name[100];
        printf("Голос %d/%d: Имя кандидата: ", i+1, voter_count);
        scanf("%99s", name);
    
        int found = 0;
        for (int j = 0; j < candidate_count; j++) {
            if (strcmp(name, candidates[j].name) == 0) {
                candidates[j].votes++;
                found = 1;
                break;
            }
        }
        if (!found) printf("Недействительный голос.\n");
    }

    // Определение победителя
    int max_votes = 0;
    for (int i = 0; i < candidate_count; i++) {
        if (candidates[i].votes > max_votes) {
            max_votes = candidates[i].votes;
        }
    }

    // Вывод результата
    printf("\nРезультаты выборов:\n");
    for (int i = 0; i < candidate_count; i++) {
        if (candidates[i].votes == max_votes) {
            printf("%s\n", candidates[i].name);
        }
    }

    free (candidates);
    return 0;
}