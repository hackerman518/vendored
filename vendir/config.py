"""
Function to read the configuration file and return our values. We only read
keys from the DEFAULT and override sections.
"""

import ConfigParser
import os

config_file = os.path.abspath(__file__ + "/../../" + 'config.ini')
config = ConfigParser.ConfigParser()
config.read(config_file)


def ConfigSectionMap():
    """Return a dict from our config.ini file. All values in the override
    section will override the default section."""
    opts = {}
    # Read all keys in the DEFAULT section to build our initial listing
    keys = config.defaults()
    for key in keys:
        # Use the key from override if defined else use DEFAULT key
        opts[key] = config.get('override', key)
    return opts