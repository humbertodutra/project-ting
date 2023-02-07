import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                contents = file.read()
                data = contents.split("\n")
                print(contents)
                return data
        except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        print("Formato inválido", file=sys.stderr)
