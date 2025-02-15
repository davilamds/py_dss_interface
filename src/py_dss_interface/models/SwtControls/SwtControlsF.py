# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""

import ctypes

from py_dss_interface.models.Base import Base


class SwtControlsF(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        double SwtControlsF(int32_t Parameter, double Argument);

    This interface returns a floating point number (64 bits) with the result of the query according to the value of
    the variable Parameter, which can be one of the following.
    """

    def _delay_read(self) -> float:
        """Gets the time delay [s] between arming and opening or closing the switch.
        Control may reset before actually operating the switch."""
        return float(self.dss_obj.SwtControlsF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _delay_write(self, argument) -> float:
        """Sets sets the time delay [s] between arming and opening or closing the switch.
        Control may reset before actually operating the switch."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SwtControlsF(ctypes.c_int32(1), ctypes.c_double(argument)))
