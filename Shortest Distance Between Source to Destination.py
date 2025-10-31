from queue import Queue
def shortestDistance(n, edges, src,dst):
    graph=[[]for _ in range(n)]
    for u,v in edges:
        graph [u].append(v)
        graph[v].append(u)
    visited=[False]*n
    q=Queue() 
    q.put((src,0))
    visited[src]=True 
    while not q.empty():
        node,distance=q.get()
        if node==dst:
            return distance
        for neighbour in graph[node]:
            if not visited[neighbour]:
                q.put((neighbour,distance+1))
                visited[neighbour]=True
    return -1
