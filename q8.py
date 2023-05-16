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
    
def converter_dec_hexadecimal(num):
    p = Pilha()
    while num > 0:
        resto = num%16
        num = num//16
        p.push(hex(resto)[2:].upper())
    return p

x = int(input('Digite um número em decimal: '))
hexadecimal = converter_dec_hexadecimal(x)

print('O número em hexadecimal é: ', end='')
while not hexadecimal.is_empty():
    print(hexadecimal.pop(), end='')