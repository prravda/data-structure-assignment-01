from typing import Optional


class Node:
    def __init__(
            self,
            data: int,
            link: Optional["Node"] = None
    ):
        self.data = data
        self.link = link
