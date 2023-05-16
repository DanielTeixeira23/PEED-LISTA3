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
    
def verificar(exp):
    p = Pilha()
    for i in exp:
        if i == '(':
            p.push(i)
        elif i == ')':
            if p.get_size() > 0:
                p.pop()
            else:
                p.push(i)
                
    return p.is_empty()
    
expressao = input('Digite a expressão matemática: ')
if verificar(expressao):
    print('A expressão está balanceada.')
else:
    print('A expressão não está balanceada.')