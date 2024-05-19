# src/main.py

import os
import yaml
import argparse
import threading
from datetime import datetime
from players.ai import AIPlayer
from utils.tree import generate_tree
from players.human import HumanPlayer
from game.modes.classic import Classic
from utils.logger import setup_logger, cleanup_logs
from utils.visualization import visualize_game_tree


def parse_arguments():
    parser = argparse.ArgumentParser(description="Play the Nim game.")
    parser.add_argument("--config", "-c", type=str, default="config.yaml", help="Configuration file")
    args, _ = parser.parse_known_args()

    if args.config:
        return args
    
    parser.add_argument("--debug", "-d", action="store_true", default=False, help="Enable debug mode")
    parser.add_argument("--mode", "-m", type=str, default="classic", help="Game mode: classic")
    parser.add_argument("--player1", "-p1", type=str, default="human", help="Player 1 type: human, ai")
    parser.add_argument("--player2", "-p2", type=str, default="ai", help="Player 2 type: human, ai")
    parser.add_argument("--num_piles", "-n", type=int, default=None, help="Number of piles")
    parser.add_argument("--alpha_beta", "-ab", action="store_true", default=False, help="Use alpha-beta pruning")
    return parser.parse_args()


def load_config(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    
    # Set default values if not provided in the config file
    config.setdefault("debug", False)
    config.setdefault("mode", "classic")
    config.setdefault("player1", "human")
    config.setdefault("player2", "ai")
    config.setdefault("num_piles", None)
    config.setdefault("alpha_beta", False)
    return config


def create_player(player_type, name, use_alpha_beta):
    if player_type == "human":
        return HumanPlayer(name)
    elif player_type == "ai":
        return AIPlayer(name, use_alpha_beta)
    else:
        raise ValueError(f"Invalid player type: {player_type}")


def main():
    args = parse_arguments()

    if args.config:
        config = load_config(args.config)

    if config:
        debug = config.get("debug")
        mode = config.get("mode")
        player1 = config.get("player1")
        player2 = config.get("player2")
        num_piles = config.get("num_piles")
        use_alpha_beta = config.get("alpha_beta")
    else:
        debug = args.debug
        mode = args.mode
        player1 = args.player1
        player2 = args.player2
        num_piles = args.num_piles
        use_alpha_beta = args.alpha_beta

    if mode != "classic":
        raise ValueError(f"Invalid game mode: {mode}")
    
    game = Classic(num_piles)

    initial_piles = game.get_piles()

    # Define a function to run in a thread
    def background_task():
        root = generate_tree(initial_piles)
        visualize_game_tree(root)

    if debug:
        # Create a thread for the background task
        background_thread = threading.Thread(target=background_task)
        
        # Start the background thread
        background_thread.start()

    player1 = create_player(player1, "Player 1", use_alpha_beta)
    player2 = create_player(player2, "Player 2", use_alpha_beta)


    log_dir = ".logs"
    os.makedirs(log_dir, exist_ok=True)

    cleanup_logs(log_dir, 5)

    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    log_file = os.path.join(log_dir, f"nim_game_{mode}_{current_datetime}.log")
    logger = setup_logger("nim_game", log_file)
    
    player1.set_logger(logger)
    player2.set_logger(logger)

    game.set_logger(logger)
    game.play(player1, player2)



if __name__ == "__main__":
    main()
