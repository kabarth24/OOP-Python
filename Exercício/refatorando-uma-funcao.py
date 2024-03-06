class Musica:
    musica = []

    def __init__(self, nome, artista, duracao):
      self.nome = nome
      self.artista = artista
      self.duracao = duracao

      Musica.musica.append(self)
    
    def listar_musicas():
       for musicas in Musica.musica:
          print(f'Nome da música: {musicas.nome} | Nome do artista/banda: {musicas.artista} | Duração da música (em segundos): {musicas.duracao}')

musica1 = Musica('Lonely Day', 'System Of A Down', 248)
musica2 = Musica('Hearts Breaking Even', 'Bon Jovi', 506)
musica3 = Musica('Simple Man', 'Lynyrd Skynyrd', 557)

Musica.listar_musicas()

"""""
Saída: Nome da música: Lonely Day | Nome do artista/banda: System Of A Down | Duração da música (em segundos): 248
Nome da música: Hearts Breaking Even | Nome do artista/banda: Bon Jovi | Duração da música (em segundos): 506
Nome da música: Simple Man | Nome do artista/banda: Lynyrd Skynyrd | Duração da música (em segundos): 557 
"""""