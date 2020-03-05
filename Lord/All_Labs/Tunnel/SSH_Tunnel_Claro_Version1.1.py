#usr/bin/python3.6
# Developed by:  GSP_Development_Group

# Report_Software:
# Usage:
# python
# External Libs Netmiko
# Developed by:   Lord Lizarazo/Sergio Salazar/Harvey Poveda/David Cobos (By GSP_Latam_Developer_Team)
print ('Developed by (gsp_develop@cisco.com):Lord Lizarazo/Sergio Salazar/Harvey Poveda/David Cobos (By GSP_Latam_Developer_Team)')

#******************** Librerias ******************


from sshtunnel import SSHTunnelForwarder
from netmiko import ConnectHandler
import getpass,time

from termcolor import colored






########################## START #####################

version = ' 1.0.1'
print('\n Welcome To Jump_Server_Mapping \n')
print(('Cisco Jump  Tools Database :') + (version) + str('....'))

print (colored("""
               ,                           *               
               ((                          *((              
        (/     ((     ,(             (     *((     (/       
        ((     ((     ((,           (((    *((     ((       
(((     ((     ((     ((,    (((    (((    *((     ((     ((
/((     ((     ((     ((,    (((    (((    *((     ((     ((
               ((                          ,((              
                                                            
                                                            
       (((((((   /((    ((((((    /((((((    (((((((((      
      (((        /((    ((((/    /((        (((     (((     
      (((        /((        (((  .((/       (((     (((     
        ((((((   /((   .(((((/     /(((((     (((((((       
             
""",'blue', 'on_white'))

jump = '200.14.205.9'

##################################User and Password############################

user_jump = input('Por favor Ingrese el User del Hendrix: ? ')
pass_jump = getpass.getpass('Por favor Ingrese el Password del Hendrix: ? :')
#
user_devices = input('Por favor Ingrese el User de los Equipos: ? ')
pass_devices = getpass.getpass('Por favor Ingrese el Password de los Equipos: ? :')

##############################Lista de IP Equipos ##############################

lista_devices = ['10.50.16.1','10.10.95.1','10.10.63.11','10.10.66.31','10.10.66.227', '10.10.66.8', '10.10.66.3', '']

for remote_ip in lista_devices:
    # remote_ip = 10.10.63.11'
    if '.' in remote_ip: # Si hay . es una ip
        try:
            print ('Intentando Conexion al Equipo: ',remote_ip)
            server = SSHTunnelForwarder(jump, # IP JUMP
                ssh_username=user_jump, #User Jum
                ssh_password=pass_jump, #pass Jump
                remote_bind_address=(remote_ip, 22)  # IP device final mas puerto de ese equipo
            )
            server.start()

            print(('     Jump Server-->: ', jump, ' To Connecting-->: (' , remote_ip ,))

            port = (server.local_bind_port)  # show assigned local port
            # work with `SECRET SERVICE` through `server.local_bind_port`.


###################################################################################
############Aqui unifico los valores para enviarlos como argumento#################

            equipo = {
                'device_type': 'autodetect',  #Tipo de equipo
                'host':   '127.0.0.1',            # IP Local_Host_Tunneling
                'username': user_devices,
                'password': pass_devices,
                'port' : port,          # optional, defaults to 22
                'global_delay_factor': 3,
            }

            # Connect using SSH
            #print ("        Connecting-->: (" , remote_ip ,')' )

            print ("#" * 30,' Open: ',  remote_ip ,"#" * 30,)
            net_connect = ConnectHandler(**equipo) # envio a la funcion ConnectHandler el argumento **Equipo guardo la conexion en la variable net_connect

            hostname = net_connect.find_prompt() # Get Hostname from Session
            print ("You are working on Hostname", hostname) # print hostname del equipo
            terminal = net_connect.send_command('terminal len 0') # Envio Terminal leno
            print (terminal)
            cmd = net_connect.send_command('show version') #Envio Comandos
            print (cmd)
            print("Try Close Connecting-->: (" + remote_ip , ' on Port:', port,'\n')
            print ("#" * 30,' Close: ',  remote_ip ,"#" * 30,'\n')
        except KeyboardInterrupt:
            print ('has canceled the connection to the Device:' , remote_ip,'\n')
            pass
    else:
        print ('Gracias por Utilizar')

server.stop()

print("""Please, Take a cup of coffee for me'
      .-~~-.
    ,|`-__-'|
    ||      |
    `|      |  Double Espresso
      `-__-'

Bye, Bye
""")
time.sleep(2)
