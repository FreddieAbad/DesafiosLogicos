def solution(X,A):
    set_camino=set()
    for i in range(len(A)):
        set_camino.add(A[i])
        if len(set_camino)==X:
            return i
    return -1


A = [1,3,2,4,2,3,5,4]
X=5
print(solution(X,A))