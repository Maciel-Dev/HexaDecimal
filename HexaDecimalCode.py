#Ler diversos numeros inteiros maiores ou iguais a 0
#Base 10
#Calcular e imprimir o equivalente na base 16

def f_base10tobase16(num10):
    denominador = int(0)
    calc = int(0)
    conversor = int(0)
    string = ""

    denominador = 16
    
    calc = num10 // denominador
    resto = calc % denominador

    while calc > 0:

        if resto >= 0 and resto <= 9:
            string += f"{resto}"

        elif resto > 9 and resto <= 15:
            listaLetras = "ABCDEF"
            string += f"{listaLetras[resto-10]}"
            print(listaLetras[resto-10])

        num10 = calc
        calc = num10 // denominador
        resto = calc % denominador
       
        print(string)






def main():

    #Variáveis
    num = int(0)

    num = int(input())
    if num >= 0:
        print(f"BASE10={num} BASE16={f_base10tobase16(num)}")

    


    

if __name__ == "__main__":
    main()