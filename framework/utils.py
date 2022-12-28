"""
Helpful functions
"""
from io import BufferedReader


def get_decoded_data(size: int, io_object: BufferedReader) -> str:
    """
    Reads file-like object and decodes it in UTF-8

    Args:
        size: amount of bytes to read
        io_object: file-like object
    Returns:
        decoded data
    """
    bytes_data = io_object.read(size)
    return bytes_data.decode(encoding='utf-8')
