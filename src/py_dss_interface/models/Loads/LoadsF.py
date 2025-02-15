# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""

import ctypes

from py_dss_interface.models.Base import Base


class LoadsF(Base):
    """
    This interface can be used to read/modify the properties of the Loads Class where the values are floating point
    numbers (double).

    The structure of the interface is as follows:
        double DSSLoadsF(int32_t Parameter,double Argument);

    This interface returns a Double (IEEE 754 64 bits), the variable “parameter” (Integer) is used to specify the
    property of the class to be used and the variable “argument” (double) can be used to modify the value of the
    property when necessary. Reading and writing properties are separated and require a different parameter number to
    be executed.

    The properties (parameter) are integer numbers and are described as follows.
    """

    def _kw(self) -> float:
        """Allows to read the kW property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _kw_write(self, argument) -> float:
        """Allows to write the kW property of the active load. The parameter argument must contain the new value in
        kW for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _kv(self) -> float:
        """Allows to read the kV property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _kv_write(self, argument) -> float:
        """Allows to write the kV property of the active load. The parameter argument must contain the new value in
        kV for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(3), ctypes.c_double(argument)))

    def _kvar(self) -> float:
        """Allows to read the kvar property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(4), ctypes.c_double(0)))

    def _kvar_write(self, argument) -> float:
        """Allows to write the kvar property of the active load. The parameter argument must contain the new value in
        kvar for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(5), ctypes.c_double(argument)))

    def _pf(self) -> float:
        """Allows to read the pf property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(6), ctypes.c_double(0)))

    def _pf_write(self, argument) -> float:
        """Allows to write the pf property of the active load. The parameter argument must contain the new value in
        pf for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(7), ctypes.c_double(argument)))

    def _pct_mean(self) -> float:
        """Allows to read the PctMean property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(8), ctypes.c_double(0)))

    def _pct_mean_write(self, argument) -> float:
        """Allows to write the PctMean property of the active load. The parameter argument must contain the new value
        in PctMean for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(9), ctypes.c_double(argument)))

    def _pct_std_dev(self) -> float:
        """Allows to read the PctStdDev property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(10), ctypes.c_double(0)))

    def _pct_std_dev_write(self, argument) -> float:
        """Allows to write the PctStdDev property of the active load. The parameter argument must contain the new
        value in PctStdDev for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(11), ctypes.c_double(argument)))

    def _allocation_factor(self) -> float:
        """Allows to read the AllocationFactor property of the active load. The parameter argument can be filled with
        a 0. """
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(12), ctypes.c_double(0)))

    def _allocation_factor_write(self, argument) -> float:
        """Allows to write the AllocationFactor property of the active load. The parameter argument must contain the
        new value in AllocationFactor for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(13), ctypes.c_double(argument)))

    def _c_factor(self) -> float:
        """Allows to read the CFactor property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(14), ctypes.c_double(0)))

    def _c_factor_write(self, argument: float) -> float:
        """Allows to write the CFactor property of the active load. The parameter argument must contain the new value
        in CFactor for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(15), ctypes.c_double(argument)))

    def _cvr_watts(self) -> float:
        """Allows to read the CVRWatts property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(16), ctypes.c_double(0)))

    def _cvr_watts_write(self, argument) -> float:
        """Allows to write the CVRWatts property of the active load. The parameter argument must contain the new
        value in CVRWatts for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(17), ctypes.c_double(argument)))

    def _cvr_vars(self) -> float:
        """Allows to read the CVRvars property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(18), ctypes.c_double(0)))

    def _cvr_vars_write(self, argument) -> float:
        """Allows to write the CVRvars property of the active load. The parameter argument must contain the new value
        in CVRWatts for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(19), ctypes.c_double(argument)))

    def _kva(self) -> float:
        """Allows to read the kva property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(20), ctypes.c_double(0)))

    def _kva_write(self, argument) -> float:
        """Allows to write the kva property of the active load. The parameter argument must contain the new value in
        kva for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(21), ctypes.c_double(argument)))

    def _kwh(self) -> float:
        """Allows to read the kWh property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(22), ctypes.c_double(0)))

    def _kwh_write(self, argument) -> float:
        """Allows to write the kWh property of the active load. The parameter argument must contain the new value in
        kWh for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(23), ctypes.c_double(argument)))

    def _kwh_days(self) -> float:
        """Allows to read the kWhdays property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(24), ctypes.c_double(0)))

    def _kwh_days_write(self, argument) -> float:
        """Allows to write the kWhdays property of the active load. The parameter argument must contain the new value
        in kWhdays for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(25), ctypes.c_double(argument)))

    def _r_neut(self) -> float:
        """Allows to read the RNeut (neutral resistance for wye connected loads) property of the active load. The
        parameter argument can be filled with a 0. """
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(26), ctypes.c_double(0)))

    def _r_neut_write(self, argument) -> float:
        """Allows to write the RNeut (neutral resistance for wye connected loads) property of the active load. The
        parameter argument must contain the new value in RNeut for the desired active load. The return value will be
        equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(27), ctypes.c_double(argument)))

    def _vmax_pu(self) -> float:
        """Allows to read the VMaxpu property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(28), ctypes.c_double(0)))

    def _vmax_pu_write(self, argument) -> float:
        """Allows to write the VMaxpu property of the active load. The parameter argument must contain the new value
        in VMaxpu for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(29), ctypes.c_double(argument)))

    def _vmin_emerg(self) -> float:
        """Allows to read the VMinemerg property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(30), ctypes.c_double(0)))

    def _vmin_emerg_write(self, argument) -> float:
        """Allows to write the VMinemerg property of the active load. The parameter argument must contain the new
        value in VMinemerg for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(31), ctypes.c_double(argument)))

    def _vmin_norm(self) -> float:
        """Allows to read the VMinnorm property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(32), ctypes.c_double(0)))

    def _vmin_norm_write(self, argument) -> float:
        """Allows to write the VMinnorm property of the active load. The parameter argument must contain the new
        value in VMinnorm for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(33), ctypes.c_double(argument)))

    def _vmin_pu(self) -> float:
        """Allows to read the VMinpu property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(34), ctypes.c_double(0)))

    def _vmin_pu_write(self, argument) -> float:
        """Allows to write the VMinpu property of the active load. The parameter argument must contain the new value
        in VMinpu for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(35), ctypes.c_double(argument)))

    def _xfkva(self) -> float:
        """Allows to read the xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor.
        Affects kW, kvar and pf.) property of the active load. The parameter argument can be filled with a 0. """
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(36), ctypes.c_double(0)))

    def _xfkva_write(self, argument) -> float:
        """Allows to write the xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor.
        Affects kW, kvar and pf.) property of the active load. The parameter argument must contain the new value in
        xfKVA for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(37), ctypes.c_double(argument)))

    def _x_neut(self) -> float:
        """Allows to read the Xneut property of the active load. The parameter argument can be filled with a 0."""
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(38), ctypes.c_double(0)))

    def _x_neut_write(self, argument) -> float:
        """Allows to write the Xneut property of the active load. The parameter argument must contain the new value
        in Xneut for the desired active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(39), ctypes.c_double(argument)))

    def _rl(self) -> float:
        """allows to read the PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies)
        property of the active load. The parameter argument can be filled with a 0. """
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(40), ctypes.c_double(0)))

    def _rl_write(self, argument) -> float:
        """allows to write the PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies)
        property of the active load. The parameter argument must contain the new value in PctSeriesRL for the desired
        active load. The return value will be equal to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(41), ctypes.c_double(argument)))

    def _rel_weight(self) -> float:
        """Allows to read the RelWeight (relative weighting factor) property of the active load. The parameter
        argument can be filled with a 0. """
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(42), ctypes.c_double(0)))

    def _rel_weight_write(self, argument) -> float:
        """Allows to write the RelWeight (relative weighting factor) property of the active load. The parameter
        argument must contain the new value in RelWeight for the desired active load. The return value will be equal
        to 0. """
        argument = Base.check_float_param(argument)
        return float(self.dss_obj.DSSLoadsF(ctypes.c_int32(43), ctypes.c_double(argument)))
