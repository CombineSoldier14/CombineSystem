from termcolor import colored
from system.commands import cmds
import json
import os
import readline

with open("config.json") as e:
    config = json.load(e)

def interpreter():
 while True:
    r = input("{0} v{1} {2}{3}{4} -> ".format(colored("CombineSystem", "green", attrs=["bold"]), 
                                          config["VERSION"], 
                                          colored("[", "magenta"),
                                          colored(os.getcwd(), "light_blue"),
                                          colored("]", "magenta")))
    arr = r.split()
    if len(arr) != 0:
        ind = 0
        params = []
        if " -" in r:
            for param in arr:
                if arr[ind].startswith("-"):
                    params.append(arr[ind])
                ind += 1


        cmdind = 0
        arg = ""
        for comds in arr:
            if arr[cmdind].startswith("+") == False and arr[cmdind].startswith("-") == False and arr[cmdind].startswith("/") == False:
                arg = arg + " " + arr[cmdind]
            cmdind += 1

        z = []
        for b in cmds:
            z.append(b["name"])
        if arr[0].lower() not in z:
            print("{0}: The command \"{1}\" was not found. Maybe you misspelled it? Type /help for a list of commands.".format(
                colored("Error", "red", attrs=["bold"]),
                colored(arr[0], "light_blue", attrs=["bold"])
            ))
        else:
            for y in cmds:
                if arr[0].lower() == y["name"]:
                    y["func"](arg=arg.replace(" ", "", 1), params=params)
