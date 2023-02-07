from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    word_search = list()
    data = instance.data

    for file in data:
        found_word = ()
        for i, line in enumerate(file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                found_word = (file['nome_do_arquivo'], i)
                found_word.append({"linha": i + 1})
        if len(found_word) > 0:
            word_search.append(
                {"palavra": word,
                 "arquivo": file["nome_do_arquivo"],
                 "ocorrencias": found_word})
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
