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
    
def converter_dec(num):
    p = Pilha()

    for i in range(len(num)-1,0,-1):
        if num[i].isdigit():
            p.push(num[i])

    r = ""
    while not p.is_empty():
        r += p.pop()

    return int(r)

numero = input('Digite um número: ')
resultado = converter_dec(numero)
print(resultado, end='')