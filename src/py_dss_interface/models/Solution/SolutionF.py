# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class SolutionF(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        double SolutionF(int32_t Parameter, double Argument);

    This interface returns a floating point number according to the number sent in the variable “parameter”. The
    parameter can be one of the following.
    """

    def _frequency_read(self) -> float:
        """Returns the frequency for the next solution."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _frequency_write(self, argument) -> float:
        """Sets the frequency for the next solution."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _seconds_read(self) -> float:
        """Returns the seconds from top of the hour."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _seconds_write(self, argument) -> float:
        """Sets the seconds from top of the hour."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _step_size_read(self) -> float:
        """Returns the step size for the next solution."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _step_size_write(self, argument) -> float:
        """Sets the step size for the next solution."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(5), ctypes.c_double(argument)))

    def _load_mult_read(self) -> float:
        """Returns the default load multiplier applied to all non-fixed loads."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(6), ctypes.c_double(0)))

    def _load_mult_write(self, argument) -> float:
        """Sets the default load multiplier applied to all non-fixed loads."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(7), ctypes.c_double(argument)))

    def _tolerance_read(self) -> float:
        """Returns the solution convergence tolerance."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(8), ctypes.c_double(0)))

    def _tolerance_write(self, argument) -> float:
        """Sets the solution convergence tolerance."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(9), ctypes.c_double(argument)))

    def _pct_growth_read(self) -> float:
        """Returns the percent default annual load growth rate."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(10), ctypes.c_double(0)))

    def _pct_growth_write(self, argument) -> float:
        """Sets the percent default annual load growth rate."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(11), ctypes.c_double(argument)))

    def _gen_kw_read(self) -> float:
        """Returns the generator kW for AutoAdd mode."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(12), ctypes.c_double(0)))

    def _gen_kw_write(self, argument) -> float:
        """Sets the generator kW for AutoAdd mode."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(13), ctypes.c_double(argument)))

    def _gen_pf_read(self) -> float:
        """Returns the pf for generators in AutoAdd mode."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(14), ctypes.c_double(0)))

    def _gen_pf_write(self, argument) -> float:
        """Sets the pf for generators in AutoAdd mode."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(15), ctypes.c_double(argument)))

    def _cap_kvar_read(self) -> float:
        """Returns the capacitor kvar for adding in AutoAdd mode."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(16), ctypes.c_double(0)))

    def _cap_kvar_write(self, argument) -> float:
        """Sets the capacitor kvar for adding in AutoAdd mode."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(17), ctypes.c_double(argument)))

    def _gen_mult_read(self) -> float:
        """Returns the default multiplier applied to generators (like LoadMult)."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(18), ctypes.c_double(0)))

    def _gen_mult_write(self, argument) -> float:
        """Sets the default multiplier applied to generators (like LoadMult)."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(19), ctypes.c_double(argument)))

    def _dbl_hour_read(self) -> float:
        """Returns the hour as a double, including fractional part."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(20), ctypes.c_double(0)))

    def _dbl_hour_write(self, argument) -> float:
        """Sets the hour as a double, including fractional part."""
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(21), ctypes.c_double(argument)))

    def _step_size_min(self) -> float:
        """Sets the step size in minutes."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(22), ctypes.c_double(0)))

    def _step_size_hr(self) -> float:
        """Sets the step size in Hours."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(23), ctypes.c_double(0)))

    def _process_time(self) -> float:
        """Retrieves the time required (microseconds) to perform the latest solution time step,
        this time does not include the time required for sampling meters/monitors."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(24), ctypes.c_double(0)))

    def _total_time_read(self) -> float:
        """Retrieves the accumulated time required (microseconds) to perform the simulation."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(25), ctypes.c_double(0)))

    def _total_time_write(self, argument) -> float:
        """Sets the accumulated time (microseconds) register. The new value for this register must be specified in
        the argument. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.SolutionF(ctypes.c_int32(26), ctypes.c_double(argument)))

    def _process_time_step(self) -> float:
        """Retrieves the time required (microseconds) to perform the latest solution time step including the time
        required for sampling meters/monitors."""
        return float(self.dss_obj.SolutionF(ctypes.c_int32(27), ctypes.c_double(0)))
