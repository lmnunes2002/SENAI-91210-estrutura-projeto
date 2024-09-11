import os
from models.pessoas import Pessoa
from models.enums.sexo import Sexo

os.system("cls||clear")

aluno = Pessoa("Marta", 22, Sexo.FEMININO)
print(aluno)