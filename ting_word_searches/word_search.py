from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
    word_search = list()
    data = instance.data
    word_lower = word.lower()

    for file in data:
        found_word = []
    
        for i, line in enumerate(file['linhas_do_arquivo']):
            if word_lower in line.lower():
                found_word = (file['nome_do_arquivo'], i)
                found_word = found_word + ({"linha": i + 1})
        if len(found_word) > 0:
            word_search = word_search + (
                {"palavra": word,
                 "arquivo": file["nome_do_arquivo"],
                 "ocorrencias": found_word})
    print(word_search)
    return word_search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
