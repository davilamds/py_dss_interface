# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 30/04/2021
"""
import ctypes
import logging
import struct
import sys

import numpy as np
import pandas as pd
from comtypes import automation

logger = logging.getLogger('opendssdirect.core')


def is_x64():
    return struct.calcsize("P") == 8


def is_delphi():
    return 'darwin' not in sys.platform and 'linux' not in sys.platform


POINTER = ctypes.c_int64 if is_x64() else ctypes.c_int32
HEADER_SIZE = 4 if is_delphi() else 8


class ArrayEnio(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_int),
        ('data', ctypes.POINTER(ctypes.c_float)),
    ]


class VArg(ctypes.Structure):
    _fields_ = [
        ('dtype', ctypes.c_uint64),
        ('p', ctypes.POINTER(None)),
        ('dum1', ctypes.c_uint64),
        ('dum2', ctypes.c_uint64),
    ]


class VarArray(ctypes.Structure):
    _fields_ = [
        ('dimcount', ctypes.c_uint8),
        ('flags', ctypes.c_uint8),
        ('elementsize', ctypes.c_uint32),
        ('lockcount', ctypes.c_uint32),
        ('data', ctypes.POINTER(None)),
        ('length', ctypes.c_uint),
        ('lbound', ctypes.c_uint),
    ]


def c_types_function(f, param, dss_arg, name):
    if isinstance(dss_arg, str):
        dss_arg = dss_arg.encode('ascii')

    logger.debug(f"Calling function {name} with arguments {(param, dss_arg)}")
    r = f(param, dss_arg)

    if isinstance(r, bytes):
        r = r.decode('ascii')
    return r

def variant_pointer_read(f, param: int, optional=None) -> list:
    variant_pointer = ctypes.pointer(automation.VARIANT())
    if optional:
        f(ctypes.c_int(param), variant_pointer, optional)
    else:
        f(ctypes.c_int(param), variant_pointer)
    return list(variant_pointer.contents.value)

def variant_pointer_write(f, param: int, arg: list) -> list:
    variant_pointer = ctypes.pointer(automation.VARIANT())
    variant_pointer.contents.value = arg
    f(ctypes.c_int(param), variant_pointer)
    return list(variant_pointer.contents.value)

def var_array_function(f, param, optional, name):
    varg = VArg(0, None, 0, 0)
    p = ctypes.POINTER(VArg)(varg)
    if optional is not None:
        f(param, p, optional)
    else:
        logger.debug(f"Calling function {name} with arguments {(param, p)}")
        f(param, p)

    logger.debug(f"Successively called and returned from function {name}")
    var_arr = ctypes.cast(varg.p, ctypes.POINTER(VarArray)).contents

    l_ = []
    if varg.dtype == 0x2008 and var_arr.length != 0:  # CString
        data = ctypes.cast(var_arr.data, ctypes.POINTER(POINTER * var_arr.length))
        for s in data.contents:
            if s == 0:
                continue
            length = ctypes.cast(s - HEADER_SIZE, ctypes.POINTER(ctypes.c_uint8)).contents.value
            if is_delphi():
                length = int(length / 2)
            s = ctypes.cast(s, ctypes.POINTER(ctypes.c_int16 * length))
            s = u''.join(chr(x) for x in s.contents[:])
            if s.lower() != 'none':
                l_.append(s)

    elif varg.dtype == 0x2005 and var_arr.length != 0:  # Float64
        data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_double * var_arr.length))
        # Converting CFloat to Python float, more efficiency could be gained by using NumPy
        l_.extend(iter(data.contents))
    elif varg.dtype == 0x2003 and var_arr.length != 0:  # Int32
        data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32 * var_arr.length))
        # Converting CInt32 to Python float, more efficiency could be gained by using NumPy
        l_.extend(iter(data.contents))
    elif varg.dtype == 0x2011 and var_arr.length != 0:
        signature = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32)).contents.value

        if signature != 43756:
            logger.warning(
                f"ByteStream did not contain expected signature. Found {signature} but expected 43756"
            )

        else:
            # data = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32 * 4))
            # signature, version, size, param = data.contents

            p = ctypes.cast(var_arr.data, ctypes.POINTER(ctypes.c_int32))
            a_ptr = ctypes.cast(p, ctypes.c_void_p)
            a_ptr.value += ctypes.sizeof(p._type_)
            version = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value
            a_ptr.value += ctypes.sizeof(p._type_)
            size = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value
            a_ptr.value += ctypes.sizeof(p._type_)
            param = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_int32)).contents.value
            logger.debug(
                "version={version}, size={size}, param={param}".format(version=version, size=size, param=param))

            a_ptr.value += ctypes.sizeof(p._type_)
            header = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_char * 256)).contents.value
            header = [i.strip() for i in header.decode('ascii').strip().rstrip(',').split(',')]

            a_ptr.value = a_ptr.value + 256 * ctypes.sizeof(ctypes.c_char)
            count = (var_arr.length - 272) / 4 / (size + 2)

            if int(count) != count:
                logger.error(
                    "Expected count to be integer but found count={count}".format(
                        count=count,
                    )
                )
            else:
                count = int(count)

            data = ctypes.cast(a_ptr, ctypes.POINTER(ctypes.c_float * (size + 2) * count))

            for row in data.contents[:]:
                l_.extend(iter(row[:]))
            try:
                l_ = np.array(l_).reshape([-1, len(header)])
                l_ = pd.DataFrame(l_, columns=header)
            except NameError:
                l_ = [l_, header]

    elif var_arr.length == 0:
        logger.warning("Empty var_arr found")
    else:
        logger.warning(
            f"Unsupported dtype {varg.dtype} returned for {name}. Please contact developer"
        )

    return l_
