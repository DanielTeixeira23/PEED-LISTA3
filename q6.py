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
        if i == '(' or i == '[' or i == '{':
            p.push(i)
        elif i == ')' or i == ']' or i == '}':
            if p.is_empty():
                return False
            topo = p.pop()
            if i == ')' and topo != '(':
                return False
            if i == ']' and topo != '[':
                return False
            if i == '}' and topo != '{':
                return False
                
    return p.is_empty()
    
expressao = input('Digite a expressão: ')
resultado = verificar(expressao)

if resultado:
    print('Os caracteres estão balanceados.')
else:
    print('Os caracteres não estão balanceados.')