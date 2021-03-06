def dfs(graph, v, visited):
    # ??¬ ?Έ?λ₯? λ°©λ¬Έμ²λ¦¬
    visited[v] = True
    print(v, end=' ')

    # ??¬ ?Έ??? ?°κ²°λ ?€λ₯? ?Έ?λ₯? ?¬κ·?? ?Όλ‘? λ°©λ¬Έ
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# κ°? ?Έ?κ°? ?°κ²°λ ? λ³΄λ?? λ¦¬μ€?Έ ?λ£ν?Όλ‘? ??(2μ°¨μ λ¦¬μ€?Έ)
graph = [
         [],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]
]

# κ°? ?Έ?κ°? λ°©λ¬Έ? ? λ³΄λ?? λ¦¬μ€?Έ ?λ£ν?Όλ‘? ??(1μ°¨μ λ¦¬μ€?Έ)
visited = [False] * 9
# print( visited ) => [False, False, False, False, False, False, False, False, False]

# ? ?? DFS ?¨? ?ΈμΆ?
dfs(graph, 1, visited)
