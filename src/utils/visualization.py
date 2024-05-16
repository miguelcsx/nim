# src/utils/visualization.py

import os
from graphviz import Digraph


def visualize_game_tree(root):
    dot = Digraph()
    dot.node('root', 'Initial State')

    def add_nodes_and_edges(nodes, parent_name):
        for node in nodes:
            node_name = f"node_{id(node)}"
            player_turn = f"Player's Turn: {node.player}"
            if node.move is not None:
                move_info = f"Move: Pile {node.move[0] + 1}, Take {node.move[1]} objects"
            else:
                move_info = "No Move"
            node_label = f"{player_turn}\n{move_info}"
            if not node.children:
                winner = get_winner(node.player)
                node_label += f"\nWinner: {winner}"
            dot.node(node_name, node_label)
            dot.edge(parent_name, node_name)
            add_nodes_and_edges(node.children, node_name)

    add_nodes_and_edges([root], 'root')

    # Render the DOT code directly to SVG without saving intermediate files
    svg_bytes = dot.pipe(format='svg')
    
    # Write the SVG content to a file
    with open(os.path.join('.out/', 'game_tree.svg'), 'wb') as f:
        f.write(svg_bytes)


def get_winner(player):
    if player == "Player 1":
        return "Player 2"
    else:
        return "Player 1"