# Telegram I/O Bot

Telegram I/O Bot, an easy way to send messages to you in Telegram with code.
Ideal when you have a really long code running and want to know when it is done.

[http://t.me/the_io_bot](http://t.me/the_io_bot)

Currently under development, the database may be re-generated and your tokens revoked at any time.

# Sending messages via code

1. Curl
```
curl --header "Content-Type: application/json" --request POST --data '{"token":"<YOUR-TOKEN>","text":"Testing"}' https://dayrell.me/send-message
```

2. Python
```
import requests, json

def send_telegram_message(token, message):
    url = 'https://dayrell.me/send-message'
    data = {'token': token, 'text': message}
    headers = {'Content-type': 'application/json'}
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers)
        return r
    except:
        return None
```

If you cant install requests and only want to use native Python Libraries

```
import json, urllib.request
def send_telegram_message(message, token):
    url = 'https://dayrell.me/send-message'
    data = {'token': token, 'text': message}

    try:
        req = urllib.request.Request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(data)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        r = urllib.request.urlopen(req, jsondataasbytes)
        return r
    except:
        return None        
```

# Things that need to be done
- [ ] Re-factor code
- [ ] Check if UUID exists before adding to the database
- [ ] Make good return messages
- [ ] Add option to revoke key
- [ ] Add a way to use input via code
- [ ] More extensive README

