# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base
from typing import List


class TopologyV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void TopologyV(int32_t Parameter, VARIANT *Argument);

    This interface returns a Variant with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def _all_looped_pairs(self) -> List[str]:
        """Gets a variant array of all looped element names, by pairs."""
        return Bridge.variant_pointer_read(self.dss_obj.TopologyV, 0)

    def _all_isolated_branches(self) -> List[str]:
        """Gets a variant array of all isolated branch names."""
        return Bridge.variant_pointer_read(self.dss_obj.TopologyV, 1)

    def _all_isolated_loads(self) -> List[str]:
        """Gets a variant array of all isolated load names."""
        return Bridge.variant_pointer_read(self.dss_obj.TopologyV, 2)
