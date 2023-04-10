from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage


class LineBot:
    def __init__(self, channel_access_token):
        self.line_bot_api = LineBotApi(channel_access_token)

    def send_message(self, user_id, message):
        try:
            self.line_bot_api.push_message(user_id, TextSendMessage(text=message))
        except LineBotApiError as e:
            print(e)
