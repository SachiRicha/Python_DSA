class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def createList(self,arr):
        head = None
        temp = None
        for i in range(len(arr)):
            if i == 0:
                head = Node(arr[i])
                temp = temp.next



def main():
    arr = [5,2,13,3,8]

main()