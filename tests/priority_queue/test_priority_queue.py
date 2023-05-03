from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():

    test_queue = PriorityQueue()

    test_queue.dequeue({"qtd_linhas": 5})
    test_queue.enqueue({"qtd_linhas": 3})
    assert len(test_queue) == 2
    assert test_queue.search(0) == {"qtd_linhas": 3}

    test_queue.dequeue()
    assert len(test_queue) == 1

    with pytest.raises(IndexError):
        test_queue.search(10)

    # """Aqui irá sua implementação"""
