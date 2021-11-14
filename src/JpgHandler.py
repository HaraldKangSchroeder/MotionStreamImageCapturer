import threading
import io
from PIL import Image
import datetime

jpg_data = {
    "start_bytes": [b'\xff', b'\xd8'],
    "end_bytes": [b'\xff', b'\xd9']
}


class JpgHandler:
    def __init__(self, sleeping_time=60, dir="./"):
        self.jpg = []
        self.reading = False
        self.sleeping = False
        self.sleeping_time = sleeping_time
        self.dir = dir

    def is_jpg_start(self, bytes):
        global jpg_data
        return self.__is_jpg_border(bytes, jpg_data["start_bytes"])

    def is_jpg_end(self, bytes):
        global jpg_data
        return self.__is_jpg_border(bytes, jpg_data["end_bytes"])

    def is_reading(self):
        return self.reading

    def set_reading(self, reading):
        self.reading = reading

    def is_sleeping(self):
        return self.sleeping

    def add_byte_to_jpg(self, byte):
        self.jpg.append(byte)

    def add_bytes_to_jpg(self, bytes):
        self.jpg += bytes

    def reset_jpg(self):
        self.jpg = []

    def start_sleeping(self):
        self.__set_sleeping(True)
        threading.Timer(self.sleeping_time,
                        self.__set_sleeping, [False]).start()

    def save_jpg(self):
        image_file = Image.open(io.BytesIO(get_byte_array(self.jpg)))
        image_file.save(
            self.dir + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".jpg")

    def __is_jpg_border(self, bytes, border_bytes):
        for i in range(0, len(bytes)):
            if bytes[i] != border_bytes[i]:
                return False
        return True

    def __set_sleeping(self, sleeping):
        self.sleeping = sleeping


def get_byte_array(bytes):
    ba = bytearray()
    for b in bytes:
        ba += b
    return ba
