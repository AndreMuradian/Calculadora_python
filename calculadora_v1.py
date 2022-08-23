# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada: ")

soma = "1 - Soma"
subtração = "2 - Subtração"
multiplicação = "3 - Multiplicação"
divisão = "4 - Divisão"

print(soma)
print(subtração)
print(multiplicação)
print(divisão)

escolha = int(input("Digite a sua opção: 1,2,3 ou 4 " ))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == 1:
    def somaFunc(num1, num2):
        return num1 + num2
    print("O resultado é: " + str(somaFunc(num1, num2)))
#print(somaFunc(num1, num2)) --- isso daria errado. (olhar indentação)
#o print deve estar dentro da funçao e nao dentro do if
elif escolha == 2:
    def subFunc(num1, num2):
            return num1 - num2
    print("O resultado é: " + str(subFunc(num1, num2)))

elif escolha == 3:
    def multiFunc(num1, num2):
        return num1 * num2
    print("O resultado é: " + str(multiFunc(num1, num2)))

elif escolha == 4:
    def divFunc(num1,  num2):
        return num1 / num2
    print("O resultado é: " + str(divFunc(num1,num2)))

else:
    print("Esse numero é inválido")



