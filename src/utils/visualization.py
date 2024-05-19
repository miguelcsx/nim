# src/utils/visualization.py

import os
from graphviz import Digraph
from utils.tree import TreeNode


def visualize_game_tree(root: TreeNode) -> None:
    dot = Digraph()
    dot.node('root', 'Game Tree', shape='box')

    def add_nodes_and_edges(nodes: list[TreeNode], parent_name: str) -> None:
        for node in nodes:
            node_name = f"node_{id(node)}"
            player_turn = f"Player's Turn: {node.player}"
            if node.move is not None:
                move_info = f"Move: Pile {node.move[0] + 1}, Take {node.move[1]} objects"
            else:
                player_turn = "Initial State"
                move_info = "Start"
            node_label = f"{player_turn}\n{move_info}"
            dot.node(node_name, node_label)
            dot.edge(parent_name, node_name)
            add_nodes_and_edges(node.children, node_name)

    add_nodes_and_edges([root], 'root')

    # Render the DOT code directly to SVG without saving intermediate files
    svg_bytes = dot.pipe(format='svg')
    
    # Write the SVG content to a file
    with open(os.path.join('.out/', 'game_tree.svg'), 'wb') as f:
        f.write(svg_bytes)

