from desafio import Livro

emprestar_biblioteca = Livro('Fluent Python', 'Luciano Ramalho', 2022)
print(f'Antes de emprestar (biblioteca): {emprestar_biblioteca.disponivel}')
emprestar_biblioteca.emprestar()
print(f'Depois de emprestar (biblioteca): {emprestar_biblioteca.disponivel}')

ano_especifico = 2019
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")
