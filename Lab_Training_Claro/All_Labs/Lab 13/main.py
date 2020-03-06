import connect
from excel_save import savefile
from parsing import *

print(connect.equipo)
version=connect.connectar(connect.equipo,"show version")
parse=parsing('cisco_ios_show_version.template',version)
savefile(parse)
print(version)

