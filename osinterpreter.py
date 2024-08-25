from termcolor import colored
from commandnames import cmds
from commandnames import cmdnames
import json
import os
import readline

with open("CombineSystemImg/CombineSystem/config.json") as e:
    config = json.load(e)

def interpreter():
    x = ""
    r = input("{0} v{1} {2}{3}{4} -> ".format(colored("CombineSystem", "green", attrs=["bold"]), 
                                          config["VERSION"], 
                                          colored("[", "magenta"),
                                          colored(os.getcwd(), "light_blue"),
                                          colored("]", "magenta")))
    for comds in r:
        if comds == " ":
            break
        else:
            x = x + comds
    arg = r.replace(x, "")
    if " " in r:
        arg = arg.replace(" ", "")
    if x.replace(' ', '').lower() not in cmdnames:
        print("{0}: The command \"{1}\" was not found. Maybe you misspelled it?".format(
            colored("Error", "red", attrs=["bold"]),
            colored(x, "light_blue", attrs=["bold"])
        ))
    else:
        for y in cmds:
            if x.replace(' ', '').lower() == y["name"]:
                y["func"](arg=arg)
    interpreter()
