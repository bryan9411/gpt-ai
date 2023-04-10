import openai
import re


def generate_response(user_message, api_key, api_endpoint):
    # 初始化 OpenAI API
    openai.api_key = api_key
    prompt = f"Conversation with a chatbot:\nUser: {user_message}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )
    message = response.choices[0].text
    # 刪除消息中的換行符和多餘空格
    message = re.sub("[\n]+", " ", message)
    message = re.sub("[ ]+", " ", message)
    message = message.strip()
    return message
