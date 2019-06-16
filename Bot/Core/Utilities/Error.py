from colorama import Fore, Style

def Error (*Messages):
    return f'{Fore.RED}{" ".join (Messages)}{Style.RESET_ALL}'
