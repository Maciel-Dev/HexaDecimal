#Ler diversos numeros inteiros maiores ou iguais a 0
#Base 10
#Calcular e imprimir o equivalente na base 16

#Define Função para conversão
#Recebe argumento inteiro
def hexaConverter(num10):

    #Declaração de variáveis
    denominador = int(0)
    calc = int(0)
    string = ""
    novaString = ""

    denominador = 16
    
    #Cálculo recebe divisão inteira
    #Resto recebe o resto da divisão
    calc = num10 // denominador
    resto = num10 % denominador
    
    #Desvio de fluxo
    #Caso o valor de calc seja igual a 0
    if calc == 0:

        #Desvio de fluxo
        #Caso o num10 esteja entre 0 e 9
        if num10 >= 0 and num10 <= 9:
            string += f"{num10}"

        #Desvio de Fluxo
        #Caso o num10 seja maior do que 9
        else:
            listaLetras = "ABCDEF"
            string += f"{listaLetras[num10-10]}"

    #Condição para continuidade da repetição
    #Enquanto divisão inteira for diferente de 0
    while calc != 0:

        calc = num10 // denominador
        resto = num10 % denominador

        #Desvio de fluxo
        #Caso o resto esteja entre 0 e 9
        if resto >= 0 and resto <= 9:
            string += f"{resto}"

        #Desvio de fluxo
        #Caso o resto esteja entre 10 e 15
        elif resto > 9 and resto <= 15:
            #String com letras possíveis em hexadecimal
            listaLetras = "ABCDEF"
            #Obtém a letra correspondente ao resultado do resto
            string += f"{listaLetras[resto-10]}"

        #Atualização da variável calc
        num10 = calc

    #Inversão do resultado
    for let in range(len(string)):
        novaString += f"{string[(len(string)-1) - let]}"

    return novaString


def main():

    #Variáveis
    num = int(0)

    num = int(input())

    while num >= 0:
        print(f"BASE10={num} BASE16={hexaConverter(num)}")
        num = int(input())

if __name__ == "__main__":
    main()