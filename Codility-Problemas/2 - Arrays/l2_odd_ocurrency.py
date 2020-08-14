lista=[9, 3, 9, 3, 9 , 7, 9]
def solution(A):
  sorted_array=sorted(A)
  for i in range(0,len(sorted_array),2):
    if i+1 ==len(sorted_array):
      return sorted_array[i]
    if sorted_array[i]!=sorted_array[i+1]:
      return sorted_array[i]
print(solution(lista))