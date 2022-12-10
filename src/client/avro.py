from avro.schema import parse
from avro.datafile import DataFileWriter
from avro.io import DatumWriter


class AvroWriter:
    def __init__(self, avro_schema_file, path, file_name):
        self.avro_data_file = path + file_name + ".avro"
        self.schema = parse(open(avro_schema_file, "rb").read())

    def write(self, data: list):
        with DataFileWriter(
            open(self.avro_data_file, "wb"), DatumWriter(), self.schema
        ) as writer:

            for d in data:
                writer.append(d.dict())
