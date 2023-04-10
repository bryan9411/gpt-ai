from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from gpt import generate_response

app = Flask(__name__)

# 設置 Line Messaging API 的頻道存取令牌和 Webhook Handler
line_bot_api = LineBotApi(
    "T7Lm4kQzEy3jt2Uf/dB7AUwITDHHY1tChfYp65efd9DySUrLrOMBT8nQdJVUb3YOVJjpnTIIYur0XsUm1TmQYpzNeEqclG1wePv6XgAGZP8Tu0/sU7sKUWC34AB83hGlrmss0xo4aDKbTr9kMDyIMwdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("b912068c1233f34d65cfd7195e3f6be5")

# 設置 ChatGPT API 的 API Key 和 endpoint
openai_key = "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"
openai_endpoint = "https://api.openai.com/v1/"


@app.route("/callback", methods=["POST"])
def callback():
    # 驗證 Line 簽名是否正確
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 獲取用戶發送的消息
    user_message = event.message.text
    # 使用 ChatGPT API 生成機器人的回答
    bot_message = generate_response(user_message, openai_key, openai_endpoint)
    # 向用戶發送機器人的回答
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=bot_message))


if __name__ == "__main__":
    app.run()
