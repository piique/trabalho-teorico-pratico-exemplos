
# if elif else
print('\nif elif else: ')
variavel = 3
if(variavel < 3):
    print("Menor")
elif(variavel > 3):
    print("Maior")
else:
    print("Igual!")

# for
print('\nfor: ')
for i in range(0, 10):
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# while
print('\nwhile: ')
variavel = 2
while(True):
    variavel *= 2
    print(variavel)  # 2, 4, 8, 16, 32, 64
    if(variavel == 64):
        break
