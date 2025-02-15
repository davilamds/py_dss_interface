# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""

from py_dss_interface.models.Sensors.SensorsF import SensorsF
from py_dss_interface.models.Sensors.SensorsI import SensorsI
from py_dss_interface.models.Sensors.SensorsS import SensorsS
from py_dss_interface.models.Sensors.SensorsV import SensorsV
from typing import List


class Sensors(SensorsV, SensorsS, SensorsI, SensorsF):
    """
    This interface implements the Sensors (ISensors) interface of OpenDSS by declaring 4 procedures for accessing the
    different properties included in this interface: SensorsV, SensorsS, SensorsI, SensorsF.
    """

    def __init__(self, obj_dss):
        super().__init__(obj_dss)

    @property
    def pct_error(self) -> float:
        return SensorsF._pct_error_read(self)

    @pct_error.setter
    def pct_error(self, arg: float):
        SensorsF._pct_error_write(self, arg)

    @property
    def weight(self) -> float:
        return SensorsF._weight_read(self)

    @weight.setter
    def weight(self, arg: float):
        SensorsF._weight_write(self, arg)

    @property
    def kv_base(self) -> float:
        return SensorsF._kv_base_read(self)

    @kv_base.setter
    def kv_base(self, arg: float):
        SensorsF._kv_base_write(self, arg)

    @property
    def _count(self) -> int:
        return SensorsI._count(self)

    def first(self) -> int:
        return SensorsI._first(self)

    def next(self) -> int:
        return SensorsI._next(self)

    @property
    def is_delta(self) -> int:
        return SensorsI._is_delta_read(self)

    @is_delta.setter
    def is_delta(self, arg: int):
        SensorsI._is_delta_write(self, arg)

    @property
    def reverse_delta(self) -> int:
        return SensorsI._reverse_delta_read(self)

    @reverse_delta.setter
    def reverse_delta(self, arg: int):
        SensorsI._reverse_delta_write(self, arg)

    @property
    def metered_terminal(self) -> int:
        return SensorsI._metered_terminal_read(self)

    @metered_terminal.setter
    def metered_terminal(self, arg: int):
        SensorsI._metered_terminal_write(self, arg)

    def reset(self) -> int:
        return SensorsI._reset(self)

    def reset_all(self) -> int:
        return SensorsI._reset_all(self)

    @property
    def name(self) -> str:
        return SensorsS._name_read(self)

    @name.setter
    def name(self, arg: str):
        SensorsS._name_write(self, arg)

    @property
    def metered_element(self) -> str:
        return SensorsS._metered_element_read(self)

    @metered_element.setter
    def metered_element(self, arg: str):
        SensorsS._metered_element_write(self, arg)

    @property
    def names(self) -> List[str]:
        return SensorsV._names(self)

    @property
    def currents(self) -> List[float]:
        return SensorsV._currents_read(self)

    @currents.setter
    def currents(self, arg: List[float]):
        SensorsV._currents_write(self, arg)

    @property
    def kvars(self) -> List[float]:
        return SensorsV._kvars_read(self)

    @kvars.setter
    def kvars(self, arg: List[float]):
        SensorsV._kvars_write(self, arg)

    @property
    def kws(self) -> List[float]:
        return SensorsV._kws_read(self)

    @kws.setter
    def kws(self, arg: List[float]):
        SensorsV._kws_write(self, arg)
