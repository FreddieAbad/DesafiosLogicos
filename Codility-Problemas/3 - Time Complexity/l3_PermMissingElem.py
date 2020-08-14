#sin errores pero mal performance
def solution (A):
  complete_A= [*range(1, len(A)+2, 1)]
  l3 = [x for x in complete_A if x not in A]
  return l3[0]

#usa el concepto de suma de gauss o serie divergente
#sin errores buen performance
# la diferencia entre la suma de la lista dada y la suma de la serie divergente es el numero falante
def solution (A):
  limite=len(A)+1
  sum_limite=limite*(limite+1)/2
  sum_A=sum(A)
  return abs(int(sum_limite-sum_A))