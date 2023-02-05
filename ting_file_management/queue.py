from ting_file_management.abstract_queue import AbstractQueue
# import threading, queue
# fila = queue.Queue()


class Queue(AbstractQueue):

    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError('erro em dequene')
        return self.queue.pop(0)

    def search(self, index):
        if not 0 <= index < len(self.queue):
            raise IndexError('não foi encontrado')
        return self.queue[index]
