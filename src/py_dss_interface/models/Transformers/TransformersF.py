# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class TransformersF(Base):
    """
    This interface can be used to read/modify the properties of the Transformers Class where the values are doubles.

    The structure of the interface is as follows:
        double TransformersF(int32_t Parameter, double argument) ;

    This interface returns a floating point number (64 bits), the variable “parameter” is used to specify the
    property of the class to be used and the variable “argument” can be used to modify the value of the property when
    necessary. Reading and writing properties are separated and require a different parameter number to be executed.

    The properties (parameter) are integer numbers and are described as follows.
    """

    def _r_read(self) -> float:
        """Gets the active winding resistance in %."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _r_write(self, argument) -> float:
        """Sets the active winding resistance in %."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _tap_read(self) -> float:
        """Gets the active winding tap in per-unit."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _tap_write(self, argument) -> float:
        """Sets the active winding tap in per-unit."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _min_tap_read(self) -> float:
        """Gets the active winding minimum tap in per-unit."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _min_tap_write(self, argument) -> float:
        """Sets the active winding minimum tap in per-unit."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(5), ctypes.c_double(argument)))

    def _max_tap_read(self) -> float:
        """Gets the active winding maximum tap in per-unit."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(6), ctypes.c_double(0)))

    def _max_tap_write(self, argument) -> float:
        """Sets the active winding maximum tap in per-unit."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(7), ctypes.c_double(argument)))

    def _kv_read(self) -> float:
        """Gets the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(8), ctypes.c_double(0)))

    def _kv_write(self, argument) -> float:
        """Sets the active winding kV rating. Phase-phase for 2 or 3 phases, actual winding kV 1 phase transformer."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(9), ctypes.c_double(argument)))

    def _kva_read(self) -> float:
        """Gets the active winding kVA rating. On winding 1, this also determines normal and emergency current
        ratings for all windings. """
        return float(self.dss_obj.TransformersF(ctypes.c_int32(10), ctypes.c_double(0)))

    def _kva_write(self, argument) -> float:
        """Sets the active winding kVA rating. On winding 1, this also determines normal and emergency current
        ratings for all windings. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(11), ctypes.c_double(argument)))

    def _x_neut_read(self) -> float:
        """Gets the active winding neutral reactance [ohms] for wye connections."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(12), ctypes.c_double(0)))

    def _x_neut_write(self, argument) -> float:
        """Sets the active winding neutral reactance [ohms] for wye connections."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(13), ctypes.c_double(argument)))

    def _r_neut_read(self) -> float:
        """Gets the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(14), ctypes.c_double(0)))

    def _r_neut_write(self, argument) -> float:
        """Sets the active winding neutral resistance [ohms] for wye connections. Set less than zero ungrounded wye."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(15), ctypes.c_double(argument)))

    def _xhl_read(self) -> float:
        """Gets the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding
        transformers. """
        return float(self.dss_obj.TransformersF(ctypes.c_int32(16), ctypes.c_double(0)))

    def _xhl_write(self, argument) -> float:
        """Sets the percent reactance between windings 1 and 2, on winding 1 kVA base. Use for 2 winding or 3 winding
        transformers. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(17), ctypes.c_double(argument)))

    def _xht_read(self) -> float:
        """Gets the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding transformers
        only."""
        return float(self.dss_obj.TransformersF(ctypes.c_int32(18), ctypes.c_double(0)))

    def _xht_write(self, argument) -> float:
        """Sets the percent reactance between windings 1 and 3, on winding 1 kVA base. Use for 3 winding transformers
        only. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(19), ctypes.c_double(argument)))

    def _xlt_read(self) -> float:
        """Gets he percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding transformers
        only. """
        return float(self.dss_obj.TransformersF(ctypes.c_int32(20), ctypes.c_double(0)))

    def _xlt_write(self, argument) -> float:
        """Sets the percent reactance between windings 2 and 3, on winding 1 kVA base. Use for 3 winding transformers
        only. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.TransformersF(ctypes.c_int32(21), ctypes.c_double(argument)))
