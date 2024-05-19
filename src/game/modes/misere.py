# src/game/modes/classic.py

from game.modes.mode import GameMode

class MisereMode(GameMode):
    def get_winner(self, current, other):
        if self.is_game_over():
            winner = other
        return winner
    
    def evaluate_state(self, piles: list[list[str]]) -> float:
        total_objects = sum(len(pile) for pile in piles)
        num_non_empty_piles = len([pile for pile in piles if pile])
        if total_objects <= 1:
            # If there is only one object left, the player who takes it loses
            return -float('inf') if total_objects == 1 else float('inf')
        return num_non_empty_piles - total_objects
