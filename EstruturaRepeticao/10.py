numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(2, numero):
    fatorial *= i

print(f"{numero}! = {fatorial}")
