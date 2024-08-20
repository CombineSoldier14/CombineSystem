from commands.cowsay import cowsaycmd
from commands.help import help

cmdnames = ["cowsay", "help"]

cmds = [
    {
        "name":"cowsay",
        "func":cowsaycmd
    },
    {
        "name":"help",
        "func":help
    }
]