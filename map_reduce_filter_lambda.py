from functools import reduce

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

print(list(map(lambda x,y:x+y, a, b))) # aplica a função lambda em todos os elementos das listas, criando uma terceira lista com a soma de 'a' e 'b'
print(reduce(lambda x,y:x+y, a)) # aplica a função lambda em 'a', somando cada elemento da lista até chegar a um resultado final
print(list(filter(lambda x:x%2==0, a))) # aplica a função lambda em 'a', retornando uma lista onde o resto da divisão é zero (true)