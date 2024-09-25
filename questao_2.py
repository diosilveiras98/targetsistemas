"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""
#Funcao que gera a sequencia fibonacci
def fib_sequencia(n):
    fib_sequencia = [0, 1]
    while fib_sequencia[-1] <n:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return fib_sequencia

#Função que verifica se o numero a ser inserido pelo usuario pertence a sequência
def verificacao_fibonacci(numero):

    fib_seq = fib_sequencia(numero)
    if numero in fib_seq:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência Fibonacci."

#inserção do numero pelo usuario
numero_informado = int(input("Informe um número:"))
resultado = verificacao_fibonacci(numero_informado)
#Retorno de verificação com mensagem de pertencimento ou não pertencimento a sequência
print(resultado)

