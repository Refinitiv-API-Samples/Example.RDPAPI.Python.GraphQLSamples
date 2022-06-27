import base64
import json
from io import BytesIO
from pathlib import Path
from typing import Union

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy import ndarray
from pandas import DataFrame

from .dataseries import DataSeriesExtractor
from .titles import TitleExtractor
from ..abstract_formatter import FormattedData, ResponseFormatter


class ChartFormattedData(FormattedData):
    def __init__(self, dataframe: DataFrame):
        self._dataframe = dataframe

    def display(self):
        self._create_plot()

    def get_display_data(self) -> dict:
        return {
            "text/plain": [str(type(self._create_plot()))],
            "image/png": self._get_base64_png(),
        }

    def _create_plot(self):
        return self._dataframe.plot(subplots=True, figsize=(12, 10))

    def _get_base64_png(self) -> str:
        temp_file = "temp.png"
        self._get_figure(self._create_plot()).savefig(temp_file)
        with Path(temp_file).open("rb") as png_file, BytesIO() as base64_stream:
            base64.encode(png_file, base64_stream)
            base64_text = base64_stream.getvalue().decode("utf-8")
        Path(temp_file).unlink()
        return base64_text

    @staticmethod
    def _get_figure(plot: Union[Axes, ndarray]) -> Figure:
        return plot.figure if isinstance(plot, Axes) else plot[0].figure


class ChartResponseFormatter(ResponseFormatter):
    def __init__(self, series_extractor: DataSeriesExtractor, title_extractor: TitleExtractor):
        self._title_extractor = title_extractor
        self._series_extractor = series_extractor

    def format(self, data: str) -> FormattedData:
        pd_data = DataFrame.from_dict(json.loads(data)["data"])
        chart_data = {}
        for item in pd_data[pd_data.columns[0]]:
            series = self._series_extractor.extract_series(item, float)
            title = self._title_extractor.extract_title(item)
            chart_data[title] = series
        return ChartFormattedData(DataFrame(chart_data))
