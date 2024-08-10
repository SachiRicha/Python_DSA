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


def isCyclic(graph,n,visited):
    queue = []
    queue.append([0,'0'])
    visited = [0 for i in range(n)]
    while len(queue) > 0:
        poppedElement = queue.pop(0)
        currentNode = poppedElement[0]
        if visited[currentNode]:
            return True
        # psf = poppedElement[1]
        visited[currentNode] = 1
        # print(currentNode,"->",psf)
        nbrs = graph[currentNode]
        for i in range(len(nbrs)):
            if nbrs[i] == 1 and visited[i] == 0:
                # queue.append([i,psf+str(i)])
                return True
    return False



def main():
    edges = [[0,1],[0,2],[1,3]]
    n = 8
    src = 0
    # des = 7
    graph = buildGraph(edges,n)
    visited = [0 for i in range(n)]
    # printGraph(graph)
    queue = [[0,'0']]
    ans = isCyclic(graph,n,visited)
    print(ans)
main()