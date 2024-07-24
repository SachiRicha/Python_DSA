def buildGraphWithAdjacencyList(edges,n):
    graph =[[] for i in range(n)]
    for edge in edges:
        src=edge[0]
        des =edge[1]
        weight = edge[2]
        graph[src].append([src,des,weight])
        graph[des].append([des,src,weight])
    return graph

def printGraphInAdjacency(graph):
    for node in graph:
        # print(node,"->",end=" ")
        for edges in node:
                print(edges,end="")


def main():
    edges = [[0,1,10],[0,2,3],[1,3,-3],[2,3,23],[4,5,123],[3,4,23],[4,6,3],[5,7,9],[6,7,9]]
    n = 8
    graph = buildGraphWithAdjacencyList(edges,n)
    printGraphInAdjacency(graph)

main()