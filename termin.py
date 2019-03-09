import requests
import re
import json
import time
import logging
import datetime

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename="termin_logs.txt",level=logging.DEBUG)


def write_response_to_log(txt):
    with open('log.txt', 'w', encoding='utf-8') as f:
        f.write(txt)

def check_if_card_available(tracking_Number):
    """
    Get the status of the availabality for the card by performing a POST request
    :param: Tracking number 
    :return: True if card is ready to be picked up else false
    """
    url = "https://www17.muenchen.de/EATWebSearch/Auskunft"
    post_data = {
    'zapnummer': tracking_Number,
    'pbAbfragen' : 'Auskunft'}
    session = requests.Session()
#     print(session.cookies)
    response = session.post(url, data=post_data )
#     print(session.cookies)
#     print(session.cookies.get_dict())
    
    time.sleep(2)
    response = session.post(url, data=post_data , cookies=session.cookies)
    # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#     print(response.text)
#     print(response)

    txt = response.text
    if 'liegt noch nicht zur Abholung bereit' in txt:
       print('Not Yet Availble')
    else:
       print('Seems like its available')
	
def get_termins(termin_type='Niederlassungserlaubnis Blaue Karte EU'):
    """
    Get termins status for given type.
    Base page https://www.muenchen.de/rathaus/terminvereinbarung_fs.html,
    and the frame for termins is https://www22.muenchen.de/termin/index.php?loc=FS
    :param termin_type: what type of appointment do you want to find?
    :return: dictionary of appointments, keys are possible dates, values are lists of available times
    """

    #TERMIN_URL = 'https://www22.muenchen.de/termin/index.php?loc=FS&ct=1071898'
    TERMIN_URL = 'https://www46.muenchen.de/rathaus/terminvereinbarung_abh.html?cts=1080805'

    REQ_URL = 'https://www.muenchen.de/rathaus/terminvereinbarung_abh.html?cts=1080805'
    url = "https://www46.muenchen.de/termin/index.php?cts=1080805"
    # 'CASETYPES[Niederlassungserlaubnis Blaue Karte EU]':0,
    
    # Which type of termin - change foreign driver license
    # Other available types:
    # 'CASETYPES[FS Fahrerlaubnis erstmalig]':0,
    # 'CASETYPES[FS Erweiterung Fahrerlaubnis]':0,
    # 'CASETYPES[FS Erweiterung C und D]':0,
    # 'CASETYPES[FS Verlängerung des Prüfauftrags]':0,
    # 'CASETYPES[FS Führerschein mit 17]':0,
    # 'CASETYPES[FS Umtausch in Kartenführerschein]':0,
    # 'CASETYPES[FS Abnutzung, Namensänderung]':0,
    # 'CASETYPES[FS Ersatzführerschein]':0,
    # 'CASETYPES[FS Karteikartenabschnitt]':0,
    # 'CASETYPES[FS Internationaler FS beantragen]':0,
    # 'CASETYPES[FS Umschreibung EU EWR FS beantragen]':0,
    # 'CASETYPES[FS Verlängerung der Fahrberechtigung bei befristetem Aufenthalt]':0,
    # 'CASETYPES[FS Verlängerung C- D-Klasse]':0,
    # 'CASETYPES[FS Eintragung BKFQ ohne Verlängerung]':0,
    # 'CASETYPES[FS Fahrerlaubnis nach Entzug]':0,
    # 'CASETYPES[FS Zuerkennung der ausländischen Fahrerlaubnis]':0,
    # 'CASETYPES[FS PBS für Taxi etc beantragen]':0,
    # 'CASETYPES[FS PBS verlängern]':0,
    # 'CASETYPES[FS Ersatz PBS]':0,
    # 'CASETYPES[FS Dienstführerschein umschreiben]':0,
    # 'CASETYPES[FS Internationaler FS bei Besitz]':0,
    # 'CASETYPES[FS Abholung Führerschein]':0,
    # 'CASETYPES[FS Auskünfte lfd Antrag allgemein]':0,
    # 'CASETYPES[FS Auskünfte lfd Antrag Begutachtung]':0,
    # 'CASETYPES[FS Auskünfte lfd Antrag Betäubungsmittel]':0,
    # 'CASETYPES[FS Auskunft zur Entziehung des Führerscheins]':0,
    # 'CASETYPES[FS Anmeldung und Vereinbarung Prüftermin]':0,
    # 'CASETYPES[FS Allgemeine Information zur Ortskundeprüfung]':0,
    # 'CASETYPES[FS Besprechung des Prüfungsergebnisses]':0,
    # 'CASETYPES[FS Beratung Fahreignung]':0,

    termin_data = {
        'step': 'WEB_APPOINT_SEARCH_BY_CASETYPES',
        'CASETYPES[%s]' % termin_type: 1,
    }
    
    session = requests.Session()
#     print(session.cookies)
    response = session.post(url, data=termin_data )
    # session.get(url)
#     print(session.cookies)
#     print(session.cookies.get_dict())
    
    time.sleep(2)
    response = session.post(url, data=termin_data , cookies=session.cookies)
    # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#     print(response.text)

#     print(response)
    txt = response.text
#     print (txt)
    try:
        json_str = re.search('jsonAppoints = \'(.*?)\'', txt).group(1)
    except AttributeError:
        print('ERROR: cannot find termins data in server\'s response. See log.txt for raw text')
        write_response_to_log(txt)
        return None

    appointments = json.loads(json_str)

    if len(appointments) != 1:
        print('ERROR: termins json is malformed. See log.txt for json data')
        write_response_to_log(str(appointments))
        return None

    try:
        for key in appointments:
            appointments = appointments[key]['appoints']
    except TypeError:
        print('ERROR: termins json is malformed. See log.txt for json data')
        write_response_to_log(str(appointments))
        return None

    return appointments


if __name__ == '__main__':
    url = "https://www46.muenchen.de/termin/index.php?cts=1080805"
    ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/{ADD_YOUR_KEY_HERE}'
#    ret = check_if_card_available()
#    exit()
    while True:
        appointments = get_termins()
        if appointments:
            json_data_dump = json.dumps(appointments, sort_keys=True, indent=4, separators=(',', ': '))
            json_object = json.loads(json_data_dump)
    #         print(json_object[0])
    #         for date_data in json_object.items():
    #             print("Date Data: {}".format(date_data))
            sorted_json = sorted(json_object.items())
    #         print(sorted_json)
            for  date_data, time_data_array in sorted_json:
                print("Date Data: {} Value: {}".format(date_data, time_data_array))
                if ('2019-10' in date_data or '2018-11' in date_data or '2018-12' in date_data):
#                     print("This is the month of Oct-Nov-Dec: {} {} ".format(date_data, time_data_array))
                    if time_data_array:
                        now = time.strftime("%c")
                        payload = { "value1" : date_data, "value2" : time_data_array, "value3" : str(url) }
                        logging.info("Appiontments availble:{}".format(time_data_array))
                        print("Appiontments availble:{}".format(time_data_array))
                        requests.post(ifttt_webhook_url, data = payload)
        
        now = datetime.datetime.now()
        today0800am = now.replace(hour=8, minute=0, second=0, microsecond=0)
        today0805am = now.replace(hour=8, minute=5, second=0, microsecond=0)

        today2230pm = now.replace(hour=22, minute=30, second=0, microsecond=0)
        today2235pm = now.replace(hour=22, minute=35, second=0, microsecond=0)
        if now > today0800am and now < today0805am:
            logging.info ("This is in bw 08:00 am and 08:05 am")
            print ("This is in bw 08:00 am and 08:05 am")
            payload = { "value1" : now, "value2" : "Testing Alive once a day", "value3" : str(url) }
            requests.post(ifttt_webhook_url, data = payload)
        logging.info("Sleeping for 5 mins...")
        print("Sleeping for 5 mins...")
        time.sleep(60*5)
        logging.info("Wake up and check if availble")
        print("Sleeping for 5 mins...")
        
    #                     for time_data in time_data_array:
    #                         print("Time Data: {}".format(time_data  ))
    #         parsed_appoints = json_data_dump.split(',')
    #         for appointment in parsed_appoints:
    #             print("Availble: {}".format(appointment))
        
        
        
        
        
        
