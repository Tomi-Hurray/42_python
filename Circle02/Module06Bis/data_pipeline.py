import json
import typing
from abc import ABC, abstractmethod
from typing import Any, Protocol


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
                formatted = f"{item['log_level']}: {item['log_message']}"
                self._data.append((self._current_rank, formatted))
                self._current_rank += 1
        else:
            formatted = f"{data['log_level']}: {data['log_message']}"
            self._data.append((self._current_rank, formatted))
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


# export plugins

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        print("JSON Output:")
        out_dict = {f"item_{rank}": value for rank, value in data}
        print(json.dumps(out_dict))


# datastream

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError("Only DataProcessor instances can be registered")
        if proc not in self._processors:
            self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in\
                      stream: {element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    extracted_data.append(proc.output())
                except IndexError:
                    break
            if extracted_data:
                plugin.process_output(extracted_data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            proc_name = proc.__class__.__name__.replace("Processor",
                                                        " Processor")
            print(
                f"{proc_name}: total {proc._current_rank} items processed, "
                f"remaining {len(proc._data)} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream_handler = DataStream()
    stream_handler.print_processors_stats()

    print("Registering Processors")
    stream_handler.register_processor(NumericProcessor())
    stream_handler.register_processor(TextProcessor())
    stream_handler.register_processor(LogProcessor())

    batch_1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh "
             "instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch_1}")
    stream_handler.process_stream(batch_1)
    stream_handler.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream_handler.output_pipeline(3, csv_plugin)
    stream_handler.print_processors_stats()

    batch_2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires in "
             "10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {batch_2}")
    stream_handler.process_stream(batch_2)
    stream_handler.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream_handler.output_pipeline(5, json_plugin)
    stream_handler.print_processors_stats()
