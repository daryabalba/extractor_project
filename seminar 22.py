from typing import Iterable, Union, Sized


class Stack():
    """
    class realising a stack in python
    """
    def __init__(self, elements=None):
        if elements:
            if isinstance(elements, list) or isinstance(elements, tuple):
                self.elements = elements
            else:
                self.elements = [elements]
        else:
            self.elements = []

    def get_in(self, element):
        if isinstance(element, list) or isinstance(element, tuple):
            self.elements.extend(element)
        else:
            self.elements.append(element)

    def get_out_del(self):
        if self.elements:
            return self.elements.pop()
        print('stack is empty. please add some elements to call this function')
        return None

    def get_out_look(self):
        if not self.elements:
            return None
        return self.elements[-1]

    def get_size(self):
        return len(self.elements)

    def get_all(self):
        return self.elements


# stack_example = Stack()
# stack_example.get_in([1, 2, 3])
# stack_example.get_in(4)
# size = stack_example.get_size()
#
# for element in range(size+1):
#     print(stack_example.get_out())

skobki = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def check_correct(input_el):
    new_stack = Stack()
    for element in input_el:
        if element not in skobki:
            new_stack.get_in(element)
        else:
            if new_stack.get_size() == 0:
                new_stack.get_in(element)
            else:
                pair = skobki.get(element)
                if new_stack.get_out_look() == pair:
                    new_stack.get_out_del()
                else:
                    return False
    if new_stack.get_size():
        return False
    return True
input_el = Stack([1, 5, 6, 2, 8])

def get_sorted(stack=Stack):
    tmp_stack = Stack(stack.get_out_del())

    while stack.get_size():
        last = tmp_stack.get_out_look()
        new_element = stack.get_out_del()
        if new_element > last:
            tmp_stack.get_in(new_element)
        else:
            ender = []
            while new_element < last:
                # if not tmp_stack.get_size():
                #     res = [new_element] + ender
                #     tmp_stack.get_in(res)
                #     continue
                # else:
                last = tmp_stack.get_out_del()
                ender.append(last)
                if tmp_stack.get_size():
                    last = tmp_stack.get_out_look()
                else:
                    res = [new_element] + ender
                    tmp_stack.get_in(res)
                    continue
            res = [new_element] + ender
            tmp_stack.get_in(res)

    return tmp_stack.get_all()


class FullQueueError(BaseException):
    """
    Raises error when queue is full
    """


class Queue:
    def __init__(self, elements: Iterable | None = None, capacity: int or None = None):
        self.elements = list(elements) if elements else []
        self._capacity = capacity

    def put(self, element: object):
        if self.full():
            raise FullQueueError
        self.elements.append(element)

    def put_iterable(self, sequence: Union[Iterable, Sized]):
        if self.capacity() and self.size() + len(sequence) > self.capacity():
            raise FullQueueError
        self.elements.extend(sequence)

    def get(self):
        return self.elements.pop(0) if self.size() else None

    def size(self):
        return len(self.elements)

    def top(self):
        return self.elements[0] if self.size() else None

    def capacity(self):
        return self._capacity

    def full(self):
        return True if self._capacity == self.size() else False


# queue = Queue(capacity=5)
# queue.put(12)
# queue.put([1, 2, 3])
# print(queue.full())
# queue.put(4)


def sober(sequence_1, sequence_2):
    steps = 0
    queue_one = Queue()
    queue_one.put_iterable(sequence_1)
    queue_two = Queue()
    queue_two.put_iterable(sequence_2)
    while queue_one.size() and queue_two.size():
        top_one = queue_one.get()
        top_two = queue_two.get()
        if top_one == 0 and top_two == 9:
            queue_one.put(top_one)
            queue_one.put(top_two)
        elif top_two == 0 and top_one == 9:
            queue_two.put(top_two)
            queue_two.put(top_one)
        elif top_one > top_two:
            queue_one.put(top_one)
            queue_one.put(top_two)
        else:
            queue_two.put(top_two)
            queue_two.put(top_one)
        steps += 1
        if steps == 10 ** 6:
            print('botva')
            return
    if queue_one.size():
        print(f'First {steps}')
        return
    else:
        print(f'Second {steps}')
        return

from src.services import
seq1 = [1, 4, 5, 8, 9]
seq2 = [2, 3, 6, 7, 0]
sober(seq1, seq2)
