from typing import Literal, Annotated

from pydantic import EncoderProtocol, EncodedBytes
from pydantic_core import PydanticCustomError


class HexEncoder(EncoderProtocol):
    """Standard (non-URL-safe) HEX encoder."""

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode the data from HEX encoded bytes to original bytes data.

        Args:
            data: The data to decode.

        Returns:
            The decoded data.
        """
        try:
            return bytes.fromhex(data.decode(encoding="ascii"))
        except ValueError as e:
            raise PydanticCustomError('hex_decode', "HEX decoding error: '{error}'", {'error': str(e)})

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode the data from bytes to a HEX encoded bytes.

        Args:
            value: The data to encode.

        Returns:
            The encoded data.
        """
        return value.hex().encode(encoding="ascii")

    @classmethod
    def get_json_format(cls) -> Literal['hex']:
        """Get the JSON format for the encoded data.

        Returns:
            The JSON format for the encoded data.
        """
        return 'hex'


HexBytes = Annotated[bytes, EncodedBytes(encoder=HexEncoder)]