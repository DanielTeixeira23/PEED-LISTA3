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

def converter_dec_bin(num):
    p = Pilha()
    while num > 0:
        resto = num%2
        num = num//2
        p.push(resto)
    return p

n = int(input('Digite um número em decimal: '))
binario = converter_dec_bin(n)

print('O número em binário é: ', end='')
while not binario.is_empty():
    print(binario.pop(), end='')