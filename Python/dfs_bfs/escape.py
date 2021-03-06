from collections import deque

n, m = map(int, input().split())

arr = list()

# 2μ°¨μ λ¦¬μ€?Έ? λ§? ? λ³? ?? ₯λ°κΈ°
for i in range(0, n):
    arr.append(list(map(int, input())))
    
# ?΄??  4λ°©ν₯ ? ?(??μ’μ°)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    sum = 1
    
    # ??¬ λ°°μ΄ κ°? 0?Όλ‘? λ°κΏμ€μ λ°©λ¬Έμ²λ¦¬
    arr[x][y] = 0
    
    # ?°? ? ?Έ λ°? x,yκ°? μΆκ?
    que = deque()
    que.append((x, y))
    
    # ?κ°? λΉ? ?κΉμ? λ°λ³΅??€.
    while que:
        # ?? κ°? ? κ±?
        now_x, now_y = que.popleft()
        
        # ??¬ ?μΉμ? ?€ λ°©ν₯?Όλ‘? ?μΉ? ??Έ
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]
            
            # λ°°μ΄? λ²μ΄?? κ°μ΄λ©? ?€? ??
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
                
            # λ°°μ΄κ°μ΄1?΄κ³?, x?? yκ°? κΈ°μ‘΄? x, yλ³΄λ€ ??? κ²½μ° ?€?
            if arr[x][y] == 1 and (x > now_x or y > now_y):
                sum += 1
                que.append((x, y))
    
    return sum 

                
# bfs?€?
sum = bfs(0, 0)
print(sum)
