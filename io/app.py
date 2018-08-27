import requests, uuid, pprint
from flask import Flask, request

from models import db, Chat

from keys import _TELEGRAM_TOKEN, _POSTGRES

app = Flask(__name__)

# App Config
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % _POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Databaset Initialisation
db.init_app(app)

def get_url(method):
  return 'https://api.telegram.org/bot{}/{}'.format(_TELEGRAM_TOKEN,method)

def process_message(update):
    chat_id = update['message']['chat']['id']

    data = {}
    data['chat_id'] = chat_id
    print(update['message']['text'])
    if (update['message']['text'].startswith('/token')):
        with app.app_context():
            chat = Chat.query.filter_by(chat_id=chat_id, revoked=False).first()
            if (chat == None):
                new_uuid = str(uuid.uuid1()).replace('-','')
                # TO-DO: ADD CHECK TO SEE IF UUID ALREADY EXISTS
                new_chat = Chat(chat_id=str(chat_id), token=new_uuid)
                db.session.add(new_chat)
                db.session.commit()

                data['text'] = 'Here is your token: {}'.format(new_uuid)
            else:
                data['text'] = 'Looks like you already have a token for this chat.\n' \
                               'Here it is: {}'.format(chat.token)
    elif (update['message']['text'].startswith('/revoke')):
        with app.app_context():
            chat = Chat.query.filter_by(chat_id=chat_id, revoked=False).first()
            if (chat == None):
                data['text'] = 'You have no active token.'
            else:
                chat.revoked = True
                db.session.commit()
                data['text'] = 'Token revoked. Please use /token to generate a new one.'
    else:
        data['text'] = 'Hi, please use the available commands:\n/token to generate a new token or\n/revoke to revoke a token.'
    r = requests.post(get_url('sendMessage'), data=data)

@app.route('/{}'.format(_TELEGRAM_TOKEN), methods=['POST'])
def process_update():
    if request.method == 'POST':
        update = request.get_json()
        # pprint.pprint(update)
        if 'message' in update:
            process_message(update)
        return 'ok', 200
    return 404

@app.route('/send-message', methods=['POST'])
def process_send_message():
    if request.method == 'POST':
        message = request.get_json()
        print(message)
        if ('token' in message):
            token = message['token']
            with app.app_context():
                chat = Chat.query.filter_by(token=token, revoked=False).first()
                if chat is not None:
                    data = {}
                    data['chat_id'] = chat.chat_id
                    data['text']    = message['text']
                    r = requests.post(get_url('sendMessage'), data=data)
                    return 'ok', 200
    return 404

@app.route('/')
def main():
    return 'Hello World'

if __name__ == '__main__':
    app.run()