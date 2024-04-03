#Feito por Wil
from func import Cliente
from func import Conta
from func import conta_C
from func import conta_p

#Feito por Letícia
cli1 = func.Cliente ('Mariana','123-456-789-00')
cli2 = func.Cliente ('Gabriel','098-765-432-11')

conta_c1 = func.conta_C ('001',tipo_conta='Corrente')
conta_p1 = func.conta_p ('100',taxa_juros=0.05)

cli1.abrir_conta(conta_c1)
cli1.abrir_conta(conta_p1)

conta_c2 = func.conta_C ('002',tipo_conta='Corrente')
conta_p2 = func.conta_p ('200',taxa_juros=0.02)

cli2.abrir_conta(conta_c2)
cli2.abrir_conta(conta_p2)

conta_c1.depositar(20000)
conta_c1.sacar(1000)
conta_c1.registrar_transacao('Transferência Recebida',200)
conta_p1.depositar(1000)
conta_p1.calcular_juros()

conta_c2.depositar(10000)
conta_c2.sacar(2000)
conta_c2.registrar_transacao('Transferência Recebida',300)
conta_p2.depositar(3000)
conta_p2.calcular_juros()

#Feito por Wil
conta_c1.extrato()
conta_p1.extrato()
conta_c2.extrato()
conta_p2.extrato()
