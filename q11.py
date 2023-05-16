class Item:
    def __init__ (self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        novoItem = Item(value)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception ('A pilha está vazia')
        valor = self.top.value
        self.top = self.top.next
        self.size -= 1
        return valor
       
    def _top(self):
        if self.size == 0:
            raise Exception('A pilha está vazia')
        return self.top.value
        
    def is_empty(self):
        return self.size == 0
     
    def get_size(self):
        return self.size
    
def ordem_crescente():
    decrescente = []
    p = Pilha()

    print('Digite 0 para parar de digitar os números.')
    while True:
        num = int(input('Digite um número: '))
        if num == 0:
            break
        decrescente.append(num)

    numeros_ordenados = sorted(decrescente, reverse = True)
    
    for i in numeros_ordenados:
        p.push(i)
    return p

ordem = ordem_crescente()

print('Números em ordem crescente: ', end='')
while not ordem.is_empty():
    print(ordem.pop(), end=' ')