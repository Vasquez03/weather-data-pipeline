arrays = [1, 2, 2, 3, 4, 4, 5]
"""

for value in arrays:
    for x in range(len(arrays)):
        if arrays[x-1] == value:
            print("iguales", value)
            arrays.pop(x-1)
             
        else:
            print("no iguales", value)


print(arrays)



a = [10, 20, 4, 45, 99]
max_value_1 = max(a)
position = a.index(max_value_1)
a.pop(position)
print(max(a))




palabra_original = "pinga"
palabra_original = list(palabra_original)

palabra_invertida = []


for letra in palabra_original[::-1]:
    palabra_invertida.append(letra)


palabra_original = "".join(palabra_original)
palabra_invertida = "".join(palabra_invertida)


if palabra_invertida == palabra_original:
    print("Es un palindromo")

else:
    print("No es un palindromo")

"""



a = "hello"

count = 0
a = list(a)

b = []

for value in a:
    for x in range(len(a)):
        if a[x] == value:
            count+=1
            b.append(count)
             


print(count)


