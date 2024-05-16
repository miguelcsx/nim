# src/main.py

import argparse
import os
from datetime import datetime
from game.modes.classic import Classic
from players.human import HumanPlayer
from utils.logger import setup_logger
from utils.tree import generate_tree
from utils.visualization import visualize_game_tree

def parse_arguments():
    parser = argparse.ArgumentParser(description="Play the Nim game.")
    parser.add_argument("--mode", "-m", type=str, default="classic", help="Game mode: classic")
    parser.add_argument("--player1", "-p1", type=str, default="human", help="Player 1 type: human, ai")
    parser.add_argument("--player2", "-p2", type=str, default="ai", help="Player 2 type: human, ai")
    return parser.parse_args()


def create_player(player_type, name):
    if player_type == "human":
        return HumanPlayer(name)
    else:
        raise ValueError(f"Invalid player type: {player_type}")


def main():
    args = parse_arguments()

    if args.mode != "classic":
        raise ValueError(f"Invalid game mode: {args.mode}")
    
    game = Classic()

    initial_piles = game.get_piles()

    root = generate_tree(initial_piles)
    visualize_game_tree(root)

    player1 = create_player(args.player1, "Player 1")
    player2 = create_player(args.player2, "Player 2")


    log_dir = ".logs"
    os.makedirs(log_dir, exist_ok=True)

    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    log_file = os.path.join(log_dir, f"nim_game_{args.mode}_{current_datetime}.log")
    logger = setup_logger("nim_game", log_file)
    
    player1.set_logger(logger)
    player2.set_logger(logger)

    game.set_logger(logger)
    game.play(player1, player2)



if __name__ == "__main__":
    main()
