from termcolor import colored
import os
import readline
from commandhandler import commandHandler
import cowsay
import wget

cmds = []

txt = []

class commands:
   
   def handler(name, arg, desc):
      return commandHandler(name=name, arg=arg, desc=desc, helptext=txt, cmds=cmds)

   @handler(name="/cd", arg="(directory)", desc=f"change your current directory!")
   def cd(arg, params):
    try:
        os.chdir(arg[0])
    except:
        print("{0}: Directory \"{1}\" not found! Perhaps you misspelled it?".format(
            colored("Error", "red", attrs=["bold"]),
            colored(arg[0], "light_blue", attrs=["bold"])
        ))

    
   @handler(name="/help", arg="", desc=f"get help on commands! {colored('which you probably already figured out...', 'white', attrs=['dark'])}")
   def helpcmd(arg, params):
    index = -1
    text = f"""{colored("CombineSystem", "green", attrs=["bold"])} has a certain way of specifiying commands, parameters, and arguments for organization:\nUsage: /command -parameter(s) argument(s)
Commands:
    """
    print(text)
    for t in txt:
        index += 1
        print(txt[index])

   
   @handler(name="/cowsay", arg="(text)", desc=f"make a cow say your text!")
   def cowsaycmd(arg, params):
    text = arg
    return cowsay.cow(text)
   
   
   @handler(name="/echo", arg="(text)", desc=f"CombineSystem repeats your text!")
   def echo(arg, params):
    print(arg)


   @handler(name="/ls", arg="", desc=f"list the files and folders in the directory you are in!")
   def ls(arg, params):
    for x in range(len(os.listdir())):
        if os.path.isfile("{0}/{1}".format(os.getcwd(), os.listdir()[x])):
            print(os.listdir()[x])
        else:
            print("{}/".format(colored(os.listdir()[x], "light_blue", attrs=["bold"])))


   @handler(name="/osmode", arg="", desc=f"run a command in your base OS!") 
   def osmode(arg, params):
    os.system(arg)


   @handler(name="/read", arg="(filepath)", desc=f"prints the contents of a text file in the terminal!") 
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


   @handler(name="/wget", arg="(url)", desc=f"downloads a file from a specified URL!") 
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

    
   @handler(name="/rm", arg="(optional: -rf: to remove directory) (file)", desc=f"Removes a specified file or directory")
   def rm(arg, params):
       if "-rf" not in params:
          if not os.path.isfile(arg[0]):
             print("{0}: File \"{1}\" not found or is a directory! Perhaps you misspelled it?\nTo delete a directory, use the \"-rf\" parameter.".format(
            colored("Error", "red", attrs=["bold"]),
            colored(arg[0], "light_blue", attrs=["bold"])))
          else:
             os.remove(arg[0])
       else:
          if not os.path.isdir(arg[0]):
             print("{0}: Directory \"{1}\" not found or is a file! Perhaps you misspelled it?\nTo delete a file, do not use the \"-rf\" parameter.".format(
            colored("Error", "red", attrs=["bold"]),
            colored(arg[0], "light_blue", attrs=["bold"])))
          else:
             try:
               os.rmdir(arg[0])
             except:
                print("{0}: Directory \"{1}\" is not empty".format(
                colored("Error", "red", attrs=["bold"]),
                colored(arg[0], "light_blue", attrs=["bold"])))