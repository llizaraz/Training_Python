from netmiko import ConnectHandler
import textfsm,os
import openpyxl
import pprint

# Netmiko is an external lib install using pip install netmiko

#############################Valores de conexion al equipo ###################


ipadd = 'ios-xe-mgmt-latest.cisco.com' # IP MGT
port = '8181'                         # PORT SSH (By Default 22)
username = 'developer'                #User de Red
password = 'C1sco12345'               #Password
global_delay = 3

###############################################################################
    #Aqui unifico los valores para enviarlos como argumento

equipo = {
    'device_type': 'cisco_ios',  #Tipo de equipo
    'host':   ipadd,            # IP MGT
    'username': username,
    'password': password,
    'port' : port,          # optional, defaults to 22
    'global_delay_factor': 3,
}
##############################################################################

# Connect using SSH
print ("Connecting : (" + ipadd + ")\n")

net_connect = ConnectHandler(**equipo) # envio a la funcion ConnectHandler el argumento **Equipo guardo la conexion en la variable net_connect

# Get Hostname from Session
hostname = net_connect.find_prompt()

print ("Hostname", hostname)

version = net_connect.send_command('show version')

print (version)

template = open('cisco_ios_show_version.template')
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(version)

print (fsm_results)

# OpenpyXL is an external lib install using pip install openpyxl

header = ['Os_Type','Version', 'Hostname', 'Uptime', 'll', 'Image', 'Serial', 'Platform', 'ConfReg']
values = fsm_results[0]

wbook =openpyxl.Workbook()
wsheet = wbook.active

wsheet.append(header)
wsheet.append(values)
wbook.save('saved_result.xlsx')

