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

def isPath(graph,src,des,visited_arr):
    if src == des:
        return True
    neighbours = graph[src]
    for i in range(len(neighbours)):
        if neighbours[i] == 1:
            if visited_arr[i] ==0:
                visited_arr[i] = 1
                ans = isPath(graph,i,des,visited_arr)
                if ans == True:
                    return True
    return False


def main():
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,7],[6,7]]
    n = 8
    graph = buildGraph(edges,n)
    # printGraph(graph)
    src = 0
    des =7
    visited_arr = [0 for i in range(n)]
    ans = isPath(graph,src,des,visited_arr)
    print(ans)
main()

