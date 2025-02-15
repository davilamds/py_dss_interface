# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes

from py_dss_interface.models.Base import Base


class MonitorsI(Base):
    """
    This interface can be used to read/write certain properties of the active DSS object.

    The structure of the interface is as follows:
        int32_t MonitorsI(int32_t Parameter, int32_t Argument);

    This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be
    one of the following.
    """

    def _first(self) -> int:
        """Sets the first monitor active. Returns 0 if no monitors."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(0), ctypes.c_int32(0))

    def _next(self) -> int:
        """Set the next monitor active. Returns 0 if no more."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(1), ctypes.c_int32(0))

    def _reset(self) -> int:
        """Resets the active Monitor object."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(2), ctypes.c_int32(0))

    def _reset_all(self) -> int:
        """Resets all Monitor object."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(3), ctypes.c_int32(0))

    def _sample(self) -> int:
        """Causes active monitor to take a sample."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(4), ctypes.c_int32(0))

    def _save(self) -> int:
        """Causes active monitor to save its current sample buffer to its monitor stream.
        Then you can access the Bytestream or channel data. Most standard solution modes do this automatically."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(5), ctypes.c_int32(0))

    def _show(self) -> int:
        """Converts monitor file into text and displays with text editor."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(6), ctypes.c_int32(0))

    # TODO include in test
    def _mode(self) -> int:
        """Returns the monitor mode (bitmask integer - see DSS Help)."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(7), ctypes.c_int32(0))

    def _mode_write(self, argument: int) -> int:
        """Sets the monitor mode (bitmask integer - see DSS Help).
        Bitmask integer designating the values the monitor is to capture:
        0 = Voltages and currents at designated terminal
        1 = Powers at designated terminal
        2 = Tap Position (Transformer Device only)
        3 = State Variables (PCElements only)
        4 = Flicker level and severity index (Pst) for voltages. No adders apply.
            Flicker level at simulation time step, Pst at 10-minute time step.
        5 = Solution variables (Iterations, etc).
        Normally, these would be actual phasor quantities from solution.
        6 = Capacitor Switching (Capacitors only)
        7 = Storage state vars (Storage device only)
        8 = All winding currents (Transformer device only)
        9 = Losses, watts and var (of monitored device)
        10 = All Winding voltages (Transformer device only)
        Normally, these would be actual phasor quantities from solution.
        11 = All terminal node voltages and line currents of monitored device
        Combine mode with adders below to achieve other results for terminal quantities:
        +16 = Sequence quantities
        +32 = Magnitude only
        +64 = Positive sequence only or avg of all phases

        Mix adder to obtain desired results. For example:
        Mode=112 will save positive sequence voltage and current magnitudes only
        Mode=48 will save all sequence voltages and currents, but magnitude only.
        """
        return self.dss_obj.MonitorsI(ctypes.c_int32(8), ctypes.c_int32(argument))

    def _sample_count(self) -> int:
        """Returns number of examples in Monitor at present."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(9), ctypes.c_int32(0))

    def _sample_all(self) -> int:
        """Causes all Monitors to take a sample of the present state. Returns 0."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(10), ctypes.c_int32(0))

    def _save_all(self) -> int:
        """Save all Monitor buffers to their respective file streams. Returns 0."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(11), ctypes.c_int32(0))

    def _count(self) -> int:
        """Returns the number of monitors."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(12), ctypes.c_int32(0))

    def _process(self) -> int:
        """Post-process monitor examples taken so far, e.g., Pst for mode = 4."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(13), ctypes.c_int32(0))

    def _process_all(self) -> int:
        """Makes that all monitors post-process the data taken so far."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(14), ctypes.c_int32(0))

    def _file_version(self) -> int:
        """Returns the Monitor File version (integer)."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(15), ctypes.c_int32(0))

    def _record_size(self) -> int:
        """Returns the size of each record in ByteStream."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(16), ctypes.c_int32(0))

    def _num_channels(self) -> int:
        """Returns the number of Channels on the active Monitor."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(17), ctypes.c_int32(0))

    def _terminal(self) -> int:
        """Returns the terminal number of element being monitored."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(18), ctypes.c_int32(0))

    def _terminal_write(self, argument: int) -> int:
        """Sets sets the terminal number of element being monitored."""
        return self.dss_obj.MonitorsI(ctypes.c_int32(19), ctypes.c_int32(argument))
