from collections import deque


# ##bfs ?¨? ? ?
def bfs(start, arr, visit):
    visit[start] = 1  # ??¬?Έ? λ°©λ¬Έμ²λ¦¬
    
    que = deque()  # ? ? ?Έ
    que.append(start)  # ??¬?Έ?λ₯? ?? ?£??€.
    
    while que:
        now_node = que.pop()  # ?? ?€?΄κ°??? ?Έ?λ₯? λΊ??€.
        
        for i in range(1, n + 1):
            if visit[i] == 0 and arr[now_node][i] == 1:
                que.append(i)  # i?Έ?λ₯? ?? ?£??€.
                visit[i] = 1  # i ?Έ?λ₯? λ°©λ¬Έμ²λ¦¬??€.
        
    return visit


# ##?¬κΈ°μλΆ??° ?? ₯λ°μ
n, m = map(int, input().split())  # n ?Έ?κ°μ, m κ°μ κ°μ
sum = 0  # ?°κ²°μ? κ°μ

# κ°μ ? λ³? ?? ¬ ? ?Έ
arr = [[0] * (n + 1) for i in range(n + 1)]

# ?Έ? κ°μ ? λ³? ?? ¬ λ§λ€κΈ?
for i in range(0, m):
    a, b = map(int, input().split())  # ?Έ? κ°μ κ°μ ? λ³΄μ? ₯
    
    arr[a][b] = 1
    arr[b][a] = 1
    
# κ°μ ? λ³΄ν? ¬ ? μΆλ ₯??μ§? ??Έ?κΈ?
# for i in range(0, n+1):
#     for j in range(0, n+1):
#         print( arr[i][j], end="" )
#     print( end="\n" )

# ?Έ?λ°©λ¬Έ?¬λΆ? λ¦¬μ€?Έ λ§λ€κΈ?
visit = [ 0 for i in range(n + 1) ]
visit[0] = 1  # 0λ²μ§Έ ?Έ?±?€? ????Όλ―?λ‘? λ―Έλ¦¬ 1λ‘? ?€? 

start = 1
flag = True

while flag:
    visit = bfs(start, arr, visit)  # bfs?¨? ?ΈμΆνκ³? λ°νκ°μΌλ‘? λ°©λ¬Έλ°°μ΄? λ°ν
    sum += 1
    
    for i in range(1, n + 1):
        if visit[i] == 0:
            start = i
            break
        if i == n and visit[i] == 1:
            flag = False

print(sum)
