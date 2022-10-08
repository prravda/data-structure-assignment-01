from linked_queue.linked_queue_impl import *


def driver_code():
    queue = LinkedQueue()
    numer_of_enqueue = 10

    for i in range(numer_of_enqueue):
        queue.enqueue(i)

    print(f'after {numer_of_enqueue} enqueue: {queue.display()}')

    print('\n\tdequeue:', queue.dequeue())
    print('\tdequeue:', queue.dequeue())
    print('\tdequeue:', queue.dequeue())

    print('\nafter 3 dequeue:', queue.display())

    hero_list = ('superman', 'batman', 'wonder_woman', 'aquaman')

    for hero in hero_list:
        queue.enqueue(hero)

    print(f'\nafter {len(hero_list)} enqueue:', queue.display())

    print('\n\tdequeue:', queue.dequeue())

    print('\nafter 1 dequeue:', queue.display())

    print('\n\tpeek:', queue.peek())


driver_code()