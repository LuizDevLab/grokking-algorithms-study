def buscaMenor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

print(buscaMenor([5, 3, 6, 2, 10]))

def ordenacaoSelecao(arr):
  novo_arr = []
  for i in range(len(arr)):
    menor_indice = buscaMenor(arr)
    novo_arr.append(arr.pop(menor_indice))
  return novo_arr

print(ordenacaoSelecao([5, 3, 6, 2, 10]))