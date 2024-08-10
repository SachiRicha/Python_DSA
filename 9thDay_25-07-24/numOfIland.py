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

def expandNode(graph,i,j,visited,n):
    if i>=n or i<0 or j>=n or j<0 or graph[i][j] == 0 or visited[i][j] == 1:
        return
    visited[i][j] = 1

    expandNode(graph,i+1,j,visited,n)
    expandNode(graph,i-1,j,visited,n)
    expandNode(graph,i,j+1,visited,n)
    expandNode(graph,i,j-1,visited,n)



        
def getNumberOfIsland(graph,n):
    count = 0
    visited = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                expandNode(graph,i,j,visited,n)
                count+=1
    return count



def main():
    global smallestPath
    global largestPath
    edges = [[0,1],[0,2],[2,1],[3,6],[3,4],[6,5],[4,5],[7,8],[9,10],[9,11],[10,11]]
    n = 12
    graph = buildGraph(edges,n)
    # #printGraph(graph)
    src = 0
    visited = [0 for i in range(n)]
    queue = [[0,"0"]]
    matrix =  [[1,1,1,0,0,1],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,1,1,1,0,1],[1,0,0,1,1,0],
        [0,0,0,1,1,0]
    ]
    # ans = getAllCompoents(graph,n)
    # print(ans)
    ans = getNumberOfIsland(matrix,6)
    print(ans)
main()