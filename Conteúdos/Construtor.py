class Restaurante:
  # Lista de todos os restaurantes
  restaurantes = []

  # Quando usamos o self, estamos acessando os atributos e métodos de um objeto em particular
  def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False

    # Assim que criarmos um restaurante, ele será adicionado à nossa lista que criamos lá em cima
    Restaurante.restaurantes.append(self)
    # O self está garantindo que será armazenado cada objeto individualmente

  # O método __str__ nos mostra o objeto em forma de texto, ao invés de nos mostrar onde ele está alocado na memória
  def __str__(self):
    return f'{self.nome} | {self.categoria}'
  
  # Podemos criar nossos próprios métodos, como o método a seguir:
  # For Loop para percorrer por toda a lista que criamos e estamos armazenando os dados do restaurante
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}') # Não usamos o self por estarmos nos referindo a lista, e não ao objeto diretamente

# Ao criar um construtor, obrigatóriamente temos que passar os parâmetros na hora de instanciar a classe, como no exemplo abaixo:
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# Chamando a lista com todos os dados dos restaurantes já criados
Restaurante.listar_restaurantes()
