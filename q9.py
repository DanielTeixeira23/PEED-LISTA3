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
        return self.size == 0
    
def palindromo(num):
    p = Pilha()
    numeros = str(num)
    
    for i in numeros:
        p.push(i)
    
    for j in numeros:
        if j != p.pop():
            return False
    return True

numero_digitado = int(input('Digite um número: '))
resultado = palindromo(numero_digitado)

if resultado:
    print('O número é um palíndromo.')
else:
    print('O número não é um palíndromo.')