# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base
from typing import List


class RelaysV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void RelaysV(int32_t Parameter, VARIANT *Argument);

    This interface returns a Variant with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def _names(self) -> List[str]:
        """Getsa variant array of strings containing names of all relay elements."""
        return Bridge.variant_pointer_read(self.dss_obj.RelaysV, 0)
