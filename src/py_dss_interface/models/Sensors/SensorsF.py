# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class SensorsF(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        double SensorsF(int32_t Parameter, double Argument);

    This interface returns a floating point number with the result of the query according to the value of the
    variable Parameter, which can be one of the following.
    """

    def _pct_error_read(self) -> float:
        """Gets the assumed percent error in the Sensor measurement. Default is 1."""
        return float(self.dss_obj.SensorsF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _pct_error_write(self, argument) -> float:
        """Sets the assumed percent error in the Sensor measurement. Default is 1."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SensorsF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _weight_read(self) -> float:
        """Gets the weighting factor for this sensor measurement with respect to the other sensors. Default is 1."""
        return float(self.dss_obj.SensorsF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _weight_write(self, argument) -> float:
        """Sets the weighting factor for this sensor measurement with respect to the other sensors. Default is 1."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SensorsF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _kv_base_read(self) -> float:
        """Gets the voltage base for the sensor measurements. LL for 2 and 3 - phase sensors, LN for 1-phase sensors."""
        return float(self.dss_obj.SensorsF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _kv_base_write(self, argument) -> float:
        """Sets the voltage base for the sensor measurements. LL for 2 and 3 - phase sensors, LN for 1-phase sensors."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SensorsF(ctypes.c_int32(5), ctypes.c_double(argument)))
