

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


# creating object
class LinkedList:
    def createList(self,arr):
        head = None
        temp = None
        for i in range(len(arr)):
            if i == 0:
                head = Node(arr[i])  
                temp = head
            else:
                temp.next = Node(arr[i])   #invoking constructor
                temp = temp.next
        return head
    # printing the LL
    def printList(self,head):
        while head != None:
            print(head.val,end=" ")
            head = head.next

    # deleting the repeated value
    def deleteValue(self,head, value):
        while head.val == value:
            head = head.next
        print(head.val)
        temp = head
        while temp.next != None and temp != None:
            if temp.next.val == value:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head

    # pick intersection point from 2 array
    def intersectList(self,head):



def main():
    arr = [12,12,12,12,12,4,6,7,-43,56,12,12,90,-78,12]
    myListOperator = LinkedList()
    head = myListOperator.createList(arr)
    myListOperator.printList(head)
    print()
    head = myListOperator.deleteValue(head,12)
    myListOperator.printList(head)

main()