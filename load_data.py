import argparse

import datetime
from datetime import date

from config import prepare_cfg
from shp2json import to_geojson

from sentinelsat import SentinelAPI, geojson_to_wkt


class Sentinel3LST:

    def __init__(self, config):
        self.cfg = config
        self.api = self._create_api()

    def _create_api(self):
        # TODO logger msg
        # TODO catch exceptions
        kwargs = self.cfg['api_args']
        api = SentinelAPI(**kwargs)

        return api

    def _get_products(self, footprint, date):
        kwargs = self.cfg['query_args']
        print(kwargs)
        products = self.api.query(
            footprint,
            date=date,
            # **kwargs
        )
        return products

    def download_data(self, footprint, date, data_dir=None):
        # TODO logger msg
        print(date)
        products = self._get_products(footprint, date)
        print(products)
        self.api.download_all(
            products,
            directory_path=data_dir if data_dir else self.cfg['default_data_dir']
        )


def prepare_date_prop(period: str):
    s_dates = period.split(',')
    dates = [date.strip() for date in s_dates]
    return tuple(dates)


def prepare_area_prop(path_to_shp: str):
    geojson = to_geojson(path_to_shp=path_to_shp)
    footprint = geojson_to_wkt(geojson_obj=geojson)
    return footprint


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--date',
                        help='Date or period when satellite made image. Use "," to separate values.',
                        default=((date.today() - datetime.timedelta(days=7)).strftime('%Y%m%d'), date.today().strftime('%Y%m%d')))
    parser.add_argument('-g', '--geolocation',
                        help="Path to folder with .shp (Shapefile) that include coordinates of needed region.",
                        default='coords/kyiv')

    cfg = prepare_cfg()
    args = parser.parse_args()

    s3lst = Sentinel3LST(cfg)
    print('start downloading')
    s3lst.download_data(
        prepare_area_prop(path_to_shp=args.geolocation),
        args.date
    )


if __name__ == "__main__":
    main()
