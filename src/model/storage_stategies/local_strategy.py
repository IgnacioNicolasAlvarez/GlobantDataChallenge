from src.client.avro import AvroWriter
from src.client.storage import Strategy


class LocalStrategy(Strategy):
    def __init__(
        self,
        avro_data_path: str,
        avro_schema_path: str,
        avro_schema_file: str,
        file_name: str,
    ):
        self.avro_data_path = avro_data_path
        self.avro_schema_path = avro_schema_path
        self.avro_schema_file = avro_schema_file
        self.file_name = file_name

    def create_snapshot(self, data: list) -> list:
        avro_writer = AvroWriter(
            avro_file_name=self.file_name,
            avro_path=self.avro_data_path,
            avro_schema_path=self.avro_schema_path,
            avro_schema_file=self.avro_schema_file,
        )
        avro_writer.write(data)

        return True
