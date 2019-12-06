class OrbitTree:
    def __init__(self, root) -> None:
        self.rootNode = Node(root)

    def add(self, parent, data):
        self.rootNode.add(parent, data)

    def count_direct_orbits(self) -> int:
        return self.rootNode.count_direct_children()

    def count_indirect_orbits(self):
        return self.rootNode.count_indirect_children()


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = list()

    def add(self, parent, data):
        if parent == self.data:
            self.children.append(Node(data))
        else:
            for node in self.children:
                node.add(parent, data)

    def count_direct_children(self) -> int:
        count = len(self.children)
        for child in self.children:
            count += child.count_direct_children()
        return count

    def count_indirect_children(self) -> int:
        count = 0
        for child in self.children:
            count += child.count_direct_children() + child.count_indirect_children()
        return count

