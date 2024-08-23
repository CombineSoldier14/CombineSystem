from CombineSystemImg.CombineSystem.commands.cowsay import cowsaycmd
from CombineSystemImg.CombineSystem.commands.help import help
from CombineSystemImg.CombineSystem.commands.ls import ls
from CombineSystemImg.CombineSystem.commands.cd import cd
from CombineSystemImg.CombineSystem.commands.read import read
from CombineSystemImg.CombineSystem.commands.osmode import osmode
from CombineSystemImg.CombineSystem.commands.wget import wgetcmd

cmdnames = ["cowsay", "help", "ls", "cd", "read", "wget", "osmode"]

cmds = [
    {
        "name":"cowsay",
        "func":cowsaycmd
    },
    {
        "name":"help",
        "func":help
    },
    {
        "name":"ls",
        "func":ls
    },
    {
        "name":"cd",
        "func":cd
    },
    {
        "name":"read",
        "func":read
    },
    {
        "name":"osmode",
        "func":osmode
    },
    {
        "name":"wget",
        "func":wgetcmd
    }
]
