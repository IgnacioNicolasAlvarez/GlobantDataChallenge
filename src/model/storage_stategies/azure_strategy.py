from typing import List

from src.client.storage import Strategy


class AzureBlobStorageStrategy(Strategy):
    def create_snapshot(self, data: List) -> List:
        return reversed(sorted(data))
