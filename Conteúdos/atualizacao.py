# Importar a classe Avaliacao do arquivo avaliacao
from avaliacao import Avaliacao

class Restaurante:
  # Lista de todos os restaurantes
  restaurantes = []

  # Quando usamos o self, estamos acessando os atributos e métodos de um objeto em particular
  def __init__(self, nome, categoria):
    self._nome = nome.title() # Essa função serve para que a primeira letra do nome do restaurante sempre apareça como maiúscula
    self.categoria = categoria
    self._ativo = False # Esse underline é uma convenção para sabermos que esse atributo não deve ser modificado
    self._avaliacao = []

    # Assim que criarmos um restaurante, ele será adicionado à nossa lista que criamos lá em cima
    Restaurante.restaurantes.append(self)
    # O self está garantindo que será armazenado cada objeto individualmente

  # O método __str__ nos mostra o objeto em forma de texto, ao invés de nos mostrar onde ele está alocado na memória
  def __str__(self):
    return f'{self.nome} | {self.categoria}'
  
  # Podemos criar nossos próprios métodos, como o método a seguir:
  # For Loop para percorrer por toda a lista que criamos e estamos armazenando os dados do restaurante
  # Método de classe para que nós possamos acessar diretamente a classe ao invés da instância da classe
  @classmethod
  def listar_restaurantes(cls):
    print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}') 
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') # Não usamos o self por estarmos nos referindo a lista, e não ao objeto diretamente

  @property
  def ativo(self):
    return 'Ativo' if self._ativo else 'Inativo'
  
  # Método para alternar o estado do restaurante para ativo
  def alternar_estado(self):
    self._ativo = not self._ativo

  # Método para os restaurantes receberem a avaliação
  def receber_avaliacao(self, cliente, nota):
    if 0 < nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)

  @property
  def media_avaliacoes(self):
    if not self._avaliacao:
      return '-' # Validando se o restaurante não tiver nenhuma avaliação, retornará 0
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) # Somando todas as notas
    quantidade_de_notas = len(self._avaliacao) # Armazenando o total de notas que temos
    media = round(soma_das_notas / quantidade_de_notas, 1)
    return media

# Ao criar um construtor, obrigatóriamente temos que passar os parâmetros na hora de instanciar a classe, como no exemplo abaixo:
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# Chamando a lista com todos os dados dos restaurantes já criados
Restaurante.listar_restaurantes()