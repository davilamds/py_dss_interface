# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class SettingsI(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        int32_t SettingsI(int32_t Parameter, int32_t Argument);

    This interface returns an integer with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    def _allow_duplicates_read(self) -> int:
        """Gets if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}."""
        return self.dss_obj.SettingsI(ctypes.c_int32(0), ctypes.c_int32(0))

    def _allow_duplicates_write(self, argument) -> int:
        """Sets if OpenDSS allows duplicate names of objects: {1 allow, 0 not allow}."""
        argument = Base.check_int_param(argument)
        return self.dss_obj.SettingsI(ctypes.c_int32(1), ctypes.c_int32(argument))

    def _zone_lock_read(self) -> int:
        """Gets the status of Lock zones on energy meters to prevent rebuilding if a circuit
        change occurs: {1= true, 0= False}."""
        return self.dss_obj.SettingsI(ctypes.c_int32(2), ctypes.c_int32(0))

    def _zone_lock_write(self, argument) -> int:
        """Sets the status of Lock zones on energy meters to prevent rebuilding if a circuit change occurs: {1= true,
        0= False}. """
        argument = Base.check_int_param(argument)
        return self.dss_obj.SettingsI(ctypes.c_int32(3), ctypes.c_int32(argument))

    def _ckt_model_read(self) -> int:
        """Gets {dssMultiphase* | dssPositiveSeq} Indicate if the circuit model is positive sequence."""
        return self.dss_obj.SettingsI(ctypes.c_int32(4), ctypes.c_int32(0))

    def _ckt_model_write(self, argument) -> int:
        """Sets {dssMultiphase* | dssPositiveSeq} Indicate if the circuit model is positive sequence."""
        argument = Base.check_int_param(argument)
        return self.dss_obj.SettingsI(ctypes.c_int32(5), ctypes.c_int32(argument))

    def _trapezoidal_read(self) -> int:
        """Gets {True (1) | False (0)} value of trapezoidal integration flag in Energy Meters."""
        return self.dss_obj.SettingsI(ctypes.c_int32(6), ctypes.c_int32(0))

    def _trapezoidal_write(self, argument) -> int:
        """Sets {True (1) | False (0)} value of trapezoidal integration flag in Energy Meters."""
        argument = Base.check_int_param(argument)
        return self.dss_obj.SettingsI(ctypes.c_int32(7), ctypes.c_int32(argument))
