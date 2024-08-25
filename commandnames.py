from commands.cowsay import cowsaycmd
from commands.help import help
from commands.ls import ls
from commands.cd import cd
from commands.read import read
from commands.osmode import osmode
from commands.wget import wgetcmd
from commands.echo import echo

cmdnames = ["cowsay", "help", "ls", "cd", "read", "wget", "osmode", "echo"]

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
    },
    {
        "name":"echo",
        "func":echo
    }
]
