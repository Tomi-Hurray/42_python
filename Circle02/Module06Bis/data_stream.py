from abc import ABC, abstractmethod
import typing
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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Registers a DataProcessor instance"""
        if not isinstance(proc, DataProcessor):
            raise TypeError("Only DataProcessor instances can be registered")
        if proc not in self._processors:
            self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Routes each element in the stream to the first matching"""
        for element in stream:
            handled = False
            for proc in self._processors:
                # Polymorphic validation and ingestion
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element in stream:\
                     {element}"
                )

    def print_processors_stats(self) -> None:
        """Prints total processed and remaining items for each registered"""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            proc_name = proc.__class__.__name__.replace("Processor",
                                                        " Processor")
            total_processed = proc._current_rank
            remaining = len(proc._data)
            print(
                f"{proc_name}: total {total_processed} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")

    # 1. Initialize DataStream and check empty statistics
    print("Initialize DataStream...")
    stream_handler = DataStream()
    stream_handler.print_processors_stats()

    # 2. Create and register only the NumericProcessor initially
    print("\nRegistering Numeric Processor...")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    stream_handler.register_processor(num_proc)

    # Mixed data batch containing valid numbers, text, logs, and invalid types
    batch_1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch_1}")
    stream_handler.process_stream(batch_1)
    stream_handler.print_processors_stats()

    # 3. Register the remaining processors and re-send the batch
    print("\nRegistering other data processors")
    stream_handler.register_processor(txt_proc)
    stream_handler.register_processor(log_proc)

    print("Send the same batch again")
    stream_handler.process_stream(batch_1)
    stream_handler.print_processors_stats()

    # 4. Test unprocessable elements even when all processors are registered
    print("\nSending batch with unsupported types (boolean, empty dict, "
          "mixed list)...")
    invalid_batch: list[Any] = [True, {}, [1, "mixed"]]
    stream_handler.process_stream(invalid_batch)

    # 5. Consume elements from the processors and show updated statistics
    print("\nConsume some elements from the data processors: Numeric 3, "
          "Text 2, Log 1")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Consumed Numeric [{rank}]: {val}")

    for _ in range(2):
        rank, val = txt_proc.output()
        print(f"Consumed Text [{rank}]: {val}")

    for _ in range(1):
        rank, val = log_proc.output()
        print(f"Consumed Log [{rank}]: {val}")

    print()
    stream_handler.print_processors_stats()
