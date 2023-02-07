import sys
import pathlib


def txt_importer(path_file):
    if pathlib.Path(path_file).suffix != '.txt':
        return sys.stderr.write(f"{'Formato inválido'}")
    try:
        with open(path_file, "r") as arquivo:
            txt_list = arquivo.read().split("\n")
            return txt_list
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
