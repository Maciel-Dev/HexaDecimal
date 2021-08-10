#Ler diversos numeros inteiros maiores ou iguais a 0
#Base 10
#Calcular e imprimir o equivalente na base 16

def hexaConverter(num10):
    denominador = int(0)
    calc = int(0)
    conversor = int(0)
    string = ""
    novaString = ""

    denominador = 16
    
    calc = num10 // denominador
    resto = num10 % denominador
    
    if calc == 0:
        if num10 >= 0 and num10 <= 9:
            string += f"{num10}"

        else:
            listaLetras = "ABCDEF"
            string += f"{listaLetras[num10-10]}"

    while calc != 0:
        calc = num10 // denominador
        resto = num10 % denominador

        if resto >= 0 and resto <= 9:
            string += f"{resto}"

        elif resto > 9 and resto <= 15:
            listaLetras = "ABCDEF"
            string += f"{listaLetras[resto-10]}"

        num10 = calc

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