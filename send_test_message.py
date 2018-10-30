import json
import urllib.request

# This code needs to send a test message to local host that mimics the one sent by webex teams

test_message_text = ['10/20/2018 date only reminder',
            '10:00am time only no space',
            '12:00 pm time only with space',
            '10/11/2018 10:00am date and time',
            '10h no time or date 10 hours',
            '15m no time or date just minutes',
            '3d no time or date just days']
# message to send to local host


entire_test_message = {'id': 'Y2lzY29zcGFyazovL3VzL1dFQkhPT0svOTQ1MGIwYzMtYjAzMi00OWRlLTk3NWMtYzAxMGEzMzQ5ZTEy',
                        'name': 'All Messages v2',
                        'targetUrl': 'http://lividhatter.ddns.net:5000/sparkbot/messages',
                        'resource': 'messages',
                        'event': 'created',
                        'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9jb25zdW1lcg',
                        'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk',
                        'appId': 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0MzMmM4MDc3NDBjNmU3ZGYxMWRhZjE2ZjIyOGRmNjI4YmJjYTQ5YmE1MmZlY2JiMmM3ZDUxNWNiNGEwY2M5MWFh',
                        'ownedBy': 'creator',
                        'status': 'active',
                        'created': '2018-10-12T17:47:58.233Z',
                        'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMjE3NGY4Yy02NDcwLTRlN2YtOWEwNy0yZGRiZWRmZTBiNTY',
                       'data': {
                            'id': 'test_message_id',
                            'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNmMzMmE1MjAtZWMxYi0xMWU3LWIyMDEtNGZkZjM2MzM0N2Ix',
                            'roomType': 'group',
                            'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMjE3NGY4Yy02NDcwLTRlN2YtOWEwNy0yZGRiZWRmZTBiNTY',
                            'personEmail': 'cameron.hughes@farmersinsurance.com',
                            'mentionedPeople': ['Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk'],
                            'created': '2018-10-28T17:35:53.507Z'}}



myurl = "http://127.0.0.1:5000/sparkbot/messages"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(entire_test_message)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))

response = urllib.request.urlopen(req, jsondataasbytes)
print(response)