import wave
import os
from os import listdir
from os.path import isfile, join
from typing import List
import argparse

class Converter():
    def __init__(self, framerate):
        self.framerate: int = int(framerate)

    def convert_files(self, input_files, output_dir):
        """! Iterates throw all files and converts them
        """
        for file in input_files:
            basename = os.path.basename(file).replace(".raw", ".wav")
            output_file = join(output_dir, basename)
            self.convert_raw_to_wav(file, output_file)

    def convert_raw_to_wav(self, input_path: str, output_path: str) -> None:
        """! Converts single raw file to wav file
        """
        with open(input_path, "rb") as input_raw:
            data = input_raw.read()
            with wave.open(output_path, "wb") as out_wav:
                out_wav.setnchannels(1)
                out_wav.setsampwidth(2)  # number of bytes
                out_wav.setframerate(self.framerate)
                out_wav.writeframesraw(data)


def list_all_files(input_path: str) -> List[str]:
    """! Check if the input is a directory and list all raw files in the directory.
         If the input is a file, return this file.
    """
    input: List[str] = []
    if os.path.isdir(input_path):
        input = [join(input_path, f) for f in listdir(input_path) if
                 (isfile(join(input_path, f)) and f.endswith('.raw'))]
    elif os.path.isfile(input_path):
        input = [input_path]
    else:
        print("It is a special file (socket, FIFO, device file)")
    return input


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", metavar='input_path',
                        help="Path containing the .raw files or a single raw file")
    parser.add_argument("framerate", metavar='framerate',
                        help="Framerate used for conversion")

    args = parser.parse_args()
    input_path = args.input_path
    framerate = args.framerate

    output_dir = "converted_wav"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_files = list_all_files(input_path)

    converter = Converter(framerate)
    converter.convert_files(input_files, output_dir)


if __name__ == "__main__":
    main()
