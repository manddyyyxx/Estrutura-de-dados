class FilaAtendimento:
    
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, nome):
        self.clientes.append(nome)
        print(f"[ENTROU] {nome} entrou na fila!")

    def atender_cliente(self):
        if self.esta_vazia():
            print("Ninguém para atendimento.")
            return None

        cliente_atendido = self.clientes.pop(0)
        print(f"[ATENDIDO] {cliente_atendido} foi chamado(a) e saiu da fila.")
        return cliente_atendido

    def ver_proximo(self):
        if self.esta_vazia():
            return "Fila vazia"
        return self.clientes[0] 

    def esta_vazia(self):
        return len(self.clientes) == 0

    def tamanho_da_fila(self):
        return len(self.clientes)

    def exibir_fila(self):
        return str(self.clientes)



fila_banco = FilaAtendimento()

while True:
    print("      SISTEMA DE FILA (FIFO)")
    print("1. Adicionar pessoa à fila")
    print("2. Atender próximo (remover)")
    print("3. Espiar quem é o próximo")
    print("4. Ver fila completa e tamanho")
    print("5. Sair do sistema")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        nome = input("Digite o nome da pessoa: ")
        if nome.strip(): # Garante que o usuário não digite um nome vazio
            fila_banco.adicionar_cliente(nome)
        else:
            print("Nome inválido. Tente novamente.")
    
    elif opcao == '2':
        fila_banco.atender_cliente()
         
    elif opcao == '3':
        proximo = fila_banco.ver_proximo()
        print(f"Próximo a ser atendido: {proximo}")
      
    elif opcao == '4':
        print(f"Fila atual: {fila_banco.exibir_fila()}")
        print(f"Total de pessoas aguardando: {fila_banco.tamanho_da_fila()}")
        
    elif opcao == '5':
        print("Saindo do sistema... Até logo!")
        break
        
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 5.")