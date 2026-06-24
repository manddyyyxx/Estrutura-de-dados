class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __gt__(self, other):
        return self.nome.lower() > other.nome.lower()

    def __lt__(self, other):
        return self.nome.lower() < other.nome.lower()

    def __str__(self):
        return f"Nome: {self.nome} | Telefone: {self.telefone}"


class Node:
    def __init__(self, content):
        self.left = None
        self.right = None
        self.content = content  

class Tree:
    def __init__(self):
        self.root = None

    def add(self, content, root=None):
        if self.root is None:
            self.root = Node(content)
            return

        if root is None:
            root = self.root

        if content > root.content:
            if root.right is None:
                root.right = Node(content)
            else:
                self.add(content, root.right)
        else:
            if root.left is None:
                root.left = Node(content)
            else:
                self.add(content, root.left)

    def printTree(self, root=None):
        if self.root is None:
            print("A lista está vazia.")
            return

        if root is None:
            root = self.root

        if root.left is not None:
            self.printTree(root.left)

        print(root.content)

        if root.right is not None:
            self.printTree(root.right)

    def search(self, nome, root=None):
        if self.root is None:
            return None

        if root is None:
            root = self.root

        if nome.lower() == root.content.nome.lower():
            return root.content
        elif nome.lower() > root.content.nome.lower():
            if root.right is None:
                return None
            return self.search(nome, root.right)
        else:
            if root.left is None:
                return None
            return self.search(nome, root.left)

    def remove(self, nome):
        self.root = self._remove_recursive(self.root, nome)

    def _remove_recursive(self, root, nome):
        if root is None:
            return root

        if nome.lower() < root.content.nome.lower():
            root.left = self._remove_recursive(root.left, nome)
        elif nome.lower() > root.content.nome.lower():
            root.right = self._remove_recursive(root.right, nome)
        
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

           
            substituto = self._min_value_node(root.right)
            root.content = substituto.content
            root.right = self._remove_recursive(root.right, substituto.content.nome)

        return root

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    agenda = Tree()

    agenda.add(Contato("Laura", "99999-1111"))
    agenda.add(Contato("Diana", "99999-2222"))
    agenda.add(Contato("Claudio", "99999-3333"))
    agenda.add(Contato("Lucas", "99999-0001"))     
    agenda.add(Contato("Daniel", "99999-0002"))    
    agenda.add(Contato("Rafael", "99999-0003"))    
    agenda.add(Contato("Beatriz", "99999-0004"))    
    agenda.add(Contato("Gabriel", "99999-0005"))    
    agenda.add(Contato("Mariana", "99999-0006"))    
    agenda.add(Contato("Vanessa", "99999-0007"))    

    while True:
        print("\n=== AGENDA TELEFÔNICA (BST) ===")
        print("1. Adicionar Contato")
        print("2. Buscar Telefone")
        print("3. Remover Contato")
        print("4. Listar Todos os Contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda.add(Contato(nome, telefone))
            print(f"Contato de {nome} adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Digite o nome para buscar: ")
            resultado = agenda.search(nome)
            if resultado:
                print(f"\n Encontrado -> {resultado}")
            else:
                print("\n Contato não encontrado.")

        elif opcao == "3":
            nome = input("Digite o nome para remover: ")
            if agenda.search(nome):
                agenda.remove(nome)
                print(f"Contato de {nome} removido!")
            else:
                print("Esse contato não existe na agenda.")

        elif opcao == "4":
            print("\n--- Lista de Contatos em Ordem Alfabética ---")
            agenda.printTree()

        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

