from termcolor import colored

def help():
    text = f"""{colored("CombineSystem", "green", attrs=["bold"])} is not like other operating systems. Rather then typing the command along with arguments, you only type the command, and then CombineSystem will prompt you for arguments!\n
    
    Commands:
    {colored("cowsay", "light_blue", attrs=["bold"])} - get ASCII art of a cow saying your text!\n
    {colored("help", "light_blue", attrs=["bold"])} - get help on commands! {colored("which you probably already figured out...", "white", attrs=["dark"])}\n
    """
    print(text)