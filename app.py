from flask import Flask, request
# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, LocationSendMessage, StickerSendMessage
# 載入 json 標準函式庫，處理回傳的資料格式
import requests, json, time, statistics # import statistics 函式庫
import os
app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = 'AU/QDri2KE1NXmPy3qxcO7hY9+GmviLxov3guTlLUT5XfpsrRlXA7we4I32aRebmsHxr/MMl6ywNJLHSD/qmBRvYmFt0esCWnAFiGkYaijl9D05w1eB3+lgscrfxpe8WLtKF3kdoYQCY5dObj0aTXwdB04t89/1O/w1cDnyilFU='
channel_secret = '9cf048df757b3f7caabf30a89c853c9a'
handler = WebhookHandler(os.getenv(CHANNEL_SECRET))
# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}    
    body = {
            'replyToken':rk,
            'messages':[{
                        'type': 'image',
                        'originalContentUrl': msg,
                        'previewImageUrl': msg
                        }]
            }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)
# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}
    body = {
            'replyToken':rk,
            'messages':[{
                        "type": "text",
                        "text": msg
                        }]
            }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)
# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}   
    body = {
            'to':uid,
            'messages':[{
                        "type": "text",
                        "text": msg
                        }]
            }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/push', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)

app = Flask(__name__)

@app.route("/bot", methods=['GET','POST'])

def home():
  line_bot_api = LineBotApi(os.getenv(CHANNEL_ACCESS_TOKEN))
  try:
    msg = request.args.get('msg')
    if msg == '1':
      # 如果 msg 等於 1，發送早安
      line_bot_api.push_message('U3f07def73305496dc2076532560edcbc', TextSendMessage(text='早安 吃藥時間到囉! ฅ●ω●ฅ'))
    elif msg == '2':
      # 如果 msg 等於 2，發送午安
      line_bot_api.push_message('U3f07def73305496dc2076532560edcbc', TextSendMessage(text='午安 吃藥時間到囉!(๑´ㅂ`๑) '))
    elif msg == '3':
      # 如果 msg 等於 3，發送晚安
      line_bot_api.push_message('U3f07def73305496dc2076532560edcbc', TextSendMessage(text='早安 吃藥時間到囉! ٩(｡・ω・｡)و'))
    else:
      msg = 'ok'   # 如果沒有 msg 或 msg 不是 1～4，將 msg 設定為 ok
    return msg
  except:
    print('error')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
