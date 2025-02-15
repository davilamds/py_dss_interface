# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models import Bridge
from py_dss_interface.models.Base import Base
from typing import List


class ParserV(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        void ParserV(int32_t Parameter, VARIANT *Argument);

    This interface returns a Variant with the result of the query according to the value of the variable Parameter,
    which can be one of the following.
    """

    # TODO include in test
    def _vector(self) -> List[float]:
        """Returns token as variant array of doubles. For parsing quoted array syntax."""
        return Bridge.variant_pointer_read(self.dss_obj.ParserV, 0)

    # TODO include in test
    def _matrix(self) -> List[float]:
        """Use this property to parse a Matrix token in OpenDSS format. Returns square matrix of order specified.
        Order same as default fortran order: column by column. """
        return Bridge.variant_pointer_read(self.dss_obj.ParserV, 1)

    # TODO include in test
    def _sym_matrix(self) -> List[float]:
        """Use this property to parse a Matrix token in lower triangular form. Symmetry is forced."""
        return Bridge.variant_pointer_read(self.dss_obj.ParserV, 2)
