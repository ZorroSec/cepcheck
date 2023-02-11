import requests
from colorama import Fore

class CepCheck:
    def __init__(self, cep):
        self.cep = cep
        
    def check(self):
        if len(self.cep) <= 6:
            print(f"{Fore.LIGHTGREEN_EX}Is Valid!!")
        else:
            print(f"{Fore.LIGHTRED_EX}Not is valid!!")