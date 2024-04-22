val: int = 10
tabela = "0123456789ABCDEF"

# Para binario
x = val
lista = []
while x > 0:
    # print(x, x//2, x%2)
    lista.append(x%2)
    x = x // 2

val_bin = bin(val)

i: int = 0
while i < len(lista)//2:
    temp = lista[i]
    lista[i] = lista[len(lista)-i-1]
    lista[len(lista)-i-1] = temp
    i = i + 1

print(f'{val} ({val_bin}) {lista}')

# Para hexadecimal
val_hex = 0xdeaf
xh = val_hex
listah = []
while xh > 0:
    listah.append(tabela[xh%16])
    xh = xh // 16

i = 0
while i < len(listah)//2:
    temp = listah[i]
    listah[i] = listah[len(listah)-i-1]
    listah[len(listah)-i-1] = temp
    i = i + 1

val_hex_bin = bin(val_hex)

print(f'{val_hex} ({val_hex_bin}) {listah}')
