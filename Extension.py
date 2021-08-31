from nltk.util import pr
import Loader
import os

commands = {}
modules = {}

def load_command(file: str, name=None):
    if "__pycache__" in file:
        return
        
    file = file.replace("/", ".")
    if file.endswith(".py"):
        file = file[:-3]
    
    if name == None:
        name = file
    
    if os.path.isdir(os.path.join("./Commands", file)):
        for new_file in os.listdir(os.path.join("./Commands", file)):
            load_command(file + "/" + new_file, file + "_" + new_file[:-3])
        return
    
    module, full_name = Loader.load_module(file, "Commands")
    
    commands[name] = getattr(module, "VoiceCommand")
    modules[name] = module

def unload_command(name):
    
    name = name[:-3]
    if name in commands.keys():
        if name == name:
            del commands[name]
            commands[name] = None
            modules[name] = None
            return
    return print("No command with name: " + name)
            

def get_commands():
    return commands

def get_modules():
    return modules