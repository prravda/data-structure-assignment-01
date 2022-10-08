from linked_queue.node import Node
from abc import ABC, abstractmethod
from typing import Optional


class LinkedQueue(ABC):
    @abstractmethod
    def __init__(self):
        self.__front: Optional[Node] = None
        self.__rear: Optional[Node] = None

    @abstractmethod
    def is_empty(self) -> bool:
        # should return current whether queue is empty or not
        pass

    @abstractmethod
    def enqueue(self, element: int) -> None:
        # should add an element making a Node instance
        # into the back-most of storage of this queue
        pass

    @abstractmethod
    def dequeue(self) -> Optional[int]:
        # should return the front-most node's data property
        # with removing the element from the storage of this queue
        pass

    @abstractmethod
    def peek(self) -> Optional[int]:
        # should return the front-most node's data property
        # without manipulating any element
        pass

    @abstractmethod
    def display(self) -> list[int]:
        # should return a list of integer
        # with extracting the data property from each Node instance
        # from the front-most Node to back-most Node
        pass

