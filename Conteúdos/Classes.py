# Uma classe é como se fosse um molde para criar objetos
class Restaurante:
  # Aqui dentro podemos definir seus atributos (propriedades) e métodos (comportamentos) que serão comuns a todos os objetos pertencentes a essa classe
  nome = ''
  categoria = ''
  ativo = False

# Chamando a classe Restaurante
restaurante_praca = Restaurante()

# Atribuindo valores aos atributos da classe Restaurante
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

# Acessando o valor do atributo nome da instância restaurante_praca
nome_do_restaurante = restaurante_praca.nome

# Verificando se o restaurante está ativo ou inativo
if restaurante_praca.ativo:
  print('O restaurante está ativo.')
else:
  print('O restaurante está inativo.')

# Acessando o valor do atributo categoria e armazenando em uma variável
categoria_restaurante = Restaurante.categoria

# Nova instância
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

# Verificando se a categoria da instância restaurante_pizza é 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
  print('A categoria é Fast Food.')
else:
  print('A categoria não é Fast Food.')

# Imprimindo o nome e a categoria da instância restaurante_praca
print(f'Nome do restaurante: {restaurante_praca.nome}')
print(f'Categoria da instância restaurante_praca: {restaurante_praca.categoria}')