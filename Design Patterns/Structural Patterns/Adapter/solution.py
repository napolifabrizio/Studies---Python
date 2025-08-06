# Interface esperada pelo sistema
class FileReader:
    def read(self) -> str:
        pass


# Classe de terceiros que trabalha com leitura em bytes
class BinaryFileReader:
    def read_bytes(self) -> bytes:
        binary_text = b"Dados binarios lidos de um arquivo"
        return ' '.join(format(byte, '08b') for byte in binary_text)


# Código cliente que espera um FileReader
def process_file(reader: FileReader) -> None:
    content = reader.read()
    print("Conteúdo do arquivo:", content)


# Adapter com composição
class AdapterBinaryToFile(FileReader):
    def __init__(self, binary_reader: BinaryFileReader):
        self.binary_reader = binary_reader

    def read(self):
        binary_data = self.binary_reader.read_bytes()
        return self.from_binary(binary_data)

    def from_binary(self, binary_str: str) -> str:
        bytes_list = [int(b, 2) for b in binary_str.split()]
        return bytes(bytes_list).decode()

binary_reader = BinaryFileReader()
adapter = AdapterBinaryToFile(binary_reader)

process_file(adapter)