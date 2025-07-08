import asyncio
import time
from abc import ABC, abstractmethod
from collections import defaultdict, Counter

class AbstractDict(ABC):
    @abstractmethod
    def int_dict(self, ids_list: list) -> dict:
        pass

    @abstractmethod
    def list_dict(self, *ids: int) -> dict:
        pass

class Async(AbstractDict):
    """
    Classe que implementa a interface AbstractDict para mapear inteiros e listas de inteiros.
    """
    @abstractmethod
    async def int_dict(ids_list: list) -> dict:
        mapped_ints = Counter(ids_list)  # Usando Counter para contar ocorrências
        await asyncio.sleep(5) # Simulando um processamento demorado
        print(f"Mapeamento de inteiros: {dict(mapped_ints)}")
        return dict(mapped_ints)

    @abstractmethod
    async def list_dict(*ids: int) -> dict:
        mapped_ints = defaultdict(list)
        for i in ids:
            mapped_ints[i].append(i)
        await asyncio.sleep(5) # Simulando um processamento demorado
        print(f"Mapeamento de lista de inteiros: {dict(mapped_ints)}")
        return dict(mapped_ints)

class Sync(AbstractDict):
    """
    Classe que implementa a interface AbstractDict para mapear inteiros e listas de inteiros.
    """
    @abstractmethod
    def int_dict(ids_list: list) -> dict:
        mapped_ints = Counter(ids_list)  # Usando Counter para contar ocorrências
        time.sleep(5) # Simulando um processamento demorado
        print(f"Mapeamento de inteiros: {dict(mapped_ints)}")
        return dict(mapped_ints)

    @abstractmethod
    def list_dict(*ids: int) -> dict:
        mapped_ints = defaultdict(list)
        for i in ids:
            mapped_ints[i].append(i)
        time.sleep(5) # Simulando um processamento demorado
        print(f"Mapeamento de lista de inteiros: {dict(mapped_ints)}")
        return dict(mapped_ints)

async def main(*args) -> None:
    await asyncio.gather(*args) # Executa as tarefas em paralelo

def run_async():
    numbers = [1, 1, 1, 3, 3, 2, 2, 4, 5, 5, 5, 5, 5]
    tasks = [
        Async.int_dict(numbers),
        Async.list_dict(*numbers)
    ]
    start = time.time()
    asyncio.run(main(*tasks))
    end = time.time()
    print(f"Tempo total da execução assíncrona: {end - start:.2f} segundos\n")

def run_sync():
    numbers = [1, 1, 1, 3, 3, 2, 2, 4, 5, 5, 5, 5, 5]
    start = time.time()
    Sync.int_dict(numbers)
    Sync.list_dict(*numbers)
    end = time.time()
    print(f"Tempo total de execução síncrona: {end - start:.2f} segundos\n")

if __name__ == "__main__":
    run_async()
    run_sync()
