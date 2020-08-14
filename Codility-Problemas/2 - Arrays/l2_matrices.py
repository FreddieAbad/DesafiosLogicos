lista=[3, 8, 9, 7, 6]
k=3

# for i in range(k):
#   pivote=lista[-1]
#   lista=lista[0:-1]
#   lista.insert(0,pivote)
# print(lista)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A, K):
#     for i in range(K):
#       pivote=A[-1]
#       A=A[0:-1]
#       A.insert(0,pivote)
#     return A

def solution(A, K):
    if not A:
        A=A
    else:
        for i in range(K):
        pivote=A[-1]
        A=A[0:-1]
        A.insert(0,pivote)
    return A


print(solution(lista,k))
print(solution([],k))