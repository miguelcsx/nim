# src/game/modes/classic.property

from game.modes.mode import GameMode

class ClassicMode(GameMode):
    def get_winner(self, current, other):
        if self.is_game_over():
            winner = current
        return winner
    
    def evaluate_state(self, piles: list[list[str]]) -> float:
        total_objects = sum(len(pile) for pile in piles)
        # If there are any piles with 1 object, the AI loses on the next turn. Assign a very low value to this state
        if any(len(pile) == 1 for pile in piles):
            return -float('inf')
        # If the total number of objects is even, the next move belongs to another player. Assign a high value to this state for the AI  
        return float('inf') if total_objects % 2 == 0 else -float('inf')
