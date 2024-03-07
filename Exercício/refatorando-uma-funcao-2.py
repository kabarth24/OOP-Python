class Pessoa:
  def __init__(self, nome='', idade=0, profissao=''):
    self.nome = nome
    self.idade = idade
    self.profissao = profissao

  def __str__(self):
    return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao}'
  
  def aniversario(self):
    self.idade += 1

  @property
  def saudacao(self):
    if self.profissao:
      return f'Olá, sou o {self.nome}! Trabalho como {self.profissao}.'
    else:
      return f'Olá, sou o {self.nome}'
  
pessoa1 = (Pessoa(nome='Luka', idade=23, profissao='Programador'))
print(pessoa1)

pessoa1.aniversario()
print(pessoa1)

print(pessoa1.saudacao)
