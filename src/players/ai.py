# src/players/ai.py

from functools import cache
from utils.tree import TreeNode

class AIPlayer:
    def __init__(self, name):
        self.name = name
        self.logger = None

    def set_logger(self, logger):
        self.logger = logger
