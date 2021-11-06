from collections import deque
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        string = {'val':self.val}
        if self.children:
            string['children'] = [child.__str__() for child in self.children]
        return str(string)

    def dfs_recursive(self):    # PREORDER
        print(self.val)
        if self.children:
            for child in self.children:
                child.dfs_recursive()

    def dfs_iterative(self):    # PREORDER
        stack = [self]
        while stack:
            cur = stack.pop()
            print(cur.val)
            if cur.children:
                stack += cur.children[::-1]

    def dfs_postorder(self):    # POST ORDER
        stack = [self]
        out = []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            if cur.children:
                stack += cur.children
        for n in out[::-1]:
            print(n)


    def bfs_iterative(self):    # LEVEL ORDERED
        queue = deque([self])
        while queue:
            cur = queue.pop()
            print(cur.val)
            if cur.children:
                queue.extendleft(cur.children)



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.children = [b,c,d]
b.children = [e,f]

#print(a)
#a.dfs_recursive()
#a.dfs_iterative()
a.dfs_postorder()
#a.bfs_iterative()