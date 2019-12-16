class OrbitTree:
    def __init__(self, root) -> None:
        self.rootNode = Node(root)

    def add(self, parent, data):
        self.rootNode.add(parent, data)

    def count_direct_orbits(self) -> int:
        return self.rootNode.count_direct_children()

    def count_indirect_orbits(self):
        return self.rootNode.count_indirect_children()

    def find_LCA(self, data1, data2):
        return self.rootNode.find_LCA(data1, data2)

    def find_path(self, data):
        path = list()
        self.rootNode.find_path(path, data)
        return len(path) - 2

    def find_shortest_path_between(self, data1, data2):
        lca = self.rootNode.find_LCA(data1, data2)
        path1 = list()
        path2 = list()
        lca.find_path(path1, data1)
        lca.find_path(path2, data2)
        return len(path1) + len(path2) - 4


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = list()
        self.parent = None

    def add(self, parent, data):
        if parent == self.data:
            self.children.append(Node(data))
        else:
            for node in self.children:
                node.add(parent, data)

    def add_node(self, parent, node):
        if parent.data == self.data:
            node.parent = self
            self.children.append(node)
        else:
            for node in self.children:
                node.add(parent, node)

    def count_direct_children(self) -> int:
        count = len(self.children)
        for child in self.children:
            count += child.count_direct_children()
        return count

    def find_path(self, path, k):

        # Store this node is path vector. The node will be
        # removed if not in path from root to k
        path.append(self)

        # See if the k is same as root's key
        if self.data == k:
            return True

        # Check if k is found in left or right sub-tree
        for child in self.children:
            if child.find_path(path, k):
                return True

            # If not present in subtree rooted with root, remove
        # root from path and return False

        path.pop()
        return False

    def find_LCA(self, n1, n2):

        # To store paths to n1 and n2 fromthe root
        path1 = []
        path2 = []

        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        if not self.find_path(path1, n1) or not self.find_path(path2, n2):
            return -1

            # Compare the paths to get the first different value
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i - 1]

    def count_indirect_children(self) -> int:
        count = 0
        for child in self.children:
            count += child.count_direct_children() + child.count_indirect_children()
        return count

