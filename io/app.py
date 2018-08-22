import requests
from flask import Flask, request

from models import db

from keys import _TELEGRAM_TOKEN, _POSTGRES

app = Flask(__name__)

# App Config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % _POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'

# Databaset Initialisation
db.init_app(app)

def get_url(method):
  return 'https://api.telegram.org/bot{}/{}'.format(_TELEGRAM_TOKEN,method)

def process_message(update):
    data = {}
    data['chat_id'] = update['message']['from']['id']
    data['text'] = 'I can hear you!'
    r = requests.post(get_url('sendMessage'), data=data)

@app.route('/{}'.format(_TELEGRAM_TOKEN), methods=['POST'])
def process_update():
    if request.method == 'POST':
        update = request.get_json()
        print(update)
        if 'message' in update:
            process_message(update)
        return 'ok!', 200

@app.route('/')
def main():
    return 'Hello World'

if __name__ == '__main__':
    app.run()