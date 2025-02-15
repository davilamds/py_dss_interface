# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from typing import List

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base


class BusV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void BUSV(int32_t Parameter, VARIANT *Argument)

    This interface returns a variant according to the number sent in the variable “parameter”. The parameter can be
    one of the following.
    """

    def _voltages(self) -> List[float]:
        """Returns a complex array of voltages at this bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 0)

    def _seq_voltages(self) -> List[float]:
        """Returns a complex array of Sequence voltages at this bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 1)

    def _nodes(self) -> List[int]:
        """Returns an integer array of node numbers defined at the bus in same order as the voltages."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 2)

    def _voc(self) -> List[float]:
        """Returns the open circuit voltage as complex array."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 3)

    def _isc(self) -> List[float]:
        """Returns the short circuit current as complex array."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 4)

    def _pu_voltages(self) -> List[float]:
        """Returns the voltages in per unit at bus as complex array."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 5)

    def _zsc_matrix(self) -> List[float]:
        """Returns the complex array of Zsc matrix at bus, column by column."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 6)

    def _zsc1(self) -> List[float]:
        """Returns the complex array of Zsc matrix at bus, column by column."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 7)

    def _zsc0(self) -> List[float]:
        """Returns the complex zero-sequence short circuit impedance at bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 8)

    def _ysc_matrix(self) -> List[float]:
        """Returns the complex array of Ysc matrix at bus, column by column."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 9)

    def _cplx_sequence_voltages(self) -> List[float]:
        """Returns the complex double array of sequence voltages (0, 1, 2) at this bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 10)

    def _vll(self) -> List[float]:
        """For 2 and 3 phase buses, returns a variant array of complex numbers representing L-L voltages in volts.
        Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 11)

    def _pu_vll(self) -> List[float]:
        """Returns a variant array of complex numbers representing L-L voltages in per unit. Returns -1.0 for 1-phase
        bus. If more than 3 phases, returns only first 3. """
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 12)

    def _vmag_angle(self) -> List[float]:
        """Returns a variant array of doubles containing voltages in magnitude (VLN), angle (deg)."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 13)

    def _vmag_angle_pu(self) -> List[float]:
        """Returns a variant array of doubles containing voltages in per unit and angles in degrees."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 14)

    def _line_list(self) -> List[str]:
        """This parameter returns a variant array of strings containing the names of the lines connected to the
        active bus. The names of the lines include the class name 'Line.' """
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 15)

    def _load_list(self) -> List[str]:
        """This parameter returns a variant array of strings containing the names of the loads connected to the
        active bus. The names of the lines include the class name 'Load.'. """
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 16)

    def _axc_012_matrix(self) -> List[float]:
        """Variant array of doubles (complex) containing the complete 012 Zsc matrix."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 17)

    def _all_pce_active_bus(self) -> List[str]:
        """Returns an array with the names of all PCE connected to the active bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 18)

    def _all_pde_active_bus(self) -> List[str]:
        """Returns an array with the names of all PDE connected to the active bus."""
        return Bridge.variant_pointer_read(self.dss_obj.BUSV, 19)
