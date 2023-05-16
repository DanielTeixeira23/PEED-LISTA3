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

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            while operadores._top() != '(':
                posfixa.append(operadores.pop())
            operadores.pop()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores._top() != '(' \
                and precedencia[caracter] <= precedencia[operadores._top()]:
                posfixa.append(operadores.pop())
            operadores.push(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.pop())
    return ''.join(posfixa)

def calcular(exp):
    p = Pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.push(caractere)
        else:
            num2 = p.pop()
            num1 = p.pop()
            if caractere == '+':
                resultado = int(num1) + int(num2)
                p.push(str(resultado))
            elif caractere == '-':
                resultado = int(num1) - int(num2)
                p.push(str(resultado))
            elif caractere == '*':
                resultado = int(num1) * int(num2)
                p.push(str(resultado))
            elif caractere == '/':
                resultado = int(num1) / int(num2)
                p.push(str(resultado))
    return p.pop() 

s = input('Digite a expressão posfixa: ')
pos_fixada = infixa_para_posfixa(s)
r = calcular(pos_fixada)
print('Resultado: ', r)