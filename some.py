def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0: return x / y
    else     : return 'Division is impossible'
    
def calculator():
    x = int(input('First: '))
    y = int(input('Second: '))
    op = input('Operator: ')
    if   op == '+': print(add(x, y))
    elif op == '-': print(sub(x, y))
    elif op == '*': print(mul(x, y))
    elif op == '/': print(div(x, y))
    else          : print('Invalid operator input')
    
pi = 3
l = [12, 4, 8]
e = 2.7

def floordiv(x, y):
	return x // y

u = 34
