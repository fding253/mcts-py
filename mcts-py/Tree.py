from abc import ABC, abstractmethod


class AbstractGameState(ABC):
    """
    Abstract object representing a game state. 
    Define a specific game state depending on game.
    """
    def __init__(self):
        pass

    @property
    @abstractmethod
    def children(self):
        pass

    @property
    @abstractmethod
    def random_child(self):
        pass

    @property
    @abstractmethod
    def is_terminal(self):
        pass

class MCTSTreeNode(object):
    """
    """
    def __init__(self, game_state, parent=None):
        """
        Node in the MC search tree. Each node represents a game state, with 
        references to the node's parent and a list of children.
        """
        self.game_state = game_state
        self.parent = parent
        self.children = list()


class MCTS(object):
    """
    """
    def __init__(self, root):
        self.root = root

    def _select(self, node):
        """
        Select an unsimulated child node.
        """
        pass

    def _expand(self, node):
        """
        If node is not a leaf, create child nodes and select.
        """
        pass

    def _simulate(self, node):
        """
        Complete playout from node.
        """
        pass

    def _backpropagate(self, node):
        """
        Propagate information from simulation step back up the tree.
        """
        pass
