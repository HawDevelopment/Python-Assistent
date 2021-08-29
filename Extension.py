import Loader

commands = {}

def load_command(name, *args):
    module, full_name = Loader.load_module(name, "Commands")
    
    cls = getattr(module, "VoiceCommand")
    commands[full_name] = cls(*args)

def unload_command(name):
    full_name = "Commands." + name
    
    if (full_name) in commands.keys():
        del commands[full_name]
        commands[full_name] = None