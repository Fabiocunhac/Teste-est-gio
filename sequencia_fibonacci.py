def pertence_a_fibonacci(n):
    if n == 0 or n == 1:
        return True

    a, b = 0, 1
    while b < n:
        a, b = b, a + b

    return b == n

def main():
    while True:
        entrada = input("Digite um número para verificar se pertence à sequência de Fibonacci (ou 'Sair' para encerrar): ")
        
        if entrada.lower() == "sair":
            print("Encerrando o programa...")
            break

        try:
            numero = int(entrada)
            if pertence_a_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci.")
        except ValueError:
            print("Por favor, insira um número inteiro válido ou 'Sair' para encerrar.")

if __name__ == "__main__":
    main()
