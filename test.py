
from ciscosparkapi import CiscoSparkAPI
import requests
import jsonify
import pickle
#
#
# x = []
#
# pickle.dump(x, open("reminder_list.pickle", "wb))

#
#
file = open("key.txt","r")

key = file.read()


botapi = CiscoSparkAPI(access_token=key)




# webhook = botapi.webhooks.create(name="Messages Firehose", targetUrl="https://lividhatterspark.appspot.com/sparkbot/messages",resource="messages",event="created")
# webhook = botapi.webhooks.delete('Y2lzY29zcGFyazovL3VzL1dFQkhPT0svMjI0NDQ3OTItZjA1OS00N2YyLTgyZGUtMTE4OGU0NzdjOWE0')
webhook = botapi.webhooks.get('Y2lzY29zcGFyazovL3VzL1dFQkhPT0svNmE2ZDA3MjAtNDcwMy00YTZkLWJhYjAtN2UwZDBkNTE4Y2Jl')
# webhook = botapi.webhooks.list()
#
print(webhook)
for item in webhook:
    print(item)
