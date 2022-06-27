class TitleExtractor:
    def __init__(
        self, title_field: str = "LongTitle", language: str = "en", fallback_title: str = "data"
    ):
        self._title_field = title_field
        self._language = language
        self._fallback_title = fallback_title

    def extract_title(self, raw_timeseries: dict) -> str:
        free_texts = raw_timeseries["Attributes"]["FreeTexts"]
        selected_free_texts = [k for k in free_texts if k["Name"] == self._title_field]
        if not selected_free_texts:
            return self._fallback_title
        free_text = selected_free_texts[0]
        title_candidates = [
            k for k in free_text["RevisionValues"] if k["Language"] in {self._language, None}
        ]
        if not title_candidates:
            return self._fallback_title
        return title_candidates[0]["Value"]
