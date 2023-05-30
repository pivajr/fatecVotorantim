def fib(i):
    ''' Retorna os i-ésimos números de Fibonacci
        fib(n)
    '''
    if i==0: return 0
    elif i==1: return 1
    else:
        return fib(i-1)+fib(i-2)