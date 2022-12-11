from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class StorageClient:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def create_snapshot(self, data: list) -> None:
        result = self._strategy.create_snapshot(data)
        return result


class Strategy(ABC):
    @abstractmethod
    def create_snapshot(self, data: List):
        pass
