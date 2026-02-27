print("-------------------------------")
print("\nBem vindo ao jogo da prestigitação!\n")
print("-------------------------------")

#Definição das variáveis#
n_secreto = 3308
n_tentativas = 0 
rodada = 1
pontos = 1000

print("Níveis de dificuldade")
print("\n(1) fácil (2) Médio (3)díficil aleatório\n")
nivel = int(input("defina um nível"))

if(nivel == 1):
    n_tentativas = 10
elif(nivel == 2):
    n_tentativas = 7
elif(nivel == 3):
    n_tentativas = 3
else:
    n_tentativas = rd.randrange(1,50)

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
            print(f"Parabéns (ou não)! Você fez {pontos} pontos.")
            break
        else:
            if(entrada_maior):
                print("Você errou! O número digitado foi maior que o secreto")
            if(entrada_menor):
                print("Você errou! O número digitado foi menor que o secreto")

        pontos_perdidos = abs(n_secreto - entrada) #(80 - 100) = 
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1
    
print("\nFim de jogo")