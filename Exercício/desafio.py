class Livro:
  def __init__(self, titulo, autor, ano_publicado):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicado = ano_publicado
    self.disponivel = True

  def __str__(self):
    return f'Titulo do livro: {self.titulo} | Nome do autor: {self.autor} | Ano de publicação: {self.ano_publicado}'

  def emprestar(self):
    self.disponivel = False

  @staticmethod
  def verificar_disponibilidade(ano):
    livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicado == ano and livro.disponivel]
    return livros_disponiveis

livro1 = Livro('O Senhor dos Aneis', 'J.R.R. Tolkien', 2019)
livro2 = Livro('O Hobbit' ,'J.R.R. Tolkien', 2019)

livro3 = Livro('Fluent Python', 'Luciano Ramalho', 2022)
print(f'Antes de emprestar: disponibilidade: {livro3.disponivel}')
livro3.emprestar()
print(f'Depois de emprestar: disponibilidade: {livro3.disponivel}')

Livro.livros = [livro1, livro2, livro3]