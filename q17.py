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
    
def converter_octal_dec(num):
    p = Pilha()
    
    for i in num:
        p.push(int(i))
        
    num_dec = 0
    base = 1
    while not p.is_empty():
        num_dec += p.pop() * base
        base *= 8
    
    return num_dec

num = input('Digite o número em octal: ')
resultado = converter_octal_dec(num)
print('Número em decimal: ', resultado, end='')