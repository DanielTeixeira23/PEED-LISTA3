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

def palindromo(texto):
    p = Pilha()
    palavra = str(texto)
    
    for i in palavra:
        p.push(i)
    
    for j in palavra:
        if j != p.pop():
            return False
    return True
            
frase_digitada = input('Digite uma frase: ')
resultado = palindromo(frase_digitada)

if resultado:
    print('A frase é um palíndromo.')
else: 
    print("A frase não é um palíndromo.")