# src/game/modes/classic.py

import random
from collections import deque

class Classic:
    def __init__(self, num_piles=None):
        self.num_piles = random.randint(2, 4) if num_piles is None else num_piles
        self.piles = [deque(['#'] * random.randint(1, 3)) for _ in range(self.num_piles)]
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger

    def get_piles(self):
        return [pile.copy() for pile in self.piles]

    def make_move(self, pile_idx, num_objects, player_name):
        pile = self.piles[pile_idx]
        if num_objects < 1 or num_objects > len(pile):
            raise ValueError(f"Invalid number of objects: {num_objects}")

        for _ in range(num_objects):
            pile.popleft()

        self.logger.info(f"{player_name} takes {num_objects} objects from pile {pile_idx + 1}. Remaining objects: {self.print_piles()}")

    def is_game_over(self):
        return all(len(pile) == 0 for pile in self.piles)

    def print_piles(self):
        piles_str = []
        for i, pile in enumerate(self.piles, start=1):
            pile_str = f"Pile {i}: {''.join(pile)} ({len(pile)} objects)"
            piles_str.append(pile_str)
        return ", ".join(piles_str)

    def play(self, player1, player2):
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
