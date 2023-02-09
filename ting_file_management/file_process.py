from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    # dict = {}
    lista = txt_importer(path_file)
    for i in range(instance.__len__()):
        dict = instance.search(i)
        if dict["nome_do_arquivo"] == path_file:
            return

    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lista),
        "linhas_do_arquivo": lista,
    }

    instance.enqueue(dict)
    sys.stdout.write(str(dict))
    # print(dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) <= 0:
        return print('Não há elementos')

    delet = instance.dequeue()
    file = delet["nome_do_arquivo"]
    print(f'Arquivo {file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    test = instance.search(position)
    try:
        print(test)
    except IndexError:
        print("Posição inválida")
