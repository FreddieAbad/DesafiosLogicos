#performance pesimo
def solution(X, Y, D):
  limite=X^Y
  for i in range(1,limite):
    val_temp=X+D*i
    # print(i, " ",val_temp)
    if val_temp>=Y:
      return i
    else:
      pass


print(solution(10,85,30))

# correcto y en performance correcto
# Busco la diferencia que tiene que transcurrir, con esta diferencia, veo si esta diferencia es multiplo
# de la D dada, si es multiplo el i salto buscado es el resultado de la division entera entre estas
# caso contrario es la division entera mas 1
def solution(X, Y, D):
  diferencia=abs(Y-X)
  i_frog=diferencia//D
  if diferencia%D==0:
    return i_frog
  else:
    return i_frog+1


print(solution(10,85,30))