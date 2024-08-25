from termcolor import colored
import os
import readline

def cd(arg):
    try:
        directory = arg
        os.chdir(directory)
    except:
        print("{0}: Directory \"{1}\" not found! Perhaps you misspelled it?".format(
            colored("Error", "red", attrs=["bold"]),
            colored(directory, "light_blue", attrs=["bold"])
        ))