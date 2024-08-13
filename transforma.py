def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Solicita ao usuário que digite um número
numero_decimal = int(input("Digite um número decimal: "))

# Converte o número para binário
resultado_binario = decimal_para_binario(numero_decimal)

# Exibe o resultado
print(f"O número {numero_decimal} em binário é {resultado_binario}.")
