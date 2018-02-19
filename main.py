from flask import Flask, jsonify, request
from ciscosparkapi import CiscoSparkAPI
import time

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
    person_dict= botapi.people.get(person_id)
    print(person_dict)
    person_nickname = person_dict.nickName
    print(person_nickname)
    # TODO Need to dermine if person_id is an admin

    if person_id != bot_id:
        room_id = incoming_data.get("roomId")
        message_id = incoming_data.get("id")
        # print("Room ID: " + room_id)
        # print("Person ID: " + person_id)

        message_dict = botapi.messages.get(message_id)
        message_text = message_dict.text

        bot_found = False
        remindme_found = False
        reminder_message =""
        message_split = message_text.split(" ")


        if message_split[0].find(bot_name) > -1:
            bot_found = True

        if message_split[1].find("remindme") > -1:
            remindme_found = True

        if bot_found and remindme_found:

            if len(message_split) > 3:
                for split in message_split[3:]:
                    reminder_message+=(split + " ")
            else:
                reminder_message = " Apparently you just wanted me to ping you... weirdo."
            wait_time = message_split[2]
            # TODO need to parse wait time for garbage inputs
            print("Waiting: " + wait_time)
            botapi.messages.create(roomId=room_id, text="Okay, I'll remind you in " + wait_time + " seconds, " + person_nickname)
            time.sleep(int(wait_time))
            botapi.messages.create(roomId=room_id, text="Reminding you: " + reminder_message)

        # Todo Determine which command was issued


    return '', 204


if __name__ == '__main__':
    app.run(debug=True)