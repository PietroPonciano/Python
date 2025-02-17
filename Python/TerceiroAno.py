N: int
soma1 : float
soma2 : float
soma3 : float
somaT : float
s1 : float
s2 : float
bonus : str
materia : str

materia = input("Qual é a materia a ser calculada? ")

N = int(input("Quantos engajamentos voce teve? "))

soma1 = 0
soma2 = 0
soma3 = 0


for i in range(0, N):
 x = int(input(f"Digite o engajamento {i + 1}: "))
 soma1 = soma1 + x

soma1 = soma1/N


s1 = int(input("Quantos simulados fechados voce teve? "))

for i in range(0, s1):
 y = int(input(f"Digite o simulado {i + 1}: "))
 soma2 = soma2 + y

soma2 = soma2/s1

bonus = str(input(f"voce recebeu algum bonus? (s/n)"))

if bonus == 's' or bonus == 'sim' or bonus == 'Sim' or bonus == 'sIm' or bonus == 'siM' or bonus == 'SIM':
    soma2 = soma2 + 5

s2 = int(input("Quantos simulados abertos voce teve? "))

for i in range(0, s2):
 y = int(input(f"Digite o simulado {i + 1}: "))
 soma3 = soma3 + y

soma3 = soma3/s2

somaT = (soma1 + soma2 + soma3) / 3
if somaT > 100:
    print(f"sua nota total em {materia} foi de 100%")
else:
    print(f"sua nota total em {materia} foi de {somaT}")






