from termcolor import colored

def read():
    try:
        file = input("What is the file in your current directory you would like to read?: ")
    except:
        print(f"{colored("Error", "red", attrs=["bold"])}: The file \"{colored(file, "light_blue", attrs=["bold"])}\" could not be found.")
        return
    with open("/CombineSystemImg/CombineSystem" + file) as e:
        try:
            print(e.read())
        except:
            print(f"{colored("Error", "red", attrs=["bold"])}: The file \"{colored(file, "light_blue", attrs=["bold"])}\" cannot be read. Are you sure this is a text file?")
