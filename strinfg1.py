def contar_letra_a(texto):
 
    count = texto.lower().count('a')
    return count

def main():
    
    texto = input("Informe uma string: ")
    
    
    quantidade = contar_letra_a(texto)

    if quantidade > 0:
        print(f"A letra 'a'a
               aparece {quantidade} vezes na string.")
    else:
        print("A letra 'a' não está na string.")

if __name__ == "__main__":
    main()