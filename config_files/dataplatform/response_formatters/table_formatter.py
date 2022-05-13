import json
from pathlib import Path

from jinja2 import Template

from .abstract_formatter import ResponseFormatter
from .handlebars_formatter import HTMLFormattedData


class TableResponseFormatter(ResponseFormatter):
    def __init__(self):
        self._template = self._load_template()

    @staticmethod
    def _load_template() -> Template:
        template_file = Path(__file__).parent.joinpath("table_template.html").resolve()
        with open(template_file, encoding="utf-8") as file:
            template = Template(file.read())
        return template

    def format(self, data: str) -> HTMLFormattedData:
        extracted_data = self._extract_data(data)
        return HTMLFormattedData(self._template.render(data_structure=extracted_data))

    @staticmethod
    def _extract_data(raw_data: str) -> dict:
        return json.loads(raw_data)
