import requests

class CepCheck:
    def __init__(self, cep):
        self.cep = cep
        
    def check(self, cep):
        return