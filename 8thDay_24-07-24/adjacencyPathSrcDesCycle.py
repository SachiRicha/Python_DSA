# dfs

def buildGraphWithAdjacencyList(edges,n):
    graph =[[] for i in range(n)]
    for edge in edges:
        src=edge[0]
        des =edge[1]
        weight = edge[2]
        graph[src].append([src,des,weight])
    #     graph[des].append([des,src,weight])
    return graph

def printGraphInAdjacency(graph):
    for node in graph:
        # print(node,"->",end=" ")
        for edges in node:
                print(edges,end="")

def isPath(graph,src,des,visited):
    if src==des:
        return True
    neighbours = graph[src]
    for i in neighbours:
        if visited[i[1]] == 0:
            visited[i[1]] = 1
            ans = isPath(graph,i[1],des,visited)
            if ans == True:
                return True
    return False
    

# source se source tho cycle hoga
def main():
    edges = [[0,1,8],[1,3,2],[2,1,-1],[3,4,3],[3,5,5],[4,1,9],[5,6,6],[7,6,7]]
    n = 8
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    graph = buildGraphWithAdjacencyList(edges,n)
    # printGraphInAdjacency(graph)
    ans = isPath(graph,src,des,visited)
    print(ans)
main()