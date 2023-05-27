import os
import openai

def ask(text): 
    user_input={"role" : "user", "content" : text}
    messages.append(user_input)

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    bot_text = response['choices'][0]['message']['content']
    bot_resp = {"role ": "assistant", "content": bot_text}
    messages.append(bot_resp)
    return bot_text

openai.api_key = "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"

system_instruction = """ 
너는 한동대학교 드롭탑 카페 AI 직원이야. 
아래는 카페 음료 종류야. 
아래 종류의 음료 말고는 다른 음료는 없어 

- 아메리카노 
- 라떼 
- 스무디 

위의 메뉴 말고는 없다고 생각하면돼 
""" 
messages = [{"role": "system", "content": system_instruction}]

while True:
    user_input = input("user input: ")
    bot_resp = ask(user_input)

    print("-"*30)
    print(f"user_input: {user_input}")
    print(f"bot_resp: {bot_resp}")