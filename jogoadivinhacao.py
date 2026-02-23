print("-------------------------------")
print("\nBem vindo ao jogo da prestigitação!\n")
print("-------------------------------")

#Definição das variáveis#
n_secreto = 3308
n_tentativas = 5
rodada = 1

for rodada in range(1,n_tentativas + 1):
    print(f"Rodada {rodada} de {n_tentativas}")
    entrada = int(input("Digite um número: "))
    acertou = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto

    if(entrada >100 or entrada < 1):
        print("o valor digitado não é permitido !")

        print(f"\nVocê digitou o número: {entrada}")

        #Verificação de acerto/erro#
        if(acertou):
            print("Parabéns, você acertou o número secreto")
            break
        else:
            if(entrada_maior):
                print("Você errou! O número digitado foi maior que o secreto")
            if(entrada_menor):
                print("Você errou! O número digitado foi menor que o secreto")
        rodada = rodada + 1
    
print("\nFim de jogo")