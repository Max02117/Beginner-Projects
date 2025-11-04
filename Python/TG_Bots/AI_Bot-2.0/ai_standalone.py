from g4f.client import Client

def send_request_gpt(content: str):
    client = Client()
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': content}],
        web_search=False
    )
    print(response.choices[0].message.content)
    
if __name__ == '__main__':
    send_request_gpt(input('Введите запрос: ') + 'подробно не писать')