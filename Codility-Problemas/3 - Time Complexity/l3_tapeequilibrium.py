def solution (A):
    sum_pp=A[0]
    sum_sp=sum(A[1:])
    diferencia=abs(sum_pp-sum_sp)
    for i in range(1,len(A)):
        dif_comparar=abs(sum_pp-sum_sp)
        if(dif_comparar<diferencia):
            diferencia=dif_comparar
        sum_pp+=A[i]
        sum_sp-=A[i]  
    return diferencia
A= [3,1,2,4,3]
print(solution(A))
# solution(A)


