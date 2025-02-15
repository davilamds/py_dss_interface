# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base
from py_dss_interface.models.Meters import Meters
from py_dss_interface.models.Text.Text import Text
from typing import List


class MetersV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void MetersV(int32_t Parameter, VARIANT *arg);

    This interface returns a variant according to the number sent in the variable “parameter”. The parameter can be
    one of the following.
    """

    # TODO add type return

    def _names(self) -> List[str]:
        """Returns an array of all Energy Meter names."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 0)

    def _register_names(self) -> List[str]:
        """Returns an array of strings containing the names of the registers."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 1)

    def _register_values(self) -> List[float]:
        """Returns an array of values contained in the Meter registers for the active Meter."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 2)

    def _totals(self) -> List[float]:
        """Returns the totals for all registers of all Meters."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 3)

    def _peak_current_read(self) -> List[float]:
        """Returns an array of doubles with the Peak Current Property."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 4)

    def _peak_current_write(self, arg: List[float]) -> List[float]:
        """Receives an array of doubles to set values of Peak Current Property."""
        return Bridge.variant_pointer_write(self.dss_obj.MetersV, 5, arg)

    def _calc_current_read(self) -> List[float]:
        """Returns the magnitude of the real part of the Calculated Current (normally determined by solution)
        for the meter to force some behavior on Load Allocation."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 6)

    # TODO: Ênio - https://github.com/PauloRadatz/py_dss_interface/issues/6
    # TODO include in test
    def _calc_current_write(self, arg: List[float]) -> List[float]:
        """Sets the magnitude of the real part of the Calculated Current (normally determined by solution)
        for the meter to force some behavior on Load Allocation."""
        return Bridge.variant_pointer_write(self.dss_obj.MetersV, 7, arg)

    def _alloc_factors_read(self) -> List[float]:
        """Returns an array of doubles: allocation factors for the active Meter."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 8)

    # TODO: Ênio - https://github.com/PauloRadatz/py_dss_interface/issues/7
    def _alloc_factors_write(self, arg: List[float]) -> List[float]:
        """Receives an array of doubles to set the phase allocation factors for the active Meter."""
        return Bridge.variant_pointer_write(self.dss_obj.MetersV, 9, arg)

    # TODO: Ênio - https://github.com/PauloRadatz/py_dss_interface/issues/8
    def _all_end_elements(self) -> List[str]:
        """Returns a variant array of names of all zone end elements."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 10)

    # TODO: Ênio - https://github.com/PauloRadatz/py_dss_interface/issues/9
    # TODO include in test
    def _all_branches_in_zone(self) -> List[str]:
        """Returns a wide string list of all branches in zone of the active Energy Meter object."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 11)

    def _all_pce_in_zone(self) -> List[str]:
        """This parameter returns a wide string list of all the PCE in zone of the active Energy Meter object."""
        return Bridge.variant_pointer_read(self.dss_obj.MetersV, 12)
