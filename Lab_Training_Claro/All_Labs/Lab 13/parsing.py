import textfsm

def parsing(template_name,command):
    #template = open('cisco_ios_show_version.template')
    template = open(template_name)
    re_table = textfsm.TextFSM(template)
    fsm_results = re_table.ParseText(command)

    return fsm_results