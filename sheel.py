from os import *
from colorama import Fore as f
from pyfiglet import *
system("clear")
fff = figlet_format("Sheel")
print("Press CTRL+Z to stop ping or something")
print(f"{f.YELLOW}{fff}")
while True:
    s = input("Terminal: $ ")
    system(f"{s}")
