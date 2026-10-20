from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._current_rank: int = 0

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data stored to output")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def ingest(self, data: int | float | list[int] | list[float] |
               list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._data.append((self._current_rank, str(data)))
            self._current_rank += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False


class TextProcessor(DataProcessor):
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._data.append((self._current_rank, str(data)))
            self._current_rank += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, str) and not isinstance(x, bool)
                for x in data
            )
        return False


class LogProcessor(DataProcessor):
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._current_rank, str(item)))
                self._current_rank += 1
        else:
            self._data.append((self._current_rank, str(data)))
            self._current_rank += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and len(data) > 0:
            return all(
                isinstance(x, str) and isinstance(y, str)
                for x, y in data.items()
            )
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, dict)
                and len(item) > 0
                and all(isinstance(x, str) and isinstance(y, str)
                        for x, y in item.items())
                for item in data
            )
        return False


if __name__ == "__main__":
    a = 67
    b = "Hello"
    c = [1, 2, 3, 4, 5]
    d = ["Hello", "Nexus", "World"]
    e = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print("=== Code Nexus - Data Processor ===\n")

    """numeric processor"""

    print("Testing Numeric processor...")
    numproc = NumericProcessor()
    print(f"Trying to validate input '{a}': {numproc.validate(a)}")
    print(f"Trying to validate input '{b}': {numproc.validate(b)}")
    #   numproc.ingest(a)
    #   numproc.output()
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numproc.ingest("foo")
    except ValueError as x:
        print(f"Got exception: {x}")
    print(f"Processing data: {c}")
    numproc.ingest(c)
    #   numproc.output()
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = numproc.output()
        print(f"Numeric value {rank}: {val}")

    """text processsor"""

    print("\nTesting Text processor...")
    txtproc = TextProcessor()
    print(f"Trying to validate input '{a}': {txtproc.validate(a)}")
    print(f"Trying to validate input '{d}': {txtproc.validate(b)}")
    print(f"Processing data: {d}")
    txtproc.ingest(d)
    #  txtproc.output()
    print("Extracting 1 value...")
    for _ in range(1):
        rank, val = txtproc.output()
        print(f"Text value {rank}: {val}")

    """log precoessor"""

    print("\nTesting Log processor...")
    logproc = LogProcessor()
    print(f"Trying to validate input '{b}': {logproc.validate(a)}")
    print(f"Trying to validate input '{d}': {logproc.validate(b)}")
    print(f"Processing data: {e}")
    logproc.ingest(e)
    #   logproc.output()
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = logproc.output()
        print(f"Log entry {rank}: {val}")
