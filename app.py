#flask(座小型的)、django(做大型的)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
#YOUR_CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('PnPW5H5f5+cL1n5fBhXcpEFRB61/6rD9SBmcdfePwh9RjgCbMQGuPYaoFYIZJHysBTEsMkd20Tm1lN4SSBSjhSGF7r/MYc//YJvJoRVNs/W1zugM6BIBE2vwApvR3GbKAinEx4ZdMash/Rj4vOSP5QdB04t89/1O/w1cDnyilFU=')
#YOUR_CHANNEL_SECRET
handler = WebhookHandler('e557c4604d48b802a3d12fedde73a675')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂'
    if msg == 'hi':
        r = 'hi'
    elif msg == '你吃飯了沒':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()