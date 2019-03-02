import glob
import shapefile


def to_geojson(path_to_shp: str):
    filename = find_shapefile(path_to_shp)
    reader = shapefile.Reader(filename, encoding='latin-1')
    buffer = create_buffer(reader)

    return {
        'type': 'FeatureCollection',
        'features': buffer,
    }


def find_shapefile(path_to_shp: str) -> str:
    pattern = '{}/*.shp'.format(path_to_shp)
    files = glob.glob(pattern)

    return files[0]


def create_buffer(reader: shapefile.Reader) -> list:
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []

    for shape_record in reader.shapeRecords():
        buffer.append(create_feature(shape_record, field_names))

    return buffer


def create_feature(shape_record: shapefile.ShapeRecord, field_names: list):
    properties = dict(zip(field_names, shape_record.record))
    geometry = shape_record.shape.__geo_interface__

    return {
        'type': 'Feature',
        'geometry': geometry,
        'properties': properties,
    }
