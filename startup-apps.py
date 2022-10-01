import obspython, platform, json, subprocess, os

match platform.system():
    case "Windows":
        prepend='start "" '
    case "Darwin":
        prepend='open '
    case "Linux":
        prepend='xdg-open '
    case _:
        prepend=''

def script_description():
    return "run command(s) on obs startup"

def script_load(settings):
    settings=json.loads(obspython.obs_data_get_json(settings))
    commands=settings['commands']
    for command in commands:
        if(platform.system() is not "Windows" and os.access(command['value'], os.X_OK)):
            subprocess.Popen([command['value']])
        else:
            subprocess.Popen(prepend+'"'+command['value']+'"',shell=True)
        
def script_properties():
    properties=obspython.obs_properties_create()
    editableList=obspython.obs_properties_add_editable_list(properties,'commands','startup app list',obspython.OBS_EDITABLE_LIST_TYPE_FILES_AND_URLS,None,None)
    return properties
