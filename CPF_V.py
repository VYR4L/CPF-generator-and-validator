cpf = input("Digite seu CPF")
novo_cpf = cpf[:-2]
total_1 = 0
total_2 = 0
contador_1 = 10
contador_2 = 11
validador = 0
valor_verdade = False

for n in novo_cpf:
    n = int(n)
    validador += n
if validador / 9 == n:
    valor_verdade = True

if valor_verdade:
    print('CPF inválido (por repetição)')
else:
    for index in range(contador_1):
        if contador_1 >= 2:
            total_1 += int(novo_cpf[index]) * contador_1
            contador_1 -= 1

    if 11 - (total_1 % 11) > 9:
        digito_1 = 0
    else:
        digito_1 = 11 - (total_1 % 11)

    digito_1 = str(digito_1)
    novo_cpf = novo_cpf + digito_1

    for index in range(contador_2):
        if contador_2 > 1:
            total_2 += int(novo_cpf[index]) * contador_2
            contador_2 -= 1

    if 11 - (total_2 % 11) > 9:
        digito_2 = 0
    else:
        digito_2 = 11 - (total_2 % 11)

    novo_cpf = novo_cpf + str(digito_2)

    if novo_cpf == cpf:
        print("CPF válido")
    else:
        print('CPF inválido')
