class Item:
    def __init__(self, value):
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

def converter_bin_octal():
    p = Pilha()

    num = input('Digite um número em binário: ')
    converter_dec = int(num, 2)
    octal = oct(converter_dec)[2:]
    
    p.push(octal) 
    return p

ordem = converter_bin_octal()

while not ordem.is_empty():
    print('Número em octal: ', end='')
    print(ordem.pop(), end='')