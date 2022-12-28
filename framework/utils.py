"""
Helpful functions
"""
from io import BufferedReader
from quopri import decodestring as quopri_decodestring


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


def normalize_data(data: str):
    """
    Converts the transmitted data in accordance with UTF-8

    Args:
        data: data to normalize

    Returns:
        normalized data
    """
    normalized_data = bytes(data.replace('%', '=').replace("+", " "), 'UTF-8')
    return quopri_decodestring(normalized_data).decode('UTF-8')
