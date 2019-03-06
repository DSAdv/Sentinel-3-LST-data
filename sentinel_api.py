"""
Module for loading data from DataHub.
"""
from sentinelsat import SentinelAPI

from config import Config, LSTConfigKiev


class DataLoader:

    def __init__(self, cfg: Config):
        cfg.check_dirs(cfg.DEFAULT_DATA_DIR, cfg.DEFAULT_COORDS_DIR)
        self.cfg = cfg
        self.api = self._create_api()

    def _create_api(self):
        # TODO logger
        kwargs = self.cfg.API_KWARGS
        api = SentinelAPI(**kwargs)
        return api

    def _get_products(self):
        # TODO logger
        kwargs = self.cfg.QUERY_KWARGS
        products = self.api.query(
            self.cfg.FOOTPRINT,
            date=(self.cfg.DATE_FROM, self.cfg.DATE_TO),
            **kwargs
        )
        return products

    def download(self):
        # TODO logger
        products = self._get_products()

        self.api.download_all(
            products,
            directory_path=self.cfg.DEFAULT_DATA_DIR
        )


def main():
    cfg = LSTConfigKiev()
    loader = DataLoader(cfg)
    loader.download()


if __name__ == "__main__":
    main()
