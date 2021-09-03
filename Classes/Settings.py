import os
import json

default_settings = {
    'voice id': 2,
    'voice': True,
    'voice rate': 150,
    'text input': True,
}

settings = default_settings.copy()
settings_path = os.path.dirname(__file__) + "\\..\\settings.json"

# Create file if it doesnt exist
if not os.path.exists(settings_path):
    with open(settings_path, "w+") as file:
        file.write("{}")

with open(settings_path, "r+") as f:
    settings = json.load(f)
    for key, value in default_settings.items():
        if key not in settings:
            settings[key] = value

def get_setting(name: str):
    try:
        return settings[name] or default_settings[name]
    except KeyError:
        return None

def get_settings():
    return settings

def reset_setting(name: str):
    if default_settings[name]:
        settings[name] = default_settings[name]
    else:
        return Exception()
 
def set_setting(name: str, value: any, default: bool = False):
    value_type = type(default_settings[name])
    value = value_type(value)
    
    if default:
        default_settings[name] = value
    else:
        settings[name] = value

def save_settings():
    with open(settings_path, "w+") as file:
        json.dump(settings, file, indent=4)
            