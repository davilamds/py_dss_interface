# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from py_dss_interface.models.DSSExecutive.DSSExecutiveI import DSSExecutiveI
from py_dss_interface.models.DSSExecutive.DSSExecutiveS import DSSExecutiveS


class DSSExecutive(DSSExecutiveS, DSSExecutiveI):
    """
    This interface implements the DSS_Executive (IDSS_Executive) interface of OpenDSS by declaring 2 procedures for
    accessing the different properties included in this interface: DSSExecutiveS, DSSExecutiveI
    """

    def __init__(self, obj_dss):
        super().__init__(obj_dss)

    @property
    def num_commands(self) -> int:
        return DSSExecutiveI._num_commands(self)

    @property
    def num_options(self) -> int:
        return DSSExecutiveI._num_options(self)

    def command(self, arg: str) -> str:
        return DSSExecutiveS._command(self, arg)

    def option(self, arg: str) -> str:
        return DSSExecutiveS._option(self, arg)

    def command_help(self, arg: str) -> str:
        return DSSExecutiveS._command_help(self, arg)

    def option_help(self, arg: str) -> str:
        return DSSExecutiveS._option_help(self, arg)

    def option_value(self, arg: str) -> str:
        return DSSExecutiveS._option_value(self, arg)

