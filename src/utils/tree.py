# src/utils/tree.py

from collections import deque

class TreeNode:
    def __init__(self, piles, move=None, player=None):
        self.piles = piles
        self.move = move
        self.player = player
        self.children = []

def generate_tree(initial_piles):
    root = TreeNode(initial_piles)
    generate_tree_bfs(root)
    return root

def generate_tree_bfs(root):
    queue = deque([(root, 1)])  # Store nodes along with their depth
    # BFS traversal to generate the game tree
    while queue:
        node, depth = queue.popleft()
        if depth % 2 == 1:
            player = "Player 1"
        else:
            player = "Player 2"
        generate_children(node, player)
        queue.extend((child, depth + 1) for child in node.children)

# Generate children nodes for the current node
def generate_children(node, player):
    piles = node.piles
    for pile_idx, pile in enumerate(piles):
        for num_objects in range(1, len(pile) + 1):
            try:
                new_piles = [deque(p) for p in piles]
                make_move(new_piles, pile_idx, num_objects, player)
                new_node = TreeNode(new_piles, (pile_idx, num_objects), player)
                node.children.append(new_node)
                make_move(new_piles, pile_idx, num_objects, "Player 1" if player == "Player 2" else "Player 2")
            except ValueError:
                continue

# Make a move on the piles
def make_move(piles, pile_idx, num_objects, player_name):
    pile = piles[pile_idx]
    if num_objects < 1 or num_objects > len(pile):
        raise ValueError(f"Invalid number of objects: {num_objects}")

    for _ in range(num_objects):
        pile.popleft()
