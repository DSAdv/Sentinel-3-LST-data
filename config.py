import os
import json
import logging


class Config(object):

    DEFAULT_DATA_DIR = 'data'
    DEFAULT_COORDS_DIR = 'coords'

    FOOTPRINT = ''
    DATE_FROM = ''
    DATE_TO = ''

    API_KWARGS = {}

    QUERY_KWARGS = {}

    @staticmethod
    def check_dirs(*paths: list):
        """
        Check list of directory paths and create they if not exists.
        """
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)


class LSTConfigKiev(Config):

    DEFAULT_COORDS_DIR = 'coords/kiev'

    FOOTPRINT = 'POLYGON((29.004285434863732 51.71104336978721, 32.34412918486373 51.71104336978721,32.34412918486373 49.172018017942364,29.004285434863732 49.172018017942364,29.004285434863732 51.71104336978721))'
    DATE_FROM = 'NOW-1DAY'
    DATE_TO = 'NOW'

    API_KWARGS = {
        "user": "s3guest",
        "password": "s3guest",
        "api_url": "https://scihub.copernicus.eu/s3/#/home",
    }

    QUERY_KWARGS = {
        "productlevel": "L2",
        "producttype": "SL_2_LST___",
        "platformname": "Sentinel-3",
        "instrumentshortname": "SLSTR",
        "timeliness": "Near Real Time"
    }
