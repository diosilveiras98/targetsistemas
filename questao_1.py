"""
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
RESPOSTA: soma vale 91

*************************


"""

indice = int(13)
soma = 0
ksoma = 0
while ksoma < indice:
    ksoma = ksoma + 1
    soma = soma + ksoma

print(f"O valor da variável SOMA é: {soma}")





