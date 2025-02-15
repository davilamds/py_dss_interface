# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class XYCurvesF(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        double XYCurvesF(int32_t Parameter, double Argument);

    This interface returns a floating point number with the result of the query according to the value of the
    variable Parameter, which can be one of the following.
    """

    def _x_read(self) -> float:
        """Gets the interpolated value after setting Y."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _x_write(self, argument) -> float:
        """Sets the X value."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _y_read(self) -> float:
        """Gets the interpolated value after setting X."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _y_write(self, argument) -> float:
        """Sets the Y value."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _x_shift_read(self) -> float:
        """Gets the amount to shift X value from original curve."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _x_shift_write(self, argument) -> float:
        """Sets the amount to shift X value from original curve."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(5), ctypes.c_double(argument)))

    def _y_shift_read(self) -> float:
        """Gets the amount to shift Y value from original curve."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(6), ctypes.c_double(0)))

    def _y_shift_write(self, argument) -> float:
        """Sets the amount to shift Y value from original curve."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(7), ctypes.c_double(argument)))

    def _x_scale_read(self) -> float:
        """Gets the factor to scale X values from original curve."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(8), ctypes.c_double(0)))

    def _x_scale_write(self, argument) -> float:
        """Sets the factor to scale X values from original curve."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(9), ctypes.c_double(argument)))

    def _y_scale_read(self) -> float:
        """Gets the factor to scale Y values from original curve."""
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(10), ctypes.c_double(0)))

    def _y_scale_write(self, argument) -> float:
        """Sets the factor to scale Y values from original curve."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.XYCurvesF(ctypes.c_int32(11), ctypes.c_double(argument)))
