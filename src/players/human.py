# src/players/human.py
from players.player import Player

class HumanPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def make_move(self, piles):
        while True:
            try:
                pile_idx = int(input(f"{self.name}, choose a pile index: ")) - 1
                num_objects = int(input(f"{self.name}, choose the number of objects to take: "))
                if 0 <= pile_idx < len(piles) and 0 <= num_objects <= len(piles[pile_idx]):
                    if self.logger:
                        self.logger.info(f"{self.name} chooses pile {pile_idx} and takes {num_objects} objects.")
                    return pile_idx, num_objects
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
