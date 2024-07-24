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

    def intersectionPoint(self,head1,head2):
        temp1 = head1
        temp2 = head2
        intersectionPoint = 0
        while temp1 and temp2:
            if temp1.val != temp2.val:
                continue
            else:
                intersectionPoint = temp1.val
        return intersectionPoint





def main():
    arr1 = [2,3,9,10,15,18]
    arr2 = [9,8,12,10,15,18]
    myListOperator = LinkedList()
    head1 = myListOperator.createList(arr1)
    head2 = myListOperator.createList(arr2)
    myListOperator.printList(arr1)
    # myListOperator.printList(head2)

    myListOperator.intersectionPoint(head1,head2)
main()

