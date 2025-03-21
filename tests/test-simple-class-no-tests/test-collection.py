import pythoness


class Node:
    """A node which stores a value"""

    def __init__(self, val):
        """
        Initializes a node with value val with left and right children
        """
        self.val = val
        self.left = None
        self.right = None

    @pythoness.spec(
        "gets val from a Node", related_objs=[__init__], verbose=True, replace=False
    )
    def get_val(self):
        """"""

    @pythoness.spec(
        "Sets a val for a node", related_objs=[__init__], verbose=True, replace=False
    )
    def set_val(self, val):
        """"""

    @pythoness.spec("gets the left child of a node", verbose=True, replace=False)
    def get_left_child(self):
        """"""

    @pythoness.spec("gets the right child of a node", verbose=True, replace=False)
    def get_right_child(self):
        """"""


class Balanced_Binary_Tree:
    """A simple adjacency-list implementation of a balanced binary tree"""

    def __init__(self, val):
        """
        inits the binary tree by creating a root node with value val
        """
        self.root = Node(val)

    @pythoness.spec(
        "gets the height of the binary tree",
        related_objs=[Node, "cls"],
        verbose=True,
        replace=False,
    )
    def get_height(self):
        """"""

    @pythoness.spec(
        "adds node to the proper place in the balanced binary tree",
        related_objs=[Node, "cls"],
        verbose=True,
        replace=False,
    )
    def add_node(self, node):
        """"""


@pythoness.spec("returns a random int")
def get_rand_int():
    """"""


tree = Balanced_Binary_Tree(66)
for x in range(100):
    tree.add_node(Node(get_rand_int()))
print(tree.get_height())
