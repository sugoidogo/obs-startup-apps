import obspython, platform, json, subprocess, os

os=platform.system()
if os == "Windows":
    prepend='start "" '
elif os == "Darwin":
    prepend='open '
elif os == "Linux":
    prepend='xdg-open '
else:
    prepend=''

def script_description():
    return "run command(s) on obs startup"

def script_defaults(settings):
    defaults=obspython.obs_data_create_from_json(json.dumps({'commands':[]}))
    obspython.obs_data_apply(defaults,settings)
    obspython.obs_data_apply(settings,defaults)

def script_load(settings):
    settings=json.loads(obspython.obs_data_get_json(settings))
    commands=settings['commands']
    for command in commands:
        if(os != "Windows" and os.access(command['value'], os.X_OK)):
            print(command['value'])
            subprocess.Popen([command['value']])
        else:
            print(prepend+command['value'])
            subprocess.Popen(prepend+'"'+command['value']+'"',shell=True)
        
def script_properties():
    properties=obspython.obs_properties_create()
    editableList=obspython.obs_properties_add_editable_list(properties,'commands','startup app list',obspython.OBS_EDITABLE_LIST_TYPE_FILES_AND_URLS,None,None)
    return properties
