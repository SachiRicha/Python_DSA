# 1 = push node on the left
# 2 = push node on right
# 3 = pop the topmost element

class Node:
    def __init__(self,data):
        self.data = data
        self.index = 1
        self .left = None
        self.right = None

class Tree:
    def buildTree(self,arr):
        st = []
        node = Node(arr[0])
        st.append(node)
        i = 1
        while len(st)>0 and i <len(arr):
            if arr[i] == None:
                i+=1
                continue
            newNode = Node(arr[i])
            peekNode = st[-1]
            if peekNode.index == 1:
                peekNode.left = newNode
                peekNode.index+=1
            elif peekNode.index == 2:
                peekNode.right = newNode
                peekNode.index+=1
            else:
                st.pop()
            # st.append(Node(arr[i]))
            st.append(newNode)
            i+=1
        return node

    def printTree(self,node):
        if node == None:
            print(None,end=" ")
            return
        # print("." if node.left == None else node.left.data,"None" if node.right == None else node.right.data)
        print(node.data,end=" ")
        self.printTree(node.left)
        self.printTree(node.right)

    def getMax(self,node):
        if node == None:
            return float("-inf")
        leftMax = self.getMax(node.left)
        rightMax = self.getMax(node.right)
        return max(node.data,max(leftMax,rightMax))

    def getMinimum(self,node):
        if node == None:
            return float("+inf")
        leftMin = self.getMinimum(node.left)
        rightMin = self.getMinimum(node.right)

        return min(node.data,min(leftMin,rightMin))

    def getHeight(self,node):
        if node == None:
            return
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        return max(leftHeight,rightHeight)


     
def main():
    arr = [1,2,4,7,None,None,None,5,None,8,None,None,3,None,6,None,None]  #hard Code this array
    t = Tree()
    tree = t.buildTree(arr)
    # node = Node(arr[0])
    t.printTree(tree)
    maximumValue = t.getMax(tree)
    print(maximumValue)
    # minimumValue = t.getMinimum(tree)
    # print(minimumValue)
    # t.height(tree)
    # height = t.getHeight(tree)
    # print(height+1)
main()   