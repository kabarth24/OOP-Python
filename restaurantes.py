# Uma classe é como se fosse um molde para criar objetos
class Restaurante:
  # Aqui dentro podemos definir seus atributos (propriedades) e métodos (comportamentos) que serão comuns a todos os objetos pertencentes a essa classe
  nome = ''
  categoria = ''
  ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)