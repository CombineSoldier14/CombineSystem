from termcolor import colored
from commandnames import cmds
from commandnames import cmdnames
import json
import os

with open("config.json") as e:
with open("/CombineSystemImg/CombineSystem/config.json") as e:
    config = json.load(e)

def interpreter():
    x = input("{0} v{1} {2}{3}{4} -> ".format(colored("CombineSystem", "green", attrs=["bold"]), 
                                          config["VERSION"], 
                                          colored("[", "magenta"),
                                          colored(os.getcwd(), "light_blue"),
                                          colored("]", "magenta")))
    if x.replace(' ', '').lower() not in cmdnames:
        print(f"{colored("Error", "red", attrs=["bold"])}: The command \"{colored(x, "light_blue", attrs=["bold"])}\" was not found. Maybe you misspelled it?")
    else:
        for y in cmds:
            if x.replace(' ', '').lower() == y["name"]:
                y["func"]()
    interpreter()
