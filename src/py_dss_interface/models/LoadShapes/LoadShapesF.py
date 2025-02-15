# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class LoadShapesF(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        double LoadShapeF(int32_t Parameter, double Argument);

    This interface returns a floating point number with the result of the query according to the value of the
    variable Parameter, which can be one of the following.
    """

    def _hr_interval(self) -> float:
        """Gets the fixed interval time value, hours."""
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _hr_interval_write(self, argument: float) -> float:
        """Sets the fixed interval time value, hours."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _min_interval(self) -> float:
        """Gets the fixed interval time value, in minutes."""
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _min_interval_write(self, argument: float) -> float:
        """Sets the fixed interval time value, in minutes."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _p_base(self) -> float:
        """Gets the base for normalizing P curve. If left at zero, the peak value is used."""
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _p_base_write(self, argument: float) -> float:
        """Sets the base for normalizing P curve. If left at zero, the peak value is used."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(5), ctypes.c_double(argument)))

    def _q_base(self) -> float:
        """Gets the base for normalizing Q curve. If left at zero, the peak value is used."""
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(6), ctypes.c_double(0)))

    def _q_base_write(self, argument: float) -> float:
        """Sets the base for normalizing Q curve. If left at zero, the peak value is used."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(7), ctypes.c_double(argument)))

    def _s_interval(self) -> float:
        """Gets the fixed interval data time interval, seconds."""
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(8), ctypes.c_double(0)))

    def _s_interval_write(self, argument: float) -> float:
        """Sets the fixed interval data time interval, seconds."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.LoadShapeF(ctypes.c_int32(9), ctypes.c_double(argument)))
