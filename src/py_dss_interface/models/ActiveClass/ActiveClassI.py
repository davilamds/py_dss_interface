# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from py_dss_interface.models.Base import Base


class ActiveClassI(Base):

    def active_class_first(self):
        """Sets first element in the active class to be the active DSS object.
        If object is a CktElement, ActiveCktElement also points to this element. Returns 0 if none."""
        return self.dss_obj.get_integer(0, 0)

    def active_class_next(self):
        """Sets next element in the active class to be the active DSS object.
        If object is a CktElement, ActiveCktElement also points to this element. Returns 0 if none."""
        return self.dss_obj.get_integer(1, 0)

    def active_class_num_elements(self):
        """Gets the number of elements in this class. Same as Count Property."""
        return self.dss_obj.get_integer(2, 0)

    def active_class_count(self):
        """Gets the number of elements in this class. Same as NumElements Property."""
        return self.dss_obj.get_integer(3, 0)
