import json

import pybars  # noqa
from IPython.core.display import display, HTML

from .abstract_formatter import ResponseFormatter, FormattedData


class HTMLFormattedData(FormattedData):
    def __init__(self, formatted_data: str):
        self._formatted_data = formatted_data

    def display(self):
        display(HTML(self._formatted_data))

    def get_display_data(self) -> dict:
        return {
            "text/html": [self._formatted_data],
            "text/plain": [self._formatted_data],
        }


class HandlebarsResponseFormatter(ResponseFormatter):
    def __init__(self, template_str: str):
        compiler = pybars.Compiler()
        precompile = compiler.precompile(template_str)
        self._template = compiler.template(precompile)

    def format(self, data: str) -> HTMLFormattedData:
        html_str = self._template(json.loads(data))
        return HTMLFormattedData(html_str)
