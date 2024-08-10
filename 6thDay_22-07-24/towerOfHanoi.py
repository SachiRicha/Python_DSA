def towerOfHanoi(np,source,destination,aux):
    count = 0
    if np == 0:
        return
    towerOfHanoi(np-1,source,aux,destination)
    print("Move",source,"to", destination)
    towerOfHanoi(np-1,aux,destination,source)

def main():
    numberOfPlates = 3
    source, aux,  destination = 'A','B','C'
    towerOfHanoi(numberOfPlates,source,destination,aux)
    
main()
