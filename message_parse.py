from dateutil.parser import *



am_pm_values =['am', 'Am', 'AM','pm','PM','Pm']
hour_minute_day_values = ['D','d','M','m','h','H','day','days','Day','Days','min','Min','mins','Mins','hour','Hour','hours','Hours']
messages = ['10/20/2018 date only reminder', '10:00am time only no space', '12:00 pm time only with space','10/11/2018 10:00am date and time','10h no time or date 10 hours','15m no time or date just minutes','3d no time or date just days']



for _ in messages:
    found_am_pm = False
    found_hour_min_day = False
    print('-'*5)
    print(_)
    message_split = _.split(' ')
    first_part_of_message = message_split[0]
    
    for item in am_pm_values:
        if item in first_part_of_message:
            found_am_pm = True
            
    if found_am_pm == False:
        for item in hour_minute_day_values:
            if item in first_part_of_message:
                found_hour_min_day = True
                print(item, first_part_of_message)

        
    if found_hour_min_day == False:
        try:
            Found = parse(_, fuzzy=True)
        except:
            print('No date or time found')

        print(Found)

