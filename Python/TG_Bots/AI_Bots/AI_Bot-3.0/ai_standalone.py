from g4f.client import Client

def send_request_gpt(system_prompt: str = None, content: str = ""):
    client = Client()
    messages = [{'role': 'user', 'content': content}]
    if system_prompt:
        messages.insert(0, {'role': 'system', 'content': system_prompt})
    response = client.chat.completions.create(
        model='gpt-4',
        messages=messages,
        web_search=False
    )
    return response.choices[0].message.content

prompts = {
    '1': "Ты - официант ресторана русской кухни.",
    '2': "Ты - повар ресторана русской кухни. Ты не принимаешь заказы, это делает официант",
    '3': "Ты - менеджер ресторана русской кухни. Предлагай скидки гостю на блюда или посещения."
}

if __name__ == '__main__':
    print("Выберите роль:")
    print("1. Официант")
    print("2. Повар") 
    print("3. Менеджер")
    print("4. Обычный GPT")
    
    choice = input("Введите номер роли (1-4): ")
    user_query = input('Введите запрос: ') + ' (подробно не писать)'
    
    if choice in prompts:
        answer = send_request_gpt(prompts[choice], user_query)
    elif choice == '4':
        answer = send_request_gpt(content=user_query)
    else:
        answer = "❌ Неверный выбор роли"
    
    print(answer)