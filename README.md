# The Telegram I/O Bot

Telegram I/O Bot

Currently under development

# Sending messages via code

1. Curl
```
curl --header "Content-Type: application/json" --request POST --data '{"token":"<YOUR-TOKEN>","text":"Testing"}' https://dayrell.me/send-message
```

2. Python
```
import requests, json

def send_telegram_message(token, message):
    url = https://dayrell.me/send-message
    data = {"token": token, "text": message}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r
```


# Things that need to be done
- [ ] Re-factor code
- [ ] Check if UUID exists before adding to the database
- [ ] Make good return messages
- [ ] Add option to revoke key
- [ ] Add a way to use input via code
- [ ] More extensive README

