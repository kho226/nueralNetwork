# This file is automatically generated by generate_ufuncs.py.
# Do not edit manually!

cdef extern from "_complexstuff.h":
    # numpy/npy_math.h doesn't have correct extern "C" declarations,
    # so we must include a wrapped version first
    pass

cdef extern from "numpy/npy_math.h":
    double NPY_NAN

cimport numpy as np
from numpy cimport (
    npy_float, npy_double, npy_longdouble,
    npy_cfloat, npy_cdouble, npy_clongdouble,
    npy_int, npy_long,
    NPY_FLOAT, NPY_DOUBLE, NPY_LONGDOUBLE,
    NPY_CFLOAT, NPY_CDOUBLE, NPY_CLONGDOUBLE,
    NPY_INT, NPY_LONG)

ctypedef double complex double_complex

cdef extern from "numpy/ufuncobject.h":
    int PyUFunc_getfperr() nogil

cdef public int wrap_PyUFunc_getfperr() nogil:
    """
    Call PyUFunc_getfperr in a context where PyUFunc_API array is initialized;
    this avoids messing with the UNIQUE_SYMBOL #defines
    """
    return PyUFunc_getfperr()

cimport libc

cimport sf_error

np.import_array()
np.import_ufunc()

cdef int _set_errprint(int flag) nogil:
    return sf_error.set_print(flag)
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double _func_faddeeva_dawsn "faddeeva_dawsn"(double) nogil
cdef void *_export_faddeeva_dawsn = <void*>_func_faddeeva_dawsn
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_dawsn_complex "faddeeva_dawsn_complex"(double complex) nogil
cdef void *_export_faddeeva_dawsn_complex = <void*>_func_faddeeva_dawsn_complex
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_erf "faddeeva_erf"(double complex) nogil
cdef void *_export_faddeeva_erf = <void*>_func_faddeeva_erf
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_erfc "faddeeva_erfc"(double complex) nogil
cdef void *_export_faddeeva_erfc = <void*>_func_faddeeva_erfc
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double _func_faddeeva_erfcx "faddeeva_erfcx"(double) nogil
cdef void *_export_faddeeva_erfcx = <void*>_func_faddeeva_erfcx
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_erfcx_complex "faddeeva_erfcx_complex"(double complex) nogil
cdef void *_export_faddeeva_erfcx_complex = <void*>_func_faddeeva_erfcx_complex
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double _func_faddeeva_erfi "faddeeva_erfi"(double) nogil
cdef void *_export_faddeeva_erfi = <void*>_func_faddeeva_erfi
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_erfi_complex "faddeeva_erfi_complex"(double complex) nogil
cdef void *_export_faddeeva_erfi_complex = <void*>_func_faddeeva_erfi_complex
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_log_ndtr "faddeeva_log_ndtr"(double complex) nogil
cdef void *_export_faddeeva_log_ndtr = <void*>_func_faddeeva_log_ndtr
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_ndtr "faddeeva_ndtr"(double complex) nogil
cdef void *_export_faddeeva_ndtr = <void*>_func_faddeeva_ndtr
cdef extern from "_ufuncs_cxx_defs.h":
    cdef double complex _func_faddeeva_w "faddeeva_w"(double complex) nogil
cdef void *_export_faddeeva_w = <void*>_func_faddeeva_w
# distutils: language = c++
