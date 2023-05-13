import random


contador_1 = 10
contador_2 = 11
total_1 = 0
total_2 = 0
nove_digitos = str(random.randint(000000000, 999999999))

for index in range(contador_1):
    if contador_1 >= 2:
        total_1 += int(nove_digitos[index]) * contador_1
        contador_1 -= 1

if 11 - (total_1 % 11) > 9:
    digito_1 = 0
else:
    digito_1 = 11 - (total_1 % 11)

digito_1 = str(digito_1)
novo_cpf = str(nove_digitos) + digito_1

for index in range(contador_2):
    if contador_2 > 1:
        total_2 += int(novo_cpf[index]) * contador_2
        contador_2 -= 1

if 11 - (total_2 % 11) > 9:
    digito_2 = 0
else:
    digito_2 = 11 - (total_2 % 11)

novo_cpf = novo_cpf + str(digito_2)
print(novo_cpf)
