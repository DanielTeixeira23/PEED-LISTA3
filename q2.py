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
       
    def _top (self):
        if self.size == 0:
            raise Exception('A pilha está vazia')
        return self.top.value
        
    def is_empty(self):
        return self.size == 0
     
    def get_tamanho(self):
        return self.size
            
def inverso(frase):
    palavras = frase.split()
    p = Pilha()
    
    for i in palavras:
        p.push(i)
       
    frase_inversa = ""
    while not p.is_empty():
        frase_inversa += p.pop() + " "
    return frase_inversa
    
texto = input('Digite uma frase: ')
palavra = inverso(texto)
print(palavra)