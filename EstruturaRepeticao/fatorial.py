numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(2, numero + 1):
    fatorial *= i

print(f"{numero}! = {fatorial}")
