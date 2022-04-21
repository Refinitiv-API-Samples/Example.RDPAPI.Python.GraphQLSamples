# pylint: disable=import-error
from .response_formatters.abstract_formatter import FormattedData
from .response_formatters.json_formatter import JSONResponseFormatter


def display_output(data: str):
    _format_data(data).display()


def _format_data(data: str) -> FormattedData:
    return JSONResponseFormatter().format(data)
