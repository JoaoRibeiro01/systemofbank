from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual

# conta_joao = ContaCorrente('joao', '155.140.157-69', '2231', '656565')
# cartao_joao = CartaoCredito("João", conta_joao)
# cartao_joao.senha = '2456'
# conta_joao.nome = "João Matheus"

#Agencia Virutal
agencia_virtual = AgenciaVirtual('www.agencialvirtual.com.br', 11231234, 123120000000)
agencia_virtual.depositar_paypal(50000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.caixa_paypal)
print("_"*100)
#Agencia Comum
agencia_comum = AgenciaComum(12312312, 1230123012)
agencia_comum.adicionar_clintes("Gliede", 21382194, 50000)
print(agencia_comum.clientes)

print("_" * 100)
#Agencia Premium
agencia_premium = AgenciaPremium(12312300123, 1293182385)
agencia_premium.adicionar_clintes("João Matheus", 21039192051, 1000000)
print(agencia_premium.clientes)
