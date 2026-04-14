#contar letras sin espacios
text = input("cuantas letras tiene tu frase: ").strip()
#text.strip() #solo left and right, no altera origen
print(text)
r = text.replace(" ","")# no altera origen, quita y devuele
print(r)

print(f"tu frase tiene {len(r)} letras")

contador =0
for x in text:
    if x !=" ":
        contador +=1
    else:
        continue

print(contador)
#BIEN BRO

contador = 0

for x in text:
    if x.isalpha():
        contador += 1

print(contador)

#by chtgpt