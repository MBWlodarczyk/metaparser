import logging
from typing import Optional, Type

import magic  # type: ignore

from .base import BaseParser
from .exif import ExifParser
from .mp3 import Mp3Parser

PARSERS = [ExifParser, Mp3Parser]

log = logging.getLogger(__name__)


class ParserFactory:
    @staticmethod
    def get_parser_for_file(filename: str) -> Optional[Type[BaseParser]]:
        mime = magic.from_file(filename, mime=True)
        log.debug("Detected MIME type '%s' for file '%s'", mime, filename)

        return ParserFactory.get_parser(mime)

    @staticmethod
    def get_parser(mime) -> Optional[Type[BaseParser]]:
        for parser in PARSERS:
            if mime in parser.supported_mimes():
                return parser

        return None