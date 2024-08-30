def commandHandler(name, arg, desc, helptext, cmds):
    def callback(func):
        from termcolor import colored
        x = "{0} {1} - {2}".format(colored("{}".format(name), 'light_blue', attrs=['bold']),
                                      arg, 
                                      desc)
        y = {
            "name":name,
            "func":func
        }
        if x not in helptext:
             helptext.append(x)
        if y not in cmds:
          cmds.append({
              "name":name,
              "func":func
          })
    return callback