# import os
from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []
    for index in range(len(instance)):
        test = instance.search(index)
        list = {
            "palavra": word,
            "arquivo": test["nome_do_arquivo"],
            "ocorrencias": []
        }
        for index2, text in enumerate(test["linhas_do_arquivo"]):
            if word.casefold() in text.casefold():
                list["ocorrencias"].append({"linha": index2 + 1})
        if len(list["ocorrencias"]):
            result.append(
                list["palavra"],
                list["arquivo"],
                list["ocorrencias"])
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
