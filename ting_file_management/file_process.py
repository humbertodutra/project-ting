import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file),
        'linhas_do_arquivo': file
    }
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    instance.enqueue(result)
    sys.stdout.write(f'{result}')


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        sys.stdout.write('Não há elementos\n')
        return None
    remove_file = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(f'Arquivo {remove_file} removido com sucesso\n')


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        search = instance.search(position)
        sys.stdout.write(f'{search}')
    except IndexError:
        sys.stderr.write('Posição inválida')
