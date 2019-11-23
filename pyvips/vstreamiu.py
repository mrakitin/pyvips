from __future__ import division

import logging

import pyvips
from pyvips import ffi, vips_lib, Error

logger = logging.getLogger(__name__)


class Streamiu(pyvips.Streami):
    """An input stream you can connect action signals to to implement
    behaviour.

    Attach handlers to the `::read` and `::seek` signals to implement
    other behavours. Subclass this to add state.

    You can pass this stream to (for example) :meth:`new_from_stream`.

    """

    def __init__(self):
        pointer = vips_lib.vips_streamiu_new()
        if pointer == ffi.NULL:
            raise Error("can't create streamiu")

        super(Streamiu, self).__init__(pointer)


__all__ = ['Streamiu']