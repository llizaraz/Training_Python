import xlrd
import pprint

from netmiko import ConnectHandler

# bbip_file = os.path.join(current_project_path, 'BBIP_RID.xlsx')
bbip_file = 'read_excel.xlsx'
bbip_book = xlrd.open_workbook(bbip_file)
bbip_sheet = bbip_book.sheet_by_index(0)
bbip_num_of_rows = bbip_sheet.nrows
bbip_num_of_cols = bbip_sheet.ncols
print(bbip_num_of_cols, bbip_num_of_rows)
print(bbip_sheet)


for row_in_bbip_file in range(1, bbip_num_of_rows):
    credentials = {}
    commands = []

    row_value_bbip_sheet = bbip_sheet.row_values(row_in_bbip_file)
    device = row_value_bbip_sheet[0]
    host = row_value_bbip_sheet[1]
    port = str(int(row_value_bbip_sheet[2]))
    device_type = row_value_bbip_sheet[3]
    username = row_value_bbip_sheet[4]
    password = row_value_bbip_sheet[5]
    global_delay_factor = int(row_value_bbip_sheet[6])
    command_1 = row_value_bbip_sheet[7]
    command_2 = row_value_bbip_sheet[8]

    #print(row_value_bbip_sheet)
    print(device,host,port,device_type,username,password,global_delay_factor,command_1,command_2)
    commands.append(command_1)
    commands.append(command_2)
    #commands.append(command_3)
    print(commands)

    credentials['device_type'] = device_type
    credentials['host'] = host
    credentials['port'] = port
    credentials['username'] = username
    credentials['password'] = password
    credentials['global_delay_factor'] = global_delay_factor
    pprint.pprint(credentials)

    # Connect using SSH
    print("Connecting : (" + host + ")\n")
    net_connect = ConnectHandler(**credentials)  # envio a la funcion ConnectHandler el argumento **Equipo guardo la conexion en la variable net_connect
    # Get Hostname from Session
    hostname = net_connect.find_prompt()

    print("Hostname", hostname)

    cmd = net_connect.send_command('show version')
    print(cmd)



