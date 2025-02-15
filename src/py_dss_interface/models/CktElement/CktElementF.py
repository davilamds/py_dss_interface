# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class CktElementF(Base):

    def _norm_amps(self) -> float:
        """Deliver the normal ampere rating for the active PDElement."""
        return float(self.dss_obj.CktElementF(ctypes.c_int32(0), ctypes.c_double(0)))

    def _norm_amps_write(self, argument: float) -> float:
        """Allows to fix the normal ampere rating for the active PDElement."""
        return float(self.dss_obj.CktElementF(ctypes.c_int32(1), ctypes.c_double(argument)))

    def _emerg_amps(self) -> float:
        """Deliver the Emergency ampere rating for the active PDElement."""
        return float(self.dss_obj.CktElementF(ctypes.c_int32(2), ctypes.c_double(0)))

    def _emerg_amps_write(self, argument: float) -> float:
        """Allows to fix the Emergency ampere rating for the active PDElement. The new value must be defined in the
        variable ?Argument?."""
        return float(self.dss_obj.CktElementF(ctypes.c_int32(3), ctypes.c_double(argument)))

    # TODO include in test
    def _variable_i(self, argument: float) -> float:
        """Delivers get the value of a variable by index for the active PCElement."""
        return float(self.dss_obj.CktElementF(ctypes.c_int32(4), ctypes.c_double(argument)))
