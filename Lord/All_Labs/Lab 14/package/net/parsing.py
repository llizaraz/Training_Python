from ..connect import *
import textfsm

def print_device():
    print(equipo)

def parsing(template_name,command):
    template = open(template_name)
    re_table = textfsm.TextFSM(template)
    fsm_results = re_table.ParseText(command)

    return fsm_results