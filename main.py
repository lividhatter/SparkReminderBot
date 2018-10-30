#!/usr/bin/env python3

from flask import Flask, jsonify, request
from ciscosparkapi import CiscoSparkAPI
import datetime
import threading
import pickle
import time
import os
from dateutil.parser import *

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
        # print('Sleeping {}'.format(sleep_time))
        time.sleep(sleep_time)

def determine_datetime(message_text):
    # ToDo needs to convert the user input into an actual date and time. send and error response if its not legit
    am_pm_values =['am', 'Am', 'AM','pm','PM','Pm']
    hour_minute_day_values = ['D','d','day','days','Day','Days',
                            'M','m','min','mins','Min','Mins',
                            'H','h','hour','hours','Hour','Hours']
    print(message_text)
    
    for _ in am_pm_values:
        found_am_pm = False
        found_hour_min_day = False
        print('-'*5)
        print(_)
        message_split = _.split(' ')
        first_part_of_message = message_split[0]
        
        for item in hour_minute_day_values:
            if item in first_part_of_message:
                found_hour_min_day = True
                print(item, first_part_of_message)
                # TODO: need to add the hours mins and days to now
        
        # for item in am_pm_values:
        #     if item in first_part_of_message:
        #         found_am_pm = True
                
        # if found_am_pm == False:
               
        if found_hour_min_day == False:
            try:
                found = parse(_, fuzzy=True)
                print(found)
            except:
                print('No date or time found')

            


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
    
    
    

    
    print('Now: ', now)
    print('Output: ', output)
    if now > output:
        output = output + datetime.timedelta(days=1)
    output_string = output.strftime('%m/%d/%Y at %I:%M%p')
    output_time_string = output.strftime('%m/%d/%Y')
    output_date_string = output.strftime('%I:%M%p')
    # should have output_time_string and output_date_string as variables

    return output, output_time_string, output_date_string
def get_test_response_dict():
    # test_message_text = ['10/20/2018 date only reminder',
    #         '10:00am time only no space',
    #         '12:00 pm time only with space',
    #         '10/11/2018 10:00am date and time',
    #         '10h no time or date 10 hours',
    #         '15m no time or date just minutes',
    #         '3d no time or date just days']
    
    test_dict = {"id": "test_message_id",
                "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNmMzMmE1MjAtZWMxYi0xMWU3LWIyMDEtNGZkZjM2MzM0N2Ix",
                "roomType": "group",
                "text": "EggTimer 5m this is the test message",
                "personId": "fake_person_id",
                "personEmail": "fake.email@nowhere.nope",
                "html": "<p><spark-mention data-object-type=\"person\" data-object-id=\"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk\">EggTimer</spark-mention> 5m test te3</p>",
                "mentionedPeople": ["Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk"],
                "created": "2018-10-28T17:35:53.507Z"}

    print(test_dict.get('text'))
    return test_dict

def send_confirmation(roomId, reminder_time_string, reminder_date_string, person_id, person_nickname,mode):
    if mode == True:
        print('Not sending confirmation.')
    else:
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
    print('Incoming Data: ', '-'*10)
    print(incoming_data)
    print('-'*10)
    person_id = incoming_data.get("personId")
    person_dict= botapi.people.get(person_id)
    person_nickname = person_dict.nickName

    # print('checking who sent message')
    if person_id != bot_id:
        # print('personID was not botID')
        room_id = incoming_data.get("roomId")
        message_id = incoming_data.get("id")
        # print('message ID: ', message_id)
        if message_id == 'test_message_id':
            print('calling function')
            message_dict = get_test_response_dict()
            test_mode = True
            message_text = message_dict.get('text')
        else:
            message_dict = botapi.messages.get(message_id)
            test_mode = False
            message_text = message_dict.text
        
        
        
        print('Room ID: ',room_id)
        print('Message ID: ',message_id)
        print('Message Dict: ',message_dict)
        print('Message Text: ', message_text)
        
        bot_found = False
        # remindme_found = False
        message_split = message_text.split(" ")

        if message_split[0].find(bot_name) > -1:
            # print('bot name found')
            bot_found = True

        # commented out the remind me requirements
        # if message_split[1].find("remindme") > -1:
            # remindme_found = True

        if bot_found: # and remindme_found:
            #  ToDo should accept time and date
            reminder_datetime, reminder_time_string = determine_datetime(message_text)
            
            # TODO: This code needs to be looked at after the datetime is properly returned
            if len(message_split) > 2:
                message = ' '.join(message_split[2:])
            else:
                message = ''
            print('Attempting to send confirmation')
            send_confirmation(room_id, reminder_time_string, reminder_date_string, person_id, person_nickname,test_mode)
            save_reminder(reminder_time, room_id, message, person_id, person_nickname,test_mode)

    return '', 204

if __name__ == '__main__':
    sleep_time = 15
    database_watcher = threading.Thread(target=check_reminders, args=(sleep_time, ))
    database_watcher.start()
    # app.run(debug=True, use_reloader=True)

    app.run('0.0.0.0')

