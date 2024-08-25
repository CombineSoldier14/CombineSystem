import wget
from termcolor import colored
import readline

def wgetcmd():
    x = input("The URL to download with wget: ")
    try:
        wget.download(x)
        print("\n")
    except:
        print("{0}: The URL \"{1}\" is invalid. Are you sure this is a valid link to a file?\n".format(
            colored("Error", "red", attrs=["bold"]),
            colored(x, "light_blue", attrs=["bold"])
        ))