from unittest import TestCase
from linked_queue.linked_queue_impl import *
from linked_queue.tests.test_dataset import *


class TestDequeue(TestCase):

    def test_linked_queue_peek_raise_exception(self):
        lq = LinkedQueue()

        self.assertRaises(QueueOutOfIndexException, lq.peek)

    def test_linked_queue_peek_raise_exception_after_enqueue(self):
        lq = LinkedQueue()

        for e in list_till_number_of_enqueue:
            lq.enqueue(e)

        with self.assertRaises(QueueOutOfIndexException):
            for _ in range(number_of_enqueue):
                lq.dequeue()

            lq.peek()

    def test_linked_queue_peek_success(self):
        lq = LinkedQueue()

        for e in list_till_number_of_enqueue:
            lq.enqueue(e)

        for e in list_till_number_of_enqueue:
            self.assertEqual(lq.peek(), e)
            lq.dequeue()
