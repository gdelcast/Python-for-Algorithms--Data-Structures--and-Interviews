import json
from collections import deque
class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        string = {'val':self.val}
        string['left'] = None if not self.left else self.left.__str__()
        string['right'] = None if not self.right else self.right.__str__()
        return json.dumps(string, separators=(':',','))

    # PreOrder
    def preorder_recursive(self):
        cur = self
        print(cur.val)
        if cur.left:
            cur.left.preorder_recursive()
        if cur.right:
            cur.right.preorder_recursive()

    def preorder_iterative(self):
        stack = [self]
        while stack:
            cur = stack.pop()
            print(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    # InOrder
    def inorder_recursive(self):
        if self.left:
            self.left.inorder_recursive()
        print(self.val)
        if self.right:
            self.right.inorder_recursive()

    def inorder_iterative(self):
        stack = []
        cur = self
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            print(cur.val)
            cur = cur.right


    # PostOrder
    def postorder_iterative(self):
        stack = [self]
        out = []
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            out.append(cur.val)
        [print(n) for n in out[::-1]]


    # Level Order

    def BFSlevelorder_iterative(self):
        stack = deque([self])
        while stack:
            cur = stack.popleft()
            print(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f

#             a
#     b           c
# d       e
#       f

#print(a)
#a.preorder_recursive()
#a.preorder_iterative()
a.inorder_recursive()
print('')
a.inorder_iterative()
#a.postorder_iterative()
#a.BFSlevelorder_iterative()