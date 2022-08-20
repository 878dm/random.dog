import requests
TOKEN='5549407151:AAGVaQx5L2bvwBYnZE3a50yycdBQfPvl1fo'

def send_button(chat_id):
    button1 = {
        'text':'random dog'
    }
    button2 = {
        'text':'random cat'
    }
    data = {
        'chat_id':chat_id,
        'text':"random",
        "reply_markup":{
            "resize_keyboard":True,
            'keyboard':[
                [button1],
                [button2]
            ]
        }
    }
    url=f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(url,json=data)

def send_Photo(chat_id):
    url=f"https://random.dog/woof.json"
    photo= requests.get(url).json()['url']
    payload={
        'chat_id':chat_id,
        'photo':photo
    }
    url=f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    requests.post(url,params=payload)

def send_photocat(chat_id):
    url =f"https://aws.random.cat/meow"
    photo = requests.get(url).json()['file']
    payload={
        'chat_id':chat_id,
        'photo':photo
    }
    url=f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    requests.post(url,params=payload)

def get_Updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    result = requests.get(url)
    data = result.json()['result'][-1]
    update_id = data['update_id']
    text = data["message"]['text']
    chat_id = data['message']['chat']['id']
    return update_id, chat_id, text

last_update_id = -1

while True :
    update_id, chat_id, text = get_Updates()
    if last_update_id !=update_id:
        if text == '/start':
            send_button(chat_id)

        if text == "random dog":
            send_Photo(chat_id)
        elif text == 'random cat':
            send_photocat(chat_id)
        last_update_id = update_id
