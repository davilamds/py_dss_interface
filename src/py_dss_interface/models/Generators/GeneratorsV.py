# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from typing import List

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base


class GeneratorsV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void GeneratorsV(int32_t Parameter, VARIANT *Argument);

    This interface returns a Variant as a result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def _names(self) -> List[str]:
        """Gets the array of names of all Generator objects."""
        return Bridge.variant_pointer_read(self.dss_obj.GeneratorsV, 0)

    def _register_names(self) -> List[str]:
        """Gets the array of names of all generator Energy Meter registers."""
        return Bridge.variant_pointer_read(self.dss_obj.GeneratorsV, 1)

    def _register_values(self) -> List[float]:
        """Gets the array of values in generator Energy Meter registers."""
        return Bridge.variant_pointer_read(self.dss_obj.GeneratorsV, 2)
