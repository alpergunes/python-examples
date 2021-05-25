#calculator

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2


operations ={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div
}




finish = False
while not finish:
    
    num1 =  int(input('Whats the first number: '))
    
    for symbol in operations:
        print(symbol)
    operations_symbol = input('pick an operation from the line above:')
    num2 = int(input('Whats the second number:'))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1,num2)
    print(f'{num1}{operations_symbol}{num2}={answer}')
    q = input('type y contionu or type n exit')
    if q == 'n':
        finish= True
    
