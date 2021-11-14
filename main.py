from src.JpgHandler import JpgHandler
from src.ByteCache import ByteCache
import requests
import sys
import os

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Make sure to call the script like main.py <url> <sleeping_time> <dest_dir>")
        exit()

    url = sys.argv[1]
    sleeping_time = float(sys.argv[2])
    dest_dir = sys.argv[3]

    if not os.path.exists(dest_dir):
        print("destination dir " + dest_dir + " does not exist")
        exit()

    stream = requests.get(url, stream=True)

    # object that caches the latest 2 bytes of the stream (2 are necessary to identify the start and end of a jpg - https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)
    byte_cache = ByteCache()
    jpg_handler = JpgHandler(sleeping_time, dest_dir)

    print("Start reading bytes from stream " + url)

    # read bytes from stream and handle it respectively
    for byte in stream.iter_content(chunk_size=1):
        byte_cache.update(byte)

        if jpg_handler.is_sleeping():
            continue

        if jpg_handler.is_jpg_start(byte_cache.get_bytes()):
            jpg_handler.set_reading(True)
            jpg_handler.add_bytes_to_jpg(byte_cache.get_bytes())

        elif jpg_handler.is_jpg_end(byte_cache.get_bytes()) and jpg_handler.is_reading():
            jpg_handler.add_byte_to_jpg(byte)
            jpg_handler.set_reading(False)
            jpg_handler.save_jpg()
            jpg_handler.start_sleeping()
            jpg_handler.reset_jpg()

        elif jpg_handler.is_reading():
            jpg_handler.add_byte_to_jpg(byte)
