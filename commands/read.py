from termcolor import colored
import readline

def read(arg):
    file = arg
    try:
        file
    except:
        print("{0}: The file \"{1}\" could not be found.".format(
            colored("Error", "red", attrs=["bold"]),
            colored(file, "light_blue", attrs=["bold"])
        ))
        return
    with open("/CombineSystemImg/CombineSystem" + file) as e:
        try:
            print(e.read())
        except:
            print("{}: The file \"{}\" cannot be read. Are you sure this is a text file?".format(
                colored("Error", "red", attrs=["bold"]),
                colored(file, "light_blue", attrs=["bold"])
            ))
