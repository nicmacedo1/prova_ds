valor_produto = float(input("Digite o valor de um produto: "))
desconto = float(input("Digite o desconto: "))

produto_desconto = valor_produto / desconto
total = valor_produto - produto_desconto
print(total)