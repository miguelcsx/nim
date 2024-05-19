# scr/players/player.py

from abc import ABC, abstractmethod
from logging import Logger

class Player(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.logger = None

    def set_logger(self, logger: Logger) -> None:
        self.logger = logger

    @abstractmethod
    def make_move(self, piles: list[list[str]]) -> tuple[int, int]:
        pass
