class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getNextLevelNodes(self,nodes):

        nextNodes = []

        for node in nodes:
            if not node.left is None:
                nextNodes.append(node.left)

            if not node.right is None:
                nextNodes.append(node.right)

        return nextNodes

    def levelOrder(self,root):
        
        data = []
        data.append(root.data)

        nodes = [root]
        
        while 1:
        
            nodes = self.getNextLevelNodes(nodes)
            
            if len(nodes) == 0:
                break

            for node in nodes:
                data.append(node.data)

        print(*data, sep=' ')              
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
