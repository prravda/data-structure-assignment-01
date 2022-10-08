from unittest import TestCase
from linked_queue.linked_queue_impl import *
from linked_queue.tests.test_dataset import *


class TestEnqueueAndDisplay(TestCase):

    def test_display_after_enqueue(self):
        lq = LinkedQueue()

        for i in range(number_of_enqueue):
            lq.enqueue(i)

        self.assertEqual(lq.display(), list_till_number_of_enqueue)

