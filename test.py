
from ciscosparkapi import CiscoSparkAPI
import requests
import jsonify



file = open("key.txt","r")

key = file.read()


botapi = CiscoSparkAPI(access_token="YTVjNTRiNjgtMGViOS00YmQyLWJiNTgtZThmMDNiYWI2Yzk3MDE3MDFmZGUtMmNj")



# webhook = botapi.webhooks.create(name="Messages Firehose", targetUrl="https://a2e10001.ngrok.io/sparkbot/messages",resource="messages",event="created")
webhook = botapi.webhooks.list()

for item in webhook:
    print(item)
