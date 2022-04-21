import json
from pathlib import Path

from IPython.core.display import display, HTML
from jinja2 import Template

from .abstract_formatter import ResponseFormatter, FormattedData


class TableFormattedData(FormattedData):
    def __init__(self, formatted_data: HTML):
        self._formatted_data = formatted_data

    def display(self):
        display(self._formatted_data)


class TableResponseFormatter(ResponseFormatter):
    def __init__(self):
        self._template = self._load_template()

    @staticmethod
    def _load_template() -> Template:
        template_file = Path(__file__).parent.joinpath("table_template.html").resolve()
        with open(template_file, encoding="utf-8") as file:
            template = Template(file.read())
        return template

    def format(self, data: str) -> TableFormattedData:
        extracted_data = self._extract_data(data)
        return TableFormattedData(HTML(self._template.render(data_structure=extracted_data)))

    @staticmethod
    def _extract_data(raw_data: str) -> dict:
        return json.loads(raw_data)
