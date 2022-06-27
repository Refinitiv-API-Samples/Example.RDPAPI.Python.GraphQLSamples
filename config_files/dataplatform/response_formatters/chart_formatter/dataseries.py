from pandas import DataFrame, Series


class DataSeriesExtractor:
    def __init__(self):
        self._index_type = "datetime64[ns]"

    def extract_series(self, raw_timeseries: dict, data_type: type) -> Series:
        timeseries = DataFrame.from_dict(raw_timeseries)["SingleObservations"]["TimeSeries"]
        series_df = DataFrame.from_dict(timeseries)
        timeseries_df = series_df["Value"].astype(data_type)
        timeseries_df.index = series_df["ObservationPeriod"].astype(self._index_type)
        return timeseries_df
