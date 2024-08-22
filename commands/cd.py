from termcolor import colored
import os

def cd():
    try:
        directory = input("Directory to change into: ")
        os.chdir(directory)
    except:
        print(f"{colored("Error", "red", attrs=["bold"])}: Directory \"{colored(directory, "light_blue", attrs=["bold"])}\" not found! Perhaps you misspelled it?")