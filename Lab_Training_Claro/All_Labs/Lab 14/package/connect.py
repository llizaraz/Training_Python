from netmiko import ConnectHandler


ipadd = 'ios-xe-mgmt-latest.cisco.com' # IP MGT
port = '8181'                         # PORT SSH (By Default 22)
username = 'developer'                #User de Red
password = 'C1sco12345'               #Password
global_delay = 3

equipo = {
    'device_type': 'cisco_ios',  #Tipo de equipo
    'host':   ipadd,            # IP MGT
    'username': username,
    'password': password,
    'port' : port,          # optional, defaults to 22
    'global_delay_factor': 3,
}

def connectar(command):
    net_connect = ConnectHandler(**equipo) # envio a la funcion ConnectHandler el argumento **Equipo guardo la conexion en la variable net_connect
    # hostname = net_connect.find_prompt()
    # print ("Hostname", hostname)

    command_response = net_connect.send_command(command)
    return command_response