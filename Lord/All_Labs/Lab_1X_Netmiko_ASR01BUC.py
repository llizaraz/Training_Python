from netmiko import ConnectHandler
import getpass
import textfsm,os
import openpyxl
import pprint

# Netmiko is an external lib install using pip install netmiko

#############################Valores de conexion al equipo ###################


ipadd = '127.0.0.1' # IP MGT
port = '9999'                         # PORT SSH (By Default 22)
username = ''                #User de Red
password = getpass.getpass('Password:')               #Password
global_delay = 3

###############################################################################
    #Aqui unifico los valores para enviarlos como argumento

equipo = {
    'device_type': 'autodetect',  #Tipo de equipo
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

cmd = net_connect.send_command('show version brief')
print (cmd)
