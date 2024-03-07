class ContaBancaria:
  def __init__(self, titular='', saldo=0):
    self._titular = titular
    self._saldo = saldo
    self._ativo = False

  @property
  def titular(self):
    return self._titular
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def ativo(self):
    return self._ativo

  def __str__(self):
    return f'Titular da conta: {self.titular} | Saldo da conta: {self.saldo}'
  
  @classmethod
  def ativar_conta(cls, conta):
    conta._ativo = True
  
conta3 = ContaBancaria(titular='Maristela', saldo=12000)
print(f'Antes de ativar a conta: {conta3.ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar a conta: {conta3.ativo}')

conta1 = ContaBancaria(titular='Luka', saldo=8000)
conta2 = ContaBancaria(titular='Isadora', saldo=10000)
conta4 = ContaBancaria(titular='Giovanna', saldo=5000)

print(conta1)
print(conta2)
print(f'Titular da conta 4: {conta4.titular}')

class ClienteBanco:
  def __init__(self, nome, idade, endereco, cpf, profissao):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco
    self.cpf = cpf
    self.profissao = profissao

  @classmethod
  def criar_conta(cls, titular, saldo_inicial):
    conta = ContaBancaria(titular, saldo_inicial)
    return conta

cliente1 = ClienteBanco(nome='Luka', idade=23, endereco='Rua Will das Varzeas', cpf='124.582.369-55', profissao='Programador')
cliente2 = ClienteBanco(nome='Isadora', idade= 22, endereco='Meu coração', cpf='148.795.632-69' , profissao='Autônoma')
cliente3 = ClienteBanco(nome='Maristela', idade= 54, endereco='Querencia do Norte', cpf='474.754.589-47' , profissao='Rainha da casa')
cliente4 = ClienteBanco(nome='Giovanna', idade=19 , endereco='NAR-SP', cpf='897.485.879-99' , profissao='Atleta')
cliente5 = ClienteBanco(nome='Estevão', idade=700 , endereco='Sim', cpf='1' , profissao='Rei')

conta_cliente1 = ClienteBanco.criar_conta('Luka Alfa', 100000000000)
print(f'Conta de {conta_cliente1.titular} criada com saldo inicial de {conta_cliente1.saldo}')
