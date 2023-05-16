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
    
def converter_hexa_dec(num):
    p = Pilha()
    
    for i in num:
        if i.isdigit():
            p.push(int(i))
        elif i == 'a' or i == 'A':
            p.push(10)
        elif i == 'b' or i == 'B':
            p.push(11)
        elif i == 'c' or i == 'C':
            p.push(12)
        elif i == 'd' or i == 'D':
            p.push(13)
        elif i == 'e' or i == 'E':
            p.push(14)
        elif i == 'f' or i == 'F':
            p.push(15)
       
    num_dec = 0
    base = 1
    while not p.is_empty():
        num_dec += p.pop() * base
        base *= 16
        
    return num_dec

num = input('Digite um número em hexadecimal: ')
resultado = converter_hexa_dec(num)
print('Número em decimal:', resultado, end='')