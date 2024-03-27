from datetime import datetime
import pytz
from random import randint

class ContaCorrente():
    """
    Funcionalidade:
        Cria um objeto, para gerenciar as contas dos clientes

    Atributos:
           nome (str) = Nome do cliente
           cpf (str) = Cpf do cliente - precisa colocar os pontos eos traços, padrão de um cpf
           saldo (int) = Saldo atual da conta do cliente
           agencia (int) = Qual a agencia do cliente
           num_conta (int)= Numero da conta do cliente
           transações (lista)= Lista de transações que foram feitas na conta do cliente.
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite =  None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f"O Saldo atual da sua conta é de: {self._saldo:,.2f}")

    def depositar_dinheiro(self, deposito):
        self._saldo += deposito
        self._transacoes.append((deposito, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, saque):
        if self._saldo - saque < self._limite_conta():
            print("Você não tem saldo suficiente")
            self.consultar_saldo()
        else:
            self._saldo -= saque
            self._transacoes.append((-saque, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_conta(self):
        print(f"Seu limite de cheque especial é de {self._limite_conta():,.2f}")

    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print("Transferência não concluída, saldo insufisiciente")
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    """
    Funcionalidade:
        Cria um objeto cartão de crédito associado a um objeto ContaCorrente

    Atributos:
        numero : Este atributo armazena o número único atribuído ao cartão de crédito. É crucial para identificar e vincular transações e atividades específicas a um cartão de crédito específico.

        titular: O nome do titular é o nome da pessoa cujo crédito está associado ao cartão. Este atributo é essencial para identificar a pessoa responsável pelo cartão e garantir que apenas o titular autorizado possa fazer transações.

        validade: A validade do cartão indica o período durante o qual o cartão pode ser usado para fazer transações. Geralmente, é composto por uma data de validade e é vital para garantir que o cartão seja utilizado dentro do prazo adequado.

        cod_seg: Este atributo armazena o código de segurança do cartão, também conhecido como CVV (Card Verification Value). O código de segurança é utilizado como uma camada adicional de segurança em transações online e por telefone, ajudando a verificar a posse física do cartão.

        _limite do cartao: O limite do cartão é o valor máximo que o titular pode gastar usando o cartão de crédito. Esse atributo é importante para controlar os gastos e evitar exceder os limites estabelecidos pela instituição financeira.

        senha: A senha é uma informação confidencial que serve como uma forma adicional de autenticação e segurança para o cartão de crédito. Geralmente é utilizada em transações presenciais e online para validar a identidade do titular do cartão.

        conta_corrente ao cartao: Este atributo indica a conta bancária ou a fonte de onde serão retirados os fundos para pagar as despesas do cartão de crédito. É essencial para garantir que as transações sejam adequadamente registradas e que os pagamentos sejam processados corretamente.

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self._numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self._validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self._cod_seg = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        self._limte = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova Senha Inválida")