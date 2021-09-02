import os

default_settings = {
    'voice id': 2,
    'voice': True,
    'text input': True
}

settings = default_settings.copy()
settings_path = os.path.dirname(__file__) + "/../settings.txt"

with open(settings_path, "r") as f:
    for line in f.readlines():
        split = line.split("=")
        settings[split[0]] = split[1]

def get_setting(name: str):
    return settings[name] or default_settings[name]

def get_settings():
    return settings

def reset_setting(name: str):
    if default_settings[name]:
        settings[name] = default_settings[name]
    else:
        return Exception()
 
def set_setting(name: str, value: any, default: bool = False):
    
    if default:
        default_settings[name] = value
    else:
        settings[name] = value

def save_settings():
    with open(settings_path, "w") as file:
        file.flush()
        for key, value in settings.items():
            file.write(key + "=" + value)
            