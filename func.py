class Cliente: #Feito por Maiza
    def __init__(self,  nome, cpf,contas):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

class Conta: #Feito por Mariana
    def __init__(self, num_conta,saldo,transacao):
        self.num_conta = num_conta
        self.saldo = saldo
        self.transacao = []

    def depositar (self,dinheiro):
        self.saldo = self.saldo + dinheiro
        self.transacao.append(("Deposito: ",dinheiro))
    
    def sacar (self,dinheiro):
        if self.saldo > dinheiro:
            self.saldo = self.saldo - dinheiro
            self.transacao.append (("Saque: ", dinheiro))
        else:
            print ("Seu saldo é insuficiente")

    def registrar_transacao (self, tipo, valor):
        self.transacao.append((tipo ,":", valor))

    def extrato (self):
        print("Extrato da conta: ", self.num_conta)
        print ("Transação: ")
        for tipo,valor in self.transacao:
            print(tipo, ":" ,valor )
        print ("Saldo atual : ",self.saldo)

class conta_C(Conta): #Feito por Júlia
    def __init__(self, num_conta, saldo, taxa_juros,tipo_conta = "Corrente"):
        super().__init__(num_conta, saldo)
        self.tipo_conta = tipo_conta

class conta_p(Conta): #Feito por Júlia
    def __init__(self, num_conta, saldo, taxa_juros, tipo_conta = "Poupança"):
        super().__init__(num_conta, saldo, )
        self.tipo_conta = tipo_conta
        self.taxa_juros = taxa_juros
