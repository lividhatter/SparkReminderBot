from dateutil.parser import *




messages = ['10/20/2018 date only reminder',
            '10:00am time only no space',
            '12:00 pm time only with space',
            '10/11/2018 10:00am date and time',
            '10h no time or date 10 hours',
            '15m no time or date just minutes',
            '3d no time or date just days']








# {'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMDMyYmIwZjAtZGFkZS0xMWU4LWJlMTQtNmZkMDQyMjMwYmJh', 'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNmMzMmE1MjAtZWMxYi0xMWU3LWIyMDEtNGZkZjM2MzM0N2Ix', 'roomType': 'group', 'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMjE3NGY4Yy02NDcwLTRlN2YtOWEwNy0yZGRiZWRmZTBiNTY', 'personEmail': 'cameron.hughes@farmersinsurance.com', 'mentionedPeople': ['Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk'], 'created': '2018-10-28T18:19:30.559Z'}

test_dict = {"id": "test_message_id",
                "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNmMzMmE1MjAtZWMxYi0xMWU3LWIyMDEtNGZkZjM2MzM0N2Ix",
                "roomType": "group",
                "text": "EggTimer 5m this is the test message",
                "personId": "fake_person_id",
                "personEmail": "fake.email@nowhere.nope",
                "html": "<p><spark-mention data-object-type=\"person\" data-object-id=\"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk\">EggTimer</spark-mention> 5m test te3</p>",
                "mentionedPeople": ["Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iODRhNjVkMS1hYWQ5LTQyMjAtOTgxZi1mMGMzZjBhM2UyMDk"],
                "created": "2018-10-28T17:35:53.507Z"
                }

x = test_dict.get('text')
print(x)