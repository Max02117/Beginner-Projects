s = input('Введите строку: ').strip()
result = []

# Поиск слов, начинающихся и заканчивающихся на одну букву
for word in s.split():
    # Очистка от не-буквенных символов в начале и конце
    start = 0
    while start < len(word) and not word[start].isalpha():
        start += 1
    end = len(word) - 1
    while end >= 0 and not word[end].isalpha():
        end -= 1
    
    if start <= end:
        cleaned = word[start:end+1]
        if cleaned[0].lower() == cleaned[-1].lower():
            result.append(cleaned)
            
print("\nСлова, начинающиеся и заканчивающиеся на одну букву:")
print(', '.join(result) if result else "Таких слов нет")