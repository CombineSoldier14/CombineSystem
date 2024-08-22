import wget
from termcolor import colored

def wgetcmd():
    x = input("The URL to download with wget: ")
    try:
        wget.download(x)
        print("\n")
    except:
        print(f"{colored("Error", "red", attrs=["bold"])}: The URL \"{colored(x, "light_blue", attrs=["bold"])}\" is invalid. Are you sure this is a valid link to a file?\n")