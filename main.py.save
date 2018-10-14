#!/usr/bin/env python3

from flask import Flask, jsonify, request
from ciscosparkapi import CiscoSparkAPI
import datetime
import threading
import pickle
import time
import os

file = open("./key.txt","r")
key = file.read()

botapi = CiscoSparkAPI(access_token=key)
bot_id = 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2I4NGE2NWQxLWFhZDktNDIyMC05ODFmLWYwYzNmMGEzZTIwOQ'

bot_name = 'EggTimer'

app = Flask(__name__)

recent_message  = [{'From' : 'Cameron', 'message': 'this is the message'}]

def load_reminder_db():
    if os.path.getsize("reminder_list.pickle") > 0:
        reminder_db = pickle.load(open("reminder_list.pickle", "rb"))
    else:
        reminder_db = []

    return reminder_db

def save_reminder_db(database_list):
    pickle.dump(database_list, open("reminder_list.pickle", "wb"))
    return

def save_reminder(datetime, roomId, message, person_id, person_nickname):
    if message == '':
        reminder_message = "Hey <@personId:" + person_id + '|' + person_nickname + '>, apparently you just wanted me to ping you... weirdo.'
    else:
        reminder_message = "Hey <@personId:" + person_id + '|' + person_nickname + '>, ' + message

    db = load_reminder_db()
    new_reminder = [datetime, roomId, reminder_message]
    # need insert reminder into list alphabetticallly
    db.append(new_reminder)
    save_reminder_db(db)
    # print(reminder_db)
    return

def error_notification():
    pass

def send_reminder(roomid, reminder_message):
    botapi.messages.create(roomId=roomid, markdown=reminder_message)

def check_reminders(sleep_time):
    while True:
        db = load_reminder_db()
        new_db = []
        for reminder in db:
            if reminder[0] <= datetime.datetime.now():
                send_reminder(reminder[1], reminder[2])
            else:
                new_db.append(reminder)

        save_reminder_db(new_db)
        print('Sleeping {}'.format(sleep_time))
        time.sleep(sleep_time)

def determine_datetime(reminder_time_raw):
    # ToDo needs to convert the user input into an actual date and time. send and error response if its not legit
    minutes_var = 0
    hours_var = 0
    days_var = 0
    now = datetime.datetime.now()
    output = 0

    # If time ends in am, pm, a or p  the following 2 ifs catch it'
    if reminder_time_raw[-2:] == 'am' or reminder_time_raw[-2:] == 'pm':
        print('am or pm')
        am_pm = reminder_time_raw[-2:]
        raw_time = reminder_time_raw[:-2]
        if len(raw_time) == 4:
            hours_var = int(raw_time[:2])
            minutes_var = int(raw_time[2:4])
        elif len(raw_time) == 3:
            hours_var = int(raw_time[:1])
            minutes_var = int(raw_time[1:3])
        elif len(raw_time) <= 2:
            hours_var = int(raw_time)

        if am_pm == 'pm':
            print(hours_var)
            if hours_var <= 11:
                hours_var += 12

        output = datetime.datetime.now().replace(hour=hours_var, minute=minutes_var)

    if reminder_time_raw[-1:] == 'a' or reminder_time_raw[-1:] == 'p':
        print('a or p')
        am_pm = reminder_time_raw[-1:]
        raw_time = reminder_time_raw[:-1]
        if len(raw_time) == 4:
            hours_var = int(raw_time[:2])
            minutes_var = int(raw_time[2:4])
        elif len(raw_time) == 3:
            hours_var = int(raw_time[:1])
            minutes_var = int(raw_time[1:3])
        elif len(raw_time) <= 2:
            hours_var = int(raw_time)

        if am_pm == 'p':
            if hours_var <= 11:
                hours_var += 12

        output = datetime.datetime.now().replace(hour=hours_var, minute=minutes_var)

    # if time ends in h, m (but is not am or pm) , or d. this will catch it
    if output == 0:
        modifier = reminder_time_raw[-1:]
        raw_time = reminder_time_raw[:-1]
        if modifier == 'm':
            minutes_var = int(raw_time)
            output = datetime.datetime.now() + datetime.timedelta(hours=hours_var, minutes=minutes_var, days=days_var)

        elif modifier =='d':
            days_var = int(raw_time)
            output = datetime.datetime.now() + datetime.timedelta(hours=hours_var, minutes=minutes_var, days=days_var)

        elif modifier == 'h':
            hours_var = int(raw_time)
            output = datetime.datetime.now() + datetime.timedelta(hours=hours_var, minutes=minutes_var, days=days_var)

    if now > output:
        output = output + datetime.timedelta(days=1)
    output_string = output.strftime('%m/%d/%Y at %I:%M%p')
    output_time_string = output.strftime('%m/%d/%Y')
    output_date_string = output.strftime('%I:%M%p')
    # should have output_time_string and output_date_string as variables

    return output, output_time_string, output_date_string

def send_confirmation(roomId, reminder_time_string, reminder_date_string, person_id, person_nickname):
    message = 'Okay, I\'ll remind you on {} at {} <@personId:{}|{}>!'.format(reminder_time_string, reminder_date_string, person_id, person_nickname)
    botapi.messages.create(roomId=roomId, markdown=message)

@app.route('/')
def Homepage():
    return "Hello Livid!"

@app.route('/sparkbot/messages')
def get_messages():
    return 'string'

@app.route('/sparkbot/messages', methods=['POST'])
def receive_message():
    incoming_webhook=request.get_json()
    incoming_data = incoming_webhook.get("data")
    
    print(incoming_data)
    person_id = incoming_data.get("personId")
    person_dict= botapi.people.get(person_id)
    person_nickname = person_dict.nickName

    print('checking who sent message')
    if person_id != bot_id:
        print('personID was not botID')

        room_id = incoming_data.get("roomId")
        message_id = incoming_data.get("id")
        message_dict = botapi.messages.get(message_id)
        message_text = message_dict.text
        bot_found = False
        remindme_found = False
        message_split = message_text.split(" ")

        if message_split[0].find(bot_name) > -1:
            print('bot name found')
            bot_found = True

        if message_split[1].find("remindme") > -1:
            remindme_found = True

        if bot_found and remindme_found:
            #  ToDo should accept time and date
            reminder_time, reminder_time_string, reminder_date_string = determine_datetime(message_split[2])
            if len(message_split) > 3:
                message = ' '.join(message_split[3:])
            else:
                message = ''
            print('Attempting to send confirmation')
            send_confirmation(room_id, reminder_time_string, reminder_date_string, person_id, person_nickname)
            save_reminder(reminder_time, room_id, message, person_id, person_nickname)

    return '', 204

if __name__ == '__main__':
    sleep_time = 15
    database_watcher = threading.Thread(target=check_reminders, args=(sleep_time, ))
    database_watcher.start()
    # app.run(debug=True, use_reloader=False)

    app.run('0.0.0.0')
