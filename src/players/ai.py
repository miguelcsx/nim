# src/players/ai.py

from functools import cache
from collections import deque
from copy import deepcopy

class AIPlayer:
    def __init__(self, name, use_alpha_beta=False):
        self.name = name
        self.use_alpha_beta = use_alpha_beta
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger

    def make_move(self, piles):
        if self.use_alpha_beta:
            self.logger.info(f"{self.name} uses minimax with alpha-beta pruning.")
            best_score, best_move = self.minimax_alpha_beta(tuple(map(tuple, piles)), True, float('-inf'), float('inf'))
        else:
            self.logger.info(f"{self.name} uses minimax without alpha-beta pruning.")
            best_score, best_move = self.minimax(tuple(map(tuple, piles)), True)
        pile_idx, num_objects = best_move
        if best_move is not None:
            if self.logger:
                self.logger.info(f"{self.name} chooses pile {pile_idx} and takes {num_objects} objects.")
            print(f"\n{self.name} (AI) takes {num_objects} objects from pile {pile_idx + 1}.")
        return best_move

    def evaluate_state(self, piles):
        total_objects = sum(len(pile) for pile in piles)
        num_non_empty_piles = len([pile for pile in piles if pile])
        return -(total_objects + num_non_empty_piles)
    
    @cache
    def minimax(self, piles, is_maximizing):
        # Base case: Check if the game is over
        if all(len(pile) == 0 for pile in piles):
            # Return score and and None for end state
            return (self.evaluate_state(piles), None)

        # Recursive case: Explore all possible moves
        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for pile_idx in range(len(piles)):
            if len(piles[pile_idx]) > 0:  # Check if pile is not empty
                for num_objects in range(1, len(piles[pile_idx]) + 1):
                    # Simulate the move
                    simulated_piles = list(map(deque, piles))
                    for _ in range(num_objects):
                        simulated_piles[pile_idx].popleft()
                    simulated_piles = tuple(map(tuple, simulated_piles))

                    # Get the score for the opponent (minimizing player)
                    score = self.evaluate_state(simulated_piles)

                    # Update best move based on maximizing or minimizing player
                    if is_maximizing and score > best_score:
                        best_score = score
                        best_move = (pile_idx, num_objects)
                    elif not is_maximizing and score < best_score:
                        best_score = score
                        best_move = (pile_idx, num_objects)
                    else:
                        # If scores are equal, explore further
                        next_score, _ = self.minimax(simulated_piles, not is_maximizing)
                        if is_maximizing and next_score > best_score:
                            best_score = next_score
                            best_move = (pile_idx, num_objects)
                        elif not is_maximizing and next_score < best_score:
                            best_score = next_score
                            best_move = (pile_idx, num_objects)

        return best_score, best_move

    @cache
    def minimax_alpha_beta(self, piles, is_maximizing, alpha, beta):
        # Base case: Check if the game is over
        if all(len(pile) == 0 for pile in piles):
            # Return score and and None for end state
            return (self.evaluate_state(piles), None)
        
        # Recursive case: Explore all possible moves
        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for pile_idx in range(len(piles)):
                if len(piles[pile_idx]) > 0:  # Check if pile is not empty
                    for num_objects in range(1, len(piles[pile_idx]) + 1):
                        # Simulate the move
                        simulated_piles = list(map(deque, piles))
                        for _ in range(num_objects):
                            simulated_piles[pile_idx].popleft()
                        simulated_piles = tuple(map(tuple, simulated_piles))

                        # Get the score for the opponent (minimizing player)
                        score, _ = self.minimax_alpha_beta(simulated_piles, False, alpha, beta)

                        if score > best_score:
                            best_score = score
                            best_move = (pile_idx, num_objects)

                        # Alpha-beta pruning
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score, best_move

        best_score = float('inf')
        best_move = None
        for pile_idx in range(len(piles)):
            if len(piles[pile_idx]) > 0:    # Check if pile is not empty
                for num_objects in range(1, len(piles[pile_idx]) + 1):
                    # Simulate the move
                    simulated_piles = list(map(deque, piles))
                    for _ in range(num_objects):
                        simulated_piles[pile_idx].popleft()
                    simulated_piles = tuple(map(tuple, simulated_piles))

                    # Get the score for the opponent (maximizing player)
                    score, _ = self.minimax_alpha_beta(simulated_piles, True, alpha, beta)

                    if score < best_score:
                        best_score = score
                        best_move = (pile_idx, num_objects)

                    # Alpha-beta pruning
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score, best_move
