def codificar(texto, desplazamiento):
    texto = texto.lower()
    codificado = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for simbolo in texto:
        if simbolo in alfabeto:
            numero = alfabeto.find(simbolo)
            numero = numero + desplazamiento

            if numero >= len(alfabeto):
                numero -= len(alfabeto)
            elif numero < 0:
                numero += len(alfabeto)
        
            codificado += alfabeto[numero]
        else:
            codificado += simbolo
    return codificado

texto = input("Ingrese el texto: ")
desplazamiento = int(input("Desplazamiento [1-26]: "))

codificado = codificar(texto,desplazamiento)
print ("Mensaje cifrado: ", codificado)