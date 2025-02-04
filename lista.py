class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.contador = 0  

class ListaEncadeada:
    def __init__(self):
        self.cabeça = None

    def adicionar(self, valor):
        new_node = Node(valor)
        if not self.cabeça:
            self.cabeça = new_node
        else:
            atual = self.cabeça
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = new_node

    def imprimir(self):
        atual = self.cabeça
        elementos = []
        while atual:
            elementos.append(f"[ {atual.valor} ]")
            atual = atual.proximo
        print(" → ".join(elementos))

    def ordenar_decrescente(self):
        if not self.cabeça or not self.cabeça.proximo:
            return

       
        nos = []
        atual = self.cabeça
        while atual:
            nos.append(atual)
            atual = atual.proximo

      
        nos.sort(key=lambda no: (-no.contador, no.valor), reverse=False)

   
        for i in range(len(nos) - 1):
            nos[i].proximo = nos[i + 1]
        nos[-1].proximo = None

  
        self.cabeça = nos[0]


def contador_frequencia(lista, valor):
    atual = lista.cabeça
    while atual and atual.valor != valor:

        atual = atual.proximo

    if not atual:
        print(f"Elemento {valor} não encontrado!")
        return

    atual.contador += 1
    print(f"Contador do valor {valor}: {atual.contador}")
    lista.ordenar_decrescente()
    lista.imprimir()


def transposicao(lista, valor):
    if not lista.cabeça or lista.cabeça.valor == valor:
        return

    anterior = None
    atual = lista.cabeça

    while atual.proximo and atual.proximo.valor != valor:
        anterior = atual
        atual = atual.proximo

    if atual.proximo:
        no_alvo = atual.proximo
        atual.proximo = no_alvo.proximo
        no_alvo.proximo = atual
        if anterior:
            anterior.proximo = no_alvo
        else:
            lista.cabeça = no_alvo

    print(f"Após transposição do valor {valor}:")
    lista.imprimir()


def move_to_front(lista, valor):
    if not lista.cabeça or lista.cabeça.valor == valor:
        return

    anterior = None
    atual = lista.cabeça

    while atual.proximo and atual.proximo.valor != valor:
        anterior = atual
        atual = atual.proximo
        

    if atual.proximo:
        no_alvo = atual.proximo
        atual.proximo = no_alvo.proximo
        no_alvo.proximo = lista.cabeça
        lista.cabeça = no_alvo

    print(f"Após mover o valor {valor} para o início:")
    lista.imprimir()


def interface():
    lista = ListaEncadeada()

    while True:
        print("\nOpções:")
        print("1 - Adicionar valor")
        print("2 - Contador de frequência")
        print("3 - Transposição")
        print("4 - Move-to-front")
        print("5 - Imprimir lista")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor = input("Informe o valor a ser adicionado: ")
            lista.adicionar(valor)
            print(f"Lista após adicionar {valor}:")
            lista.imprimir()

        elif escolha == '2':
            valor = input("Informe o valor para contador de frequência: ")
            contador_frequencia(lista, valor)

        elif escolha == '3':
            valor = input("Informe o valor para transposição: ")
            transposicao(lista, valor)

        elif escolha == '4':
            valor = input("Informe o valor para mover para o início: ")
            move_to_front(lista, valor)

        elif escolha == '5':
            print("Lista atual:")
            lista.imprimir()

        elif escolha == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    interface()
