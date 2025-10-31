def adjMatrix():
    graph=[[0]*5 for _ in range(5)]
    edges=[[0,1],[0,2],[0,3],[0,4],[1,3],[1,4],[2,3]]
    for u,v in edges:
        graph[u][v]=1
        graph[v][u]=1
    return graph
#Write your code here
