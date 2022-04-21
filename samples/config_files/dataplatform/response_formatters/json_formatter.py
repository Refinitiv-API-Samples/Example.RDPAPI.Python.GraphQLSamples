import json

from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.data import JsonLexer

from .abstract_formatter import ResponseFormatter, FormattedData


class JSONFormattedData(FormattedData):
    def __init__(self, data_string: str):
        self._data_string = data_string

    def display(self):
        print(self._data_string)


class JSONResponseFormatter(ResponseFormatter):
    def __init__(self, indent: int = 4):
        self._indent = indent

    def format(self, data: str) -> JSONFormattedData:
        formatter_string = json.dumps(json.loads(data), indent=self._indent)
        return JSONFormattedData(highlight(formatter_string, JsonLexer(), TerminalFormatter()))