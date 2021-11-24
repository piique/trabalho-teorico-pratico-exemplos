# https://docs.python.org/3.1/library/string.html#string-formatting

preco = 20.5
unidades = 13

# %s qualquer objeto que possa ser representado como string (str, int, float)
# %d inteiros (int)
# %f ponto flutuante (float)
# %.2f ponto flutuante com duas casas decimais (float)
# %x hexadecimal (int)
# %X hexadecimal (int)

text_final = 'Qtd Produto: %X; Preço: %s Total: %.2f' % (unidades, preco, unidades * preco)
print(text_final)

print("Qtd Produto: %s; Preço: %s Total: %.2f" % (unidades, preco, preco * unidades))

print("Qtd Produto: {}; Preço: {} Total: {}".format(unidades, preco, preco * unidades))

print("Qtd Produto: {valor_x}; Preço: {valor_y}; Total: {valor_total}"
      .format(valor_x=unidades, valor_y=preco, valor_total=preco * unidades))
