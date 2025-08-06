# Interface esperada pelo sistema
class FileReader:
    def read(self) -> str:
        pass


# Classe de terceiros que trabalha com leitura em bytes
class BinaryFileReader:
    def read_bytes(self) -> bytes:
        return b"Dados binarios lidos de um arquivo"


# Código cliente que espera um FileReader
def process_file(reader: FileReader):
    content = reader.read()
    print("Conteúdo do arquivo:", content)


# Tentativa de uso com BinaryFileReader (incompatível)
binary_reader = BinaryFileReader()

# Isso não funciona:
# process_file(binary_reader)
