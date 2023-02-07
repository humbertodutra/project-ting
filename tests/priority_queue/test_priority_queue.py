from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    p_queue = PriorityQueue()
    p_queue.priority_limit = 3

    p_queue.enqueue({'nome_do_arquivo': 'arquivo1.txt',
                    'qtd_linhas': 2,
                     'linhas_do_arquivo': ['linha1', 'linha2']})
    p_queue.enqueue({'nome_do_arquivo': 'arquivo2.txt', 'qtd_linhas': 4,
                    'linhas_do_arquivo': ['linha1', 'linha2', 'linha3',
                                          'linha4']})
    p_queue.enqueue({'nome_do_arquivo': 'arquivo3.txt',
                    'qtd_linhas': 1, 'linhas_do_arquivo': ['linha1']})

    assert len(p_queue.high_priority) == 1
    assert len(p_queue.regular_priority) == 2
