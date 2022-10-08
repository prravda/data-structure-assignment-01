from typing import Optional
from linked_queue.linked_queue_adt import LinkedQueue, Node
from linked_queue.custom_exceptions.queue_out_of_index_exception import QueueOutOfIndexException


class LinkedQueue(LinkedQueue):
    def __init__(self):
        self.__front: Optional[Node] = None
        self.__rear: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.__front is None

    def enqueue(self, element: int) -> None:
        node_to_enqueue = Node(element)

        if self.is_empty():
            self.__front = self.__rear = node_to_enqueue
            return None

        self.__rear.link = node_to_enqueue
        self.__rear = self.__rear.link

    def dequeue(self) -> int:
        if self.is_empty():
            raise QueueOutOfIndexException("Can not dequeue because the queue is empty")

        node_to_dequeue = self.__front
        self.__front = self.__front.link

        return node_to_dequeue.data

    def peek(self) -> Optional[int]:
        if self.is_empty():
            raise QueueOutOfIndexException("Can not dequeue because the queue is empty")

        return self.__front.data

    def display(self) -> list[int]:
        elements = []
        front_most = self.__front

        while front_most is not None:
            elements.append(front_most.data)
            front_most = front_most.link

        return elements

