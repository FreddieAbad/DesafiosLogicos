
def funcionbynarygap(N):
  max_dif=0
  n_str=bin(N)
  n_str=n_str[2:]
  diferencias=[x for x, v in enumerate(n_str) if v == '1']
  if not diferencias:
    max_dif=0
  if(len(diferencias)==1):
    if(diferencias[0]==0):
      max_dif=0
    else:
      max_dif=diferencias[0]-1
  if(len(diferencias)>1):
    maximos=[]
    for i in range(len(diferencias)):
      if(i!=len(diferencias) and i!=len(diferencias)-1):
        maximos.append(abs(diferencias[i]-diferencias[i+1]))
    if not maximos:
      max_dif=0
    else:
      max_dif=max(maximos)-1
  return max_dif


N=funcionbynarygap(1041)
print(N)

N=funcionbynarygap(32)
print(N)
