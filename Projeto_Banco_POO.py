from abc import ABC, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self,numero, cliente, agencia):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque no valor de: R${valor}")
            return True
        else:
            return False
        
    def deposito(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        else:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito no valor de: R${valor}")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_diario = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_diario = limite_diario
    def sacar(self, valor):
        if valor > self._limite:
            print("Valor acima do limite. Saque inválido!")
        elif self._saldo == 0:
            print("Saldo insuficiente!")
        elif self._limite_diario == 0:
            print("Operação de saque realizada 3 vezes. Volte amanhã!")
        elif valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque no valor de: R${valor}")
            self._limite_diario -= 1
            return super().sacar(valor)
        return False
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        else:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito no valor de: R${valor}")
            return super().deposito(valor)
        return False
    def __str__(self):
        return f"Conta Corrente: {self._numero} - Saldo: R${self._saldo} - Agenda: {self._agencia} - Nome do Cliente: {self._cliente._nome}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )
    
class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = []
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class Pessoa_fisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)