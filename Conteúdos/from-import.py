from atualizacao import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Luka', 10)
restaurante_praca.receber_avaliacao('Isadora', 8)
restaurante_praca.receber_avaliacao('Maristela', 5)

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()