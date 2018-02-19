
from ciscosparkapi import CiscoSparkAPI
import requests
import jsonify



file = open("key.txt","r")

key = file.read()


botapi = CiscoSparkAPI(access_token=key)



# webhook = botapi.webhooks.create(name="Messages Firehose", targetUrl="https://a2e10001.ngrok.io/sparkbot/messages",resource="messages",event="created")
webhook = botapi.webhooks.list()

for item in webhook:
    print(item)
