produto = "camiseta"
preco = 50.00
desconto = 0.20

preco_com_desconto = preco * (1 - desconto)

print(f'O preço do {produto} é R${preco}, com desconto fica R$ {preco_com_desconto:.2f}')