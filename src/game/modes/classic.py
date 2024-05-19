# src/game/modes/classic.py

from logging import Logger
import random
from collections import deque
from players.player import Player

class Classic:
    def __init__(self, num_piles: int = None) -> None:
        self.num_piles = random.randint(2, 4) if num_piles is None else num_piles
        self.piles = [deque(['#'] * random.randint(1, 2)) for _ in range(self.num_piles)]
        self.logger = None

    def set_logger(self, logger: Logger) -> None:
        self.logger = logger

    def get_piles(self) -> list[list[str]]:
        return [pile.copy() for pile in self.piles]

    def make_move(self, pile_idx: int, num_objects: int, player_name: str) -> None:
        pile = self.piles[pile_idx]
        if num_objects < 1 or num_objects > len(pile):
            raise ValueError(f"Invalid number of objects: {num_objects}")

        for _ in range(num_objects):
            pile.popleft()

        self.logger.info(f"{player_name} takes {num_objects} objects from pile {pile_idx + 1}. Remaining objects: {self.print_piles()}")

    def is_game_over(self) -> bool:
        return all(len(pile) == 0 for pile in self.piles)

    def print_piles(self) -> str:
        piles_str = []
        for i, pile in enumerate(self.piles, start=1):
            pile_str = f"Pile {i}: {''.join(pile)} ({len(pile)} objects)"
            piles_str.append(pile_str)
        return ", ".join(piles_str)

    def play(self, player1: Player, player2: Player) -> None:
        self.logger.info(f"Initial configuration: {self.print_piles()} ({self.num_piles} piles)")

        current_player = player1
        other_player = player2

        while not self.is_game_over():
            print(f"\nCurrent piles: {self.print_piles()}")
            pile_idx, num_objects = current_player.make_move(self.get_piles())
            self.make_move(pile_idx, num_objects, current_player.name)

            if self.is_game_over():
                break

            current_player, other_player = other_player, current_player

        if current_player == player1:
            self.logger.info(f"{player2.name} wins!")
            print(f"\n{player2.name} wins!")
        else:
            self.logger.info(f"{player1.name} wins!")
            print(f"\n{player1.name} wins!")
