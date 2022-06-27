from .response_formatters.abstract_formatter import ResponseFormatter
from .response_formatters.chart_formatter import (
    ChartResponseFormatter,
    DataSeriesExtractor,
    TitleExtractor,
)
from .response_formatters.handlebars_formatter import HandlebarsResponseFormatter
from .response_formatters.json_formatter import JSONResponseFormatter
from .response_formatters.table_formatter import TableResponseFormatter


def display_output(data: str, formatter: ResponseFormatter):
    formatted_data = formatter.format(data)
    formatted_data.display()


class NoTemplateException(Exception):
    pass


class FormatterSelector:
    def __init__(self, handlebars_template: str = ""):
        self._handlebars_template = handlebars_template

    def get_formatter(self, format_: str = "json") -> ResponseFormatter:
        formatters = {
            "json": JSONResponseFormatter,
            "table": TableResponseFormatter,
            "handlebars": self._get_handlebars_formatter,
            "chart": self._get_chart_formatter,
        }
        return formatters[format_]()

    def _get_handlebars_formatter(self):
        if not self._handlebars_template:
            raise NoTemplateException("No template provided for handlebars.")
        return HandlebarsResponseFormatter(self._handlebars_template)

    @staticmethod
    def _get_chart_formatter():
        return ChartResponseFormatter(DataSeriesExtractor(), TitleExtractor("LongTitle"))
