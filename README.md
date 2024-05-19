# Nim
:robot: Minimax with alpha-beta pruning for the game of Nim.

## Overview

**Nim** is a mathematical game of strategy in which two players take turns removing objects from distinct heaps. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap.

## Features

- **Classic Mode**: Play the classic version of Nim with configurable options.
- **AI Mode**: Play against an AI opponent that uses the minimax algorithm with alpha-beta pruning to make decisions.
- **Configurability**: Adjust game parameters such as the number of piles and player types through a configuration file.
- **Logging**: Logs of gameplays are saved in the `.logs` directory for reference and analysis.

## Usage

1. Clone the repository:
```bash
git clone https://github.com/miguelcsx/nim.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the game settings in the `config.yaml` file.

4. Run the game:
```bash
python src/main.py
```

## Configuration Options

- **debug**: Enable debug mode (creates a graph visualization of the decision tree).
- **mode**: Game mode (currently supports *classic* or *misere*).
- **player1**: Type of player 1 (human or ai).
- **player2**: Type of player 2 (human or ai).
- **num_piles**: Number of piles in the game.
- **alpha_beta**: Use alpha-beta pruning in the minimax algorithm for the AI player.

### Config File
```yaml
debug: true
mode: misere
player1: human
player2: ai
num_piles: 3
alpha_beta: true
```

### Command-Line Arguments

You can specify the configuration file through the `--config` argument:
```bash
python src/main.py --config config.yaml
```

You can also specify the game settings through command-line arguments. For example:
```bash
python src/main.py --debug --mode classic --player1 human --player2 ai --num_piles 3 --alpha_beta
```



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

