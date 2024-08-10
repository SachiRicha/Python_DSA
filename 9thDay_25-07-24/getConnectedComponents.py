def buildGraph(edges,n):
    graph = [[0 for i in range(n)] for j in range(n)]
    for e in edges:
        src = e[0]
        des = e[1]

        graph[src][des] = 1
        graph[des][src] = 1
    return graph

def printGraph(graph):
    for row in graph:
        for e in row:
            print(e,end=" ")
        print()
    
def getCurrentComponent(graph,src,visited,currentComponent):
    visited[src] = 1
    currentComponent.append(src)
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1 and visited[i] == 0:
            getCurrentComponent(graph,i,visited,currentComponent)
    
def getAllComponents(graph,n):
    visited = [0 for i in range(n)]
    ans = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            currentComponent = []
            getCurrentComponent(graph,i,visited,currentComponent)
            ans.append(currentComponent)
    return ans
    
def main():
    edges = [[0,1],[0,2],[2,1],[3,6],[3,4],[6,5],[4,5],[7,8],[9,10],[9,11],[10,11]]
    n = 12
    graph = buildGraph(edges,n)
    # printGraph(graph)
    src = 0
    visited_arr = [0 for i in range(n)]
    ans = getAllComponents(graph,n)
    print(ans)
main()