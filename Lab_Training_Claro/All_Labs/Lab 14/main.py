import package.connect
from package.net.excel_save import savefile
from package.net.parsing import *

print_device()
version=package.connect.connectar("show version")
parse=parsing('cisco_ios_show_version.template',version)
savefile(parse)
print(version)

