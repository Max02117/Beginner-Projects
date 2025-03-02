#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>

void decrypt(wchar_t *text, int key);
void encrypt(wchar_t *text, int key);

int main(void) {
    setlocale(LC_ALL, "");
    int choice;
    wprintf(L"1. Зашифровать текст.\n2. Расшифровать текст.\nВыберите '1' или '2': ");
  
    while (wscanf(L"%d", &choice) != 1 || (choice != 1 && choice != 2)) {
   	    wprintf(L"Ошибка: Введите '1' или '2': ");
        
        wint_t c;
        while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера в случае ошибкии
    }
    
    wint_t c;
    while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера
    
    // Динамическое выделение памяти
    wchar_t *text = (wchar_t *)malloc(1024 * sizeof(wchar_t));
    if (!text) {
    	wprintf(L"Ошибка выделения памяти !\n");
    	return 1;
    }
    
    if (choice == 1) {
        wprintf(L"Введите текст: ");
        fflush(stdout); // Очистка буфера
        if (fgetws(text, 1024, stdin) == NULL) { // Если обращение к несуществующим данным
            wprintf(L"Ошибка чтения текста!\n");
            free(text);
            return 1;
        }
        if (wcslen(text) > 0 && text[wcslen(text) - 1] == L'\n') {
            text[wcslen(text) - 1] = L'\0'; // Удаляет '\n' из введённой строки
        }

        int key;
        wprintf(L"Введите ключ: ");
        while (wscanf(L"%d", &key) != 1 || key <= 0) {
            wprintf(L"Ошибка: введите положительное число\n");
            while ((c = getwchar()) != L'\n' && c != WEOF); // Очистка буфера
            wprintf(L"Введите ключ: ");
        }
        while ((c = getwchar()) != L'\n' && c != WEOF);
        
        wprintf(L"Зашифрованный текст: ");
        encrypt(text, key);
    }
    else {
        wprintf(L"Введите зашифрованный текст: ");
        fflush(stdout); 
        if (fgetws(text, 1024, stdin) == NULL) { // Если обращение к несуществующим данным
            wprintf(L"Ошибка чтения текста!\n");
            free(text);
            return 1;
        }
        if (wcslen(text) > 0 && text[wcslen(text) - 1] == L'\n') {
            text[wcslen(text) - 1] = L'\0';
        }
        
        int key;
        wprintf(L"Введите ключ: ");
        while (wscanf(L"%d", &key) != 1 || key <= 0) {
            wprintf(L"Ошибка: введите положительное число\n");
            while (getchar() != '\n');
            wprintf(L"Введите ключ: ");
        }
        while ((c = getwchar()) != L'\n' && c != WEOF);
        
        wprintf(L"Расшифрованный текст: ");
        decrypt(text, key);
    }
    free(text);
    return 0;
}

// Шифрование
void encrypt(wchar_t *text, int key) {
    int flag = 0;
    for (int i = 0; text[i] != L'\0'; i++) {
        //Замена 'Ё' на 'Е'
        if (text[i] == L'Ё' || text[i] == L'ё') {
            if (text[i] == L'Ё') {
                text[i] = L'Е';
            } else {
                text[i] = L'е';
            }
            flag = 1;
        }
        
        // Английский
        if ((text[i] >= L'A' && text[i] <= L'Z') || (text[i] >= L'a' && text[i] <= L'z')) {
            int keyTemp = (key % 26 + 26) % 26;
   		    wchar_t offset = (text[i] >= L'a') ? L'a' : L'A';
            wprintf(L"%lc", ((text[i] - offset + keyTemp) % 26) + offset);
        }
        
        // Русский
        // Заглавные
        else if (text[i] >= L'А' && text[i] <= L'Я') {
            wchar_t offset = L'А';
            wchar_t formula = ((text[i] - offset + key + 33) % 33) + offset;

			if (formula == L'а') { //'а' идет после 'Я' в Unicode
            	formula = L'А';
            	formula --;
            }
   
   		  if (flag == 1) { // Если была замена 'Ё'
            	formula++;
            	flag = 0;
            }
            
            // Если сдвиг проходит дальше буквы 'Я'
            int j = 0;
            if (text[i] > L'Е' && text[i] + key > L'Я') {
            	formula ++;
            	j = 1;
            }
            
            // Если сдвиг проходит через 'Ё'
            if (formula == L'Ж') {
            	formula = L'Ё';
            }
            else if ((text[i] < L'Ж' || j == 1) && formula >= L'Ж') {
            	formula --;
            }
			if (formula == L'Џ') { // перед 'А' идет 'Џ'
				formula = L'Я';
			}

            wprintf(L"%lc", formula);
        }
        
        // Строчные
		else if (text[i] >= L'а' && text[i] <= L'я') {
            wchar_t offset = L'а';
            wchar_t formula = ((text[i] - offset + key + 33) % 33) + offset;
 
			if (formula == L'ѐ') { //'ѐ' идет после 'я' в Unicode
            	formula = L'а';
            	formula --;
            }
         
            if (flag == 1) { // Если была замена ё
            	formula++;
            	flag = 0;
            }

            // Если сдвиг проходит дальше буквы 'я'
            int j = 0;
            if (text[i] > L'е' && text[i] + key > L'я') {
            	formula ++;
            	j = 1;
            }
            
            // Если сдвиг проходит через 'ё
            if (formula == L'ж') {
            	formula = L'ё';
            }
            else if ((text[i] < L'ж' || j == 1)&& formula >= L'ж') {
            	formula --;
            }
            if (formula == L'Я') { // т.к перед 'а' стоит 'Я' в ASII
            		formula = L'я';
            	}
            	
            wprintf(L"%lc", formula);
        }
            else {
            wprintf(L"%lc", text[i]);
        }
    }
    wprintf(L"\n");
}


// Расшифрование
void decrypt(wchar_t *text, int key) {
    int flag = 0;
    for (int i = 0; text[i] != L'\0'; i++) {
        //Замена 'Ё' на 'Ж'
        if (text[i] == L'Ё' || text[i] == L'ё') {
            if (text[i] == L'Ё') {
                text[i] = L'Ж';
            } else {
                text[i] = L'ж';
            }
            flag = 1;
        }
        
        // Английский
		if ((text[i] >= L'A' && text[i] <= L'Z') || (text[i] >= L'a' && text[i] <= L'z')) {
            int keyTemp = (key % 26 + 26) % 26;
  		    wchar_t offset = (text[i] >= L'a') ? L'a' : L'A';
            wprintf(L"%lc", ((text[i] - offset - keyTemp + 26) % 26) + offset);
        }
        
        // Русский
        // Заглавные
        else if (text[i] >= L'А' && text[i] <= L'Я') {
            wchar_t offset = L'А';
            wchar_t formula = ((text[i] - offset - (key % 33) + 33) % 33) + offset;

			if (formula == L'а') { // 'а' идёт после 'Я' в Unicode
            	formula = L'А';
            	formula --;
            }
	
			if (flag == 1) { // Если была замена 'Ё'
            	formula --;
            	flag = 0;
            }
             // Если сдвиг проходит дальше 'А' (если вычитать)
            int j = 0;
            if (text[i] <= L'Е' && text[i] - key < L'А') {
            	formula--;
            	j = 1;
            }
            // Если сдвиг проходит через 'Ё' (если вычитать)
            if (formula == L'Е') {
            	formula = L'Ё';
            }
            else if ((text[i] >= L'Ж' || j == 1) && formula <= L'Е') {
            	formula ++;
            }
            
            if (formula == L'Џ') { // 'Џ' находится перед 'А'
            	formula = L'Я';
            }
            
            wprintf(L"%lc", formula);
        }
        // Строчные
        else if (text[i] >= L'а' && text[i] <= L'я') {
            wchar_t offset = L'а';
            wchar_t formula = ((text[i] - offset - (key % 33) + 33) % 33) + offset;
        
        	if (formula == L'ѐ') { // 'ѐ' идет после 'я'
            	formula = L'а';
            	formula--;
            }
        	
            if (flag == 1) {
             	formula --;
             	flag = 0;
            }

            // Если сдвиг проходит дальше 'а' (если вычитать)
			int j = 0;
			if (text[i] < L'ж' && text[i] - key < L'а') {
            	formula--;
            	j = 1;
            }

            // Если сдвиг проходит через 'ё'
            if (formula == L'е') {
            	formula = L'ё';
            }
			else if ((text[i] >= L'ж' || j == 1) && formula <= L'е') {
            	formula++;
            }
            
            if (formula == L'Я') { // 'я' находится перед 'А'
            	formula = L'я';
            }
            wprintf(L"%lc", formula);
        } else {
            wprintf(L"%lc", text[i]);
        }
    }
    
    wprintf(L"\n");
}