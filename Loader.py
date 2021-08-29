import importlib
import os

loaded_modules = {}

def load_module(module_name: str, package: str = "Classes"):
    """Loads a module from a given name.

    Args:
        module_name (str): The name of the module to load.
        package (str): The package to load the module from.

    Returns:
        module: The loaded module.
    """
    
    full_name = package + "." + module_name
    
    module = importlib.import_module(full_name)
    
    loaded_modules[full_name] = module
    return module, full_name

def reload_module(module_name: str, package: str = "Classes"):
    """Reloads a module from a given name.

    Args:
        module_name (str): The name of the module to reload.
        package (str): The package to reload the module from.

    Returns:
        None
    """
    
    full_name = package + "." + module_name
    
    if full_name in loaded_modules.keys():
        importlib.reload(loaded_modules[full_name])
    
