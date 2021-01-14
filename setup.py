#!/usr/bin/env python3
import json

'''
- Code to generate config and do other setup on first run
'''

# default settings file
settings = {
    "port" : "6666",
}

# writes settings to config
with open("./config.json", "w") as file:
    file.write(json.dumps(settings, indent=4))
