# The Telegram I/O Bot

Telegram I/O Bot

# Sending messages via code

1. Curl
```
curl --header "Content-Type: application/json" --request POST --data '{"token":"<YOUR-TOKEN>","text":"Testing"}' <URL>
```

2. Python
```
import requests, json
url = '<URL>'
data = {"token":"<YOUR-TOKEN>","text":"Testing"}
headers = {'Content-type': 'application/json'}
>>> r = requests.post(url, data=json.dumps(data), headers=headers)
```


# Things that need to be done
- [ ] Re-factor code
- [ ] Check if UUID exists before adding to the database
- [ ] Make good return messages
- [ ] Add option to revoke key
- [ ] Add a way to use input via code
- [ ] More extensive README

