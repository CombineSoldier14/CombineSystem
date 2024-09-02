from termcolor import colored
import os
import readline
from commandhandler import commandHandler
import cowsay
import wget

cmds = []

txt = []

class commands():
   @commandHandler(name="/cd", arg="(directory)", desc=f"change your current directory!", helptext=txt, cmds=cmds)
   def cd(arg, params):
    try:
        directory = arg.replace("+","",1)
        os.chdir(directory)
    except:
        print("{0}: Directory \"{1}\" not found! Perhaps you misspelled it?".format(
            colored("Error", "red", attrs=["bold"]),
            colored(directory, "light_blue", attrs=["bold"])
        ))

    
   @commandHandler(name="/help", arg="", desc=f"get help on commands! {colored('which you probably already figured out...', 'white', attrs=['dark'])}", helptext=txt, cmds=cmds)
   def helpcmd(arg, params):
    index = -1
    text = f"""{colored("CombineSystem", "green", attrs=["bold"])} has a certain way of specifiying commands, parameters, and arguments for organization:\nUsage: /command -parameter(s) argument(s)
Commands:
    """
    print(text)
    for t in txt:
        index += 1
        print(txt[index])

   
   @commandHandler(name="/cowsay", arg="(text)", desc=f"make a cow say your text!", helptext=txt, cmds=cmds)
   def cowsaycmd(arg, params):
    text = arg
    return cowsay.cow(text)
   
   
   @commandHandler(name="/echo", arg="(text)", desc=f"CombineSystem repeats your text!", helptext=txt, cmds=cmds)
   def echo(arg, params):
    print(arg)


   @commandHandler(name="/ls", arg="", desc=f"list the files and folders in the directory you are in!", helptext=txt, cmds=cmds)
   def ls(arg, params):
    for x in range(len(os.listdir())):
        if os.path.isfile("{0}/{1}".format(os.getcwd(), os.listdir()[x])):
            print(os.listdir()[x])
        else:
            print("{}/".format(colored(os.listdir()[x], "light_blue", attrs=["bold"])))


   @commandHandler(name="/osmode", arg="", desc=f"run a command in your base OS!", helptext=txt, cmds=cmds) 
   def osmode(arg, params):
    os.system(arg)


   @commandHandler(name="/read", arg="(filepath)", desc=f"prints the contents of a text file in the terminal!", helptext=txt, cmds=cmds) 
   def read(arg, params):
    file = arg
    try:
        arg
    except:
        print("{0}: The file \"{1}\" could not be found.".format(
            colored("Error", "red", attrs=["bold"]),
            colored(arg, "light_blue", attrs=["bold"])
        ))
        return
    with open(file) as e:
        try:
            print(e.read())
        except:
            print("{}: The file \"{}\" cannot be read. Are you sure this is a text file?".format(
                colored("Error", "red", attrs=["bold"]),
                colored(file, "light_blue", attrs=["bold"])
            ))


   @commandHandler(name="/wget", arg="(url)", desc=f"downloads a file from a specified URL!", helptext=txt, cmds=cmds) 
   def wgetcmd(arg, params):
    x = arg.replace("+","",1)
    try:
        wget.download(x)
        print("\n")
    except:
        print("{0}: The URL \"{1}\" is invalid. Are you sure this is a valid link to a file?\n".format(
            colored("Error", "red", attrs=["bold"]),
            colored(x, "light_blue", attrs=["bold"])
        ))
