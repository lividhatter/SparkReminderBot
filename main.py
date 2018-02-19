from flask import Flask, jsonify, request
from ciscosparkapi import CiscoSparkAPI

file = open("key.txt","r")
key = file.read()
botapi = CiscoSparkAPI(access_token=key)
bot_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YTkzZDUyZC02NmU3LTRmMjYtOTljNC1iM2U1OThkZjU2M2M'
bot_name = 'LividTest'

app = Flask(__name__)

recent_message  = [{'From' : 'Cameron', 'message': 'this is the message'}]

@app.route('/')
def Homepage():
    return "Hello Livid!"

@app.route('/sparkbot/messages')
def get_messages():
    return jsonify(recent_message)


@app.route('/sparkbot/messages', methods=['POST'])
def send_message():

    incoming_webhook=request.get_json()
    incoming_data = incoming_webhook.get("data")

    # print('\n')
    # print(incoming_data)
    # print('\n')

    person_id = incoming_data.get("personId")
    if person_id != bot_id:
        room_id = incoming_data.get("roomId")
        message_id = incoming_data.get("id")
        # print("Room ID: " + room_id)
        # print("Person ID: " + person_id)

        message_dict = botapi.messages.get(message_id)
        message_text = message_dict.text
        first_nine_characters = message_text[0:9]
        print(first_nine_characters)
        if first_nine_characters == bot_name:
            message_text = message_text[10:]
            botapi.messages.create(roomId=room_id, text=message_text)

    return '', 204


if __name__ == '__main__':
    app.run(debug=True)