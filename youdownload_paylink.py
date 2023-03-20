import requests
from paylink import short

mxid = []
var = True

conf = {
    "token_id": "",
    "chat_id": ""
}


def send_to_telegram(to, message):
    if to == False:
        to = conf['chat_id']
    else:
        pass
    message = str(message)
    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json"
    }

    payload = {'chat_id': to,
               'parse_mode': 'HTML', 'text': message, 'parse_mode': "HTML", "disable_web_page_preview": True}
    apiURL = f'https://api.telegram.org/bot{conf["token_id"]}/sendMessage'
    response = requests.post(apiURL, json=payload, headers=headers).json()

    return response


def inbox():
    url = f'https://api.telegram.org/bot{conf["token_id"]}/getUpdates'
    payload = {
        "offset": -1,
        "limit": 100,
        "timeout": 10
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(
        url, json=payload, headers=headers).json()["result"]

    try:

        for i in response:
            if str(i['message']['message_id']) in mxid:
                pass
            else:
                mxid.append(str(i['message']['message_id']))

                inbox = {'FROM': i['message']['from']['username'],
                         'ID_FROM': i['message']['from']['id'],
                         'TEXT': i['message']['text']
                         }

                return inbox

                # print("" + str(i['message']['message_id']))
                # response = []
                # mxid.append(str(i['message']['message_id']))
                # print(mxid)
    except:
        pass


def link_creator(url):

    if url.startswith('https://www.youtube.com/'):
        x = url.split('/')
        link = "https://www.youtubepi.com/" + x[3]
        link = short(link)['data'][-1]['short_url']

        link = '<a href="' + link + '">' + 'DOWNLOAD' + '</a>'
        return(link)
    else:
        if url.startswith('https://youtu.be'):
            x = url.split('/')
            link = "https://www.youtubepi.com/" + "watch?v=" + x[3]
            link = short(link)['data'][-1]['short_url']
            link = '<a href="' + link + '">' + 'DOWNLOAD' + '</a>'
            return(link)
        else:
            return False


if __name__ == '__main__':

    print("Bot inizializzato...")

    while True:
        ris = inbox()
        if ris == None:
            pass
        else:
            if var == True:
                var = False
            else:
                print(ris['TEXT'])
                mex = link_creator(ris['TEXT'])
                if mex == False:
                    send_to_telegram(int(
                        ris['ID_FROM']), "<b>Inserisci un link YouTube Valido!!</b>")
                    pass
                else:
                    send_to_telegram(int(ris['ID_FROM']), mex)
