class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = Node(10)
tree.left = Node(5)
tree.left.left = Node(1)
tree.left.right = Node(8)
tree.left.right.left = Node(6)
tree.left.right.right = Node(9)
tree.right = Node(30)
tree.right.left = Node(20)
tree.right.left.left = Node(21)     #invalid
tree.right.left.right = Node(22)

#               10
#       5                   30
#   1       8         20
#         6   9     15  22  

tree_vals = []
def TraverseInOrder(tree):
    if tree != None:
        TraverseInOrder(tree.left)          # traverse to the most left bottom level
        #print(tree.value)                  
        tree_vals.append(tree.value)        # append to array most left, then parent, then right...
        TraverseInOrder(tree.right)
        
def sort_check(tree_vals):
    print(tree_vals)                        # a BST traverse must be sorted to be valid
    return tree_vals == sorted(tree_vals)

TraverseInOrder(tree)
print(sort_check(tree_vals))








# class BinarySearchTree(object):

#     def __init__(self):
#         self.root = None

#     def insert(self,value):
#         node = Node(value)
#         if not self.root:
#             self.root = node
#         else:
#             c = self.root
#             while c: 
#                 if node.value<=c.value and c.left:
#                     c = c.left
#                 elif node.value<=c.value and not c.left:
#                     c.left = node
#                     break
#                 elif node.value>c.value and c.right:
#                     c = c.right
#                 elif node.value>c.value and not c.right:
#                     c.right = node
#                     break

# tree = BinarySearchTree()       # this is always going to create a valid BST
# tree.insert(10)
# tree.insert(5)
# tree.insert(1)
# tree.insert(8)
# tree.insert(6)
# tree.insert(9)
# tree.insert(30)
# tree.insert(20)
# tree.insert(15)
# tree.insert(22)
