from termcolor import colored
from commandnames import cmds
from commandnames import cmdnames
import json

file = open('config.json')
config = json.load(file)

def interpreter():
    x = input("{0} v{1} -> ".format(colored("CombineSystem", "green", attrs=["bold"]), config["VERSION"]))
    if x not in cmdnames:
        print("The command \"{}\" was not found. Maybe you misspelled it?".format(colored(x, "light_blue", attrs=["bold"])))
    else:
        for y in cmds:
            if x == y["name"]:
                y["func"]()
    interpreter()

