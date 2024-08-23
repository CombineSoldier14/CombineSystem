from termcolor import colored
from commandnames import cmds
from commandnames import cmdnames
import json
import os

with open("/CombineSystemImg/CombineSystem/config.json") as e:
    config = json.load(e)

def interpreter():
    try:
        r = input(f"{colored("CombineSystem", "green", attrs=["bold"])} v{config["VERSION"]} {colored("[", "magenta")}{colored(os.getcwd(), "light_blue")}{colored("]", "magenta")} -> ")
    except EOFError:
        return
    if r.replace(' ', '').lower() not in cmdnames:
        print(f"{colored("Error", "red", attrs=["bold"])}: The command \"{colored(x, "light_blue", attrs=["bold"])}\" was not found. Maybe you misspelled it?")
    else:
        for y in cmds:
            if r.replace(' ', '').lower() == y["name"]:
                y["func"]()
    interpreter()
