from abc import ABC, abstractmethod


class FormattedData(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_display_data(self) -> dict:
        pass


class ResponseFormatter(ABC):
    @abstractmethod
    def format(self, data: str) -> FormattedData:
        pass
