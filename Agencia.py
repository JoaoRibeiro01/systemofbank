from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self._limite_caixa = None
        self.emprestimos = []


    def _valor_caixa_formatado(self):
        valor = f"{self.caixa:,.2f}"
        valor = str(valor)
        valor = valor.replace(",", '_')
        valor = valor.replace(".", ',')
        valor = valor.replace('_', '.')
        return valor

    def _regra_caixa(self):
        self._limite_caixa = 1000000
        return self._limite_caixa


    def verificar_caixa(self):
        if self.caixa < self._regra_caixa():
            print(f"Caixa Atual: R${self._valor_caixa_formatado()}, O Caixa está abaixo do nível recomendado!")
        else:
            print(f"Caixa Atual: R${self._valor_caixa_formatado()}, O Caixa pode prosseguir com novas operações.")

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Não é possível realizar o empréstimo, dinheiro não disponível em caixa!")

    def adicionar_clintes(self, nome, cpf, patrimonio):
        if patrimonio > 0:
            self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=f"{randint(1001,9999)}")
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=f"{randint(1001,9999)}")
        self.caixa = 10000000

    def adicionar_clintes(self, nome, cpf, patrimonio):
        if patrimonio >= 1000000:
            super().adicionar_clintes(nome, cpf, patrimonio)
        else:
            print('O Cliente não possui patrimônio necessáiro, para ser cadastrado!')