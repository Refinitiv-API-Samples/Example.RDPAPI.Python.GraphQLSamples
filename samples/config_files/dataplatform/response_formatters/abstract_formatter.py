from abc import ABC, abstractmethod


class FormattedData(ABC):
    @abstractmethod
    def display(self):
        pass


class ResponseFormatter(ABC):
    @abstractmethod
    def format(self, data: str) -> FormattedData:
        pass
