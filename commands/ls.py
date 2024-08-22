from termcolor import colored
import os

def ls():
    for x in range(len(os.listdir())):
        if os.path.isfile("{0}/{1}".format(os.getcwd(), os.listdir()[x])):
            print(os.listdir()[x])
        else:
            print(f"{colored("{}/".format(os.listdir()[x]), "light_blue", attrs=["bold"])}")