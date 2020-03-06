#!/python33/python

import urllib.request as urllib2
import json
import codecs,pprint
url = "http://macvendors.co/api/"


mac_list = []


path_data = '/Users/llizaraz/Python27/Labs/MAC_VENDOR/MAC_LIST.txt'

input_file = open((path_data))
raw_text_data = input_file.read()
input_file.close()

"""{'result': {'company': 'Cisco Systems, Inc', 'mac_prefix': '00:00:0C', 'address': '170 WEST TASMAN DRIVE,SAN JOSE  CA  95134-1706,US', 'start_hex': '00000C000000', 'end_hex': '00000CFFFFFF', 'country': 'US', 'type': 'MA-L'}}
"""

mac_list = raw_text_data.splitlines()

for mac_address in mac_list:
    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen( request )
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))


    try:
        print (str(mac_address) + ":" +  str((obj['result']['company'])))
    except:
        print(str(mac_address) + ": Buscar Manual" )
