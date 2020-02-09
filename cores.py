# importe o módulo colorama
import colorama
from colorama import Fore, Style, init

init(convert=True)
print("Hello World!")
print(Fore.RED + "Hello world!")