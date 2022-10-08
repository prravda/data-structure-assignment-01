# Data structure - first assignment

written by 201603001 전인섭

# Description

## Project Structure

```
assignments
├── __init__.py
└── linked_queue
    ├── __init__.py
    ├── custom_exceptions <- custom exception 을 정의한 directory 입니다.
    │   ├── __init__.py
    │   └── queue_out_of_index_exception.py
    ├── linked_queue_adt.py <- abstract data type 을 정의 하였습니다.
    ├── linked_queue_impl.py <- abstract data type 을 기반으로 queue 를 구현하였습니다.
    ├── node.py <- linked structure 에 사용할 (singly) node를 구현하였습니다.
    └── tests <- python 의 내장 testing module unittest 를 통해 구현한 test 들 입니다.
        ├── __init__.py
        ├── test_dataset.py <- test 들에서 공통적으로 사용하는 dataset 입니다.
        ├── test_dequeue.py
        ├── test_enqueue_and_display.py
        └── test_peek.py
├── console_output.py <- 선생님께서 만드신 print 기반 test 입니다.
├── Dockerfile <- Dockerfile 입니다.
└── test.sh <- PYTHONPATH 설정, unittest 기반 test 및 console_output.py 실행
```

## Execution

### before getting started

- `assignment` directory 로 이동해주셔야 합니다.

### using python3 (python) directly

```bash
# set PYTHONPATH variable to this directory
export PYTHONPATH="${PYTHONPATH}:/"
# run test with unittest and console test which described in eclass
python3 -m unittest -v && python3 linked_queue/console_output.py
```

### using shell script

```bash
/bin/bash test.sh
```

### using DockerFile

```bash
# build a docker image
docker build -t data-structure-assignment-inseob .
# run container
docker run data-structure-assignment-inseob
```

---

# 0. Define problem

- Design, implement, and test `Queue` using singular linked list

---

# 1. Define ADT(Abstract Data Type) based on 0

```python
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
```

---

# 2. Code: implementation based on 1

```python
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
            raise QueueOutOfIndexException("Can not peek because the queue is empty")

        return self.__front.data

    def display(self) -> list[int]:
        elements = []
        front_most = self.__front

        while front_most is not self.__rear:
            elements.append(front_most.data)

        return elements
```

---

# 3. Test and dataset for test

## 0. test dataset

```python
# success scenario
number_of_enqueue = 10
number_of_successful_dequeue = 3

# fail scenario
number_of_dequeue_raise_exception = number_of_enqueue + 1

# common
list_till_number_of_enqueue = list(range(number_of_enqueue))
```

## 1. tests

### 0. test_dequeue

```python
from unittest import TestCase
from linked_queue.linked_queue_impl import *
from linked_queue.tests.test_dataset import *

class TestDequeue(TestCase):

    def test_linked_queue_dequeue_raise_exception(self):
        lq = LinkedQueue()

        self.assertRaises(QueueOutOfIndexException, lq.dequeue)

    def test_linked_queue_dequeue_raise_exception_after_enqueue(self):
        lq = LinkedQueue()

        for e in list_till_number_of_enqueue:
            lq.enqueue(e)

        with self.assertRaises(QueueOutOfIndexException):
            for _ in range(number_of_dequeue_raise_exception):
                lq.dequeue()

    def test_linked_queue_dequeue_success(self):
        lq = LinkedQueue()

        for e in list_till_number_of_enqueue:
            lq.enqueue(e)

        for e in list_till_number_of_enqueue:
            self.assertEqual(lq.dequeue(), e)
```

### 1. test_peek

```python
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
```

### 2. test_enqueue_and_display

```python
from unittest import TestCase
from linked_queue.linked_queue_impl import *
from linked_queue.tests.test_dataset import *

class TestEnqueueAndDisplay(TestCase):

    def test_display_after_enqueue(self):
        lq = LinkedQueue()

        for i in range(number_of_enqueue):
            lq.enqueue(i)

        self.assertEqual(lq.display(), list_till_number_of_enqueue)
```

---

# 4. Time complexity of each methods

## is_empty

- **time complexity:** `O(1)`
- **reason:** `front` 라는 property 가 `None` 인지 아닌지 1번만 연산하면 되기 때문이다.

## enqueue

- **time complexity:** `O(1)`
- **reason:**
    - 현재 queue 가 비었을 경우: front 와 rear 에 argument 로 받은 element 를 통해 만든 Node instance 를 할당하기만 하면 된다.
    - 현재 queue 가 비어있지 않을 경우: rear 의 다음 Node (memory address)를 의미하는 `rear.link` 에 element 를 통해 만든 Node instance 를 할당하고, `rear` 라는 property 에 rear.link 를 할당하기만 하면 된다.
    - 모든 경우의 time complexity 가 `O(1)` 이므로, 해당 method 의 time complexity 또한 `O(1)` 이다.

## dequeue

- **time complexity:** `O(1)`
- **reason:**
    - 현재 queue 가 비었을 경우: exception raising 만 해 주면 된다.
    - 현재 queue 가 비어있지 않을 경우: 변수를 하나 선언하여 가장 앞에 있는(frontmost) node 를 `front` property 를 통하여 접근해서 담고, 가장 앞에 있는 node 가 지워져야 하니 front property 를 `front.link` 로 재할당 해 준 뒤, Node 를 담아놓은 변수의 data property 를 반환하기만 하면 된다.
    - 모든 경우의 time complexity 가 `O(1)` 이므로, 해당 method 의 time complexity 또한 `O(1)` 이다.

## peek

- **time complexity:** `O(1)`
- **reason:**
    - 현재 queue 가 비었을 경우: exception raising 만 해 주면 된다.
    - 현재 queue 가 비어있지 않을 경우: 변수를 하나 선언하여 가장 앞에 있는(frontmost) node 를 `front` property 를 통하여 접근해서 담고, 가장 앞에 있는 node 가 지워져야 하니 front property 를 `front.link` 로 재할당 해 주기만 하면 된다.
    - 모든 경우의 time complexity 가 `O(1)` 이므로, 해당 method 의 time complexity 또한 `O(1)` 이다.

## display

- **time complexity:** `O(n)`
- **reason:** 가장 앞부터 시작하여 끝까지 탐색하는 과정이기에, element 의 갯수만큼 연산이 필요하여 O(n)의 time complexity 이다.