"""
Splinterglyph

Tools for encrypting and decrypting files using distributed
secret keys
"""

from importlib.metadata import metadata as importlib_metadata
from splinterglyph.splinterglyph_tools import decrypt
from splinterglyph.splinterglyph_tools import encrypt

__version__ = importlib_metadata("splinterglyph")["version"]
__author__ = "Bill Bradley"
__credits__ = "Mirabolic Consulting"

__all__ = [
    "decrypt",
    "encrypt",
]