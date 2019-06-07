# binary tree - the data starts from the root.

class Node():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left


class Tree:
    def __init__(self):
        self.root  = None  # this is the root of the Tree data structure
    def contains(self, key):
        found = False
        current = self.root
        while current != None and found ==False:
            if current.key == key:
                found = True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return found

    def update(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
        else:
            current = self.root
            while current != None:
                if current.key == key:
                    current.value = value
                    break
                elif key < current.key:
                    if current.left == None:
                        current.left = Node(key, value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(key, value)
                        break
                    current = current.right

    def get(self, key):
        current = self.root
        while current != None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


    def traverse(self, current, arr):
        if current != None:
            arr.append(current.key)
            self.traverse(current.left, arr)
            self.traverse(current.right, arr)

    def keys(self):
        arr = []
        self.traverse(self.root, arr)
        return arr

    def values(self):
        ks = self.keys()
        return [self.get(k) for k in ks]

tree = Tree()
tree.update("a", 2)
tree.update("c", 4)
tree.update("b", 5)
tree.update("b", 4)
print(tree.keys())
print(tree.values())
print(tree.get("b"))


