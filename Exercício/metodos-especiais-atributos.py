class Carro:
  def __init__(self, modelo, cor, ano):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano

golf = Carro(modelo='VW Golf GTI', cor='Vermelho', ano=2023)

class Restaurante:
  def __init__(self, nome='Não informado', categoria='Nenhuma', ativo=False, estrelas=0, ano_inauguracao=0):
    self.nome = nome
    self.categoria = categoria
    self.ativo = ativo
    self.estrelas = estrelas
    self.ano_inauguracao = ano_inauguracao

  def __str__(self):
    return f'Nome do restaurante: {self.nome} | Categoria: {self.categoria}'

gracco = Restaurante(nome='Gracco', categoria='Hamburgueria', estrelas=4.8, ano_inauguracao=2022)
print(gracco)

class Cliente:
  def __init__(self, nome, idade, sexo, clube=False):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.clube = clube

cliente1 = Cliente(nome='Luka', idade=23, sexo='Masculino', clube=True)
cliente2 = Cliente(nome='Isadora', idade=22, sexo='Feminino')
cliente3 = Cliente(nome='João', idade=25, sexo='Masculino', clube=True)
cliente4 = Cliente(nome='Giovanna', idade=19, sexo='Feminino')