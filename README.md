# cepcheck

```uma api feita em python com o intuito de substituir a requisicao de uma api de cep para o uso pessoal
```

## Exemplos

### Cep.check()
```python
from cepchecking import CepCheck
cep = "01001000"
cepcheck = CepCheck(cep)

cepcheck.check()
```
`is valid` ou `not is valid!`

### Cep.formatCep()
```python
from cepchecking import Cep
cep = "01001000"
Cep = Cep(cep)

Cep.formatCep
```
`resultado: 01001-000`

#### CepCheck.cep()