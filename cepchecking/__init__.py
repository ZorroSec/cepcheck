import requests
from colorama import Fore

class CepInfo:
    def __init__(self, cep):
        self.cep = cep
    
    def todo(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()
        for k, v in r.items():
            print(k, v)
    
    def localidade(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()
        print(r['localidade'])
    
    def logradouro(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
        print(r['logradouro'])
    
    def bairro(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
        print(r['bairro'])
    
    def comlemento(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
        print(r['complemento'])
    
    def uf(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
        print(r['uf'])

class Cep:
    def __init__(self, cep):
        self.cep = cep
    
    def check(self):
        if len(self.cep) <= 6:
            print(f"{Fore.LIGHTGREEN_EX}Is Valid!!")
        else:
            print(f"{Fore.LIGHTRED_EX}Not is valid!!")
    
    def formatCep(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/").json()
        print(r['cep'])
