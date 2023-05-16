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

def converter_bin_dec(num):
    p = Pilha()
    
    for i in num:
        if i == '0' or i == '1':
            p.push(int(i))
        else:
            raise ValueError('O número digitado não é binário.')
    
    num_dec = 0
    base = 1
    while not p.is_empty():
        num_dec += p.pop() * base
        base *= 2
        
    return num_dec

num = input('Digite um número binário: ')
num_dec = converter_bin_dec(num)
print('Número em decimal:', num_dec, end='')