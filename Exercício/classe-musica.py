class Musica:
  nome = ''
  artista = ''
  duracao = ''

musica1 = Musica()
musica1.nome = 'Balada Louca'
musica1.artista = 'Munhoz & Mariano'
musica1.duracao = '3'

musica2 = Musica()
musica2.nome = 'Bêbado Famoso'
musica2.artista = 'Murilo Huff'
musica2.duracao = '3:18'

musica3 = Musica()
musica3.nome = 'Mensagem Pra Ela'
musica3.artista = 'César Menotti & Fabiano'
musica3.duracao = '2:43'

print(f'Música: {musica1.nome} - Dupla sertaneja: {musica1.artista}, Duração: {musica1.duracao} minutos')
