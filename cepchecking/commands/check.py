from colorama import Fore

def isValid(cep):
    if len(cep) <= 6:
        print(f"{Fore.LIGHTGREEN_EX}Is Valid!!")
    else:
        print(f"{Fore.LIGHTRED_EX}Not is valid!!")
