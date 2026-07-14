import math


inf = math.inf


from dataclasses import dataclass
from typing import List, Union

_LIR_UNDEF = object()
class _LirAbsent:
    __slots__ = ()
_LIR_ABSENT = _LirAbsent()

def _lir_result_getattr(self, name):
    if name in type(self)._lir_absent_fields:
        return _LIR_ABSENT
    raise AttributeError(name)

@dataclass(init=False)
class __diode_va_model_rawResult:
    __slots__ = ["model_param_cj0", "model_param_ea", "model_param_is", "model_param_m", "model_param_minr", "model_param_n", "model_param_rs", "model_param_rth", "model_param_tnom", "model_param_vj", "model_param_zetais", "model_param_zetars", "model_param_zetarth", "_flags", "_invalid_params"]
    _lir_absent_fields = frozenset(("model_param_cj0", "model_param_ea", "model_param_is", "model_param_m", "model_param_minr", "model_param_n", "model_param_rs", "model_param_rth", "model_param_tnom", "model_param_vj", "model_param_zetais", "model_param_zetars", "model_param_zetarth"))
    __getattr__ = _lir_result_getattr
    model_param_cj0: Union[float, _LirAbsent]
    model_param_ea: Union[float, _LirAbsent]
    model_param_is: Union[float, _LirAbsent]
    model_param_m: Union[float, _LirAbsent]
    model_param_minr: Union[float, _LirAbsent]
    model_param_n: Union[float, _LirAbsent]
    model_param_rs: Union[float, _LirAbsent]
    model_param_rth: Union[float, _LirAbsent]
    model_param_tnom: Union[float, _LirAbsent]
    model_param_vj: Union[float, _LirAbsent]
    model_param_zetais: Union[float, _LirAbsent]
    model_param_zetars: Union[float, _LirAbsent]
    model_param_zetarth: Union[float, _LirAbsent]
    _flags: int
    _invalid_params: List[str]

    def __init__(self):
        self._flags = 0
        self._invalid_params = []

def __diode_va_model_raw_entry(_lir_capture_model_param_cj0, _lir_capture_model_param_ea, _lir_capture_model_param_is, _lir_capture_model_param_m, _lir_capture_model_param_minr, _lir_capture_model_param_n, _lir_capture_model_param_rs, _lir_capture_model_param_rth, _lir_capture_model_param_tnom, _lir_capture_model_param_vj, _lir_capture_model_param_zetais, _lir_capture_model_param_zetars, _lir_capture_model_param_zetarth, _lir_invalid_params, param_is, given_is, param_rs, given_rs, param_zetars, given_zetars, param_n, given_n, param_cj0, given_cj0, param_vj, given_vj, param_m, given_m, param_rth, given_rth, param_zetarth, given_zetarth, param_zetais, given_zetais, param_ea, given_ea, param_tnom, given_tnom, param_minr, given_minr):
    if given_is:
        if not (((0) <= (param_is)) & ((param_is) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(0) }")
    else:
        _lir_capture_model_param_is = 0.00000000000001
    if given_rs:
        if not (((0) <= (param_rs)) & ((param_rs) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(1) }")
    else:
        _lir_capture_model_param_rs = 0
    if given_zetars:
        if not (((-10) <= (param_zetars)) & ((param_zetars) <= (10))):
            _lir_invalid_params.append("Parameter { id: ParamId(2) }")
    else:
        _lir_capture_model_param_zetars = 0
    if given_n:
        if not (((0) <= (param_n)) & ((param_n) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(3) }")
    else:
        _lir_capture_model_param_n = 1
    if given_cj0:
        if not (((0) <= (param_cj0)) & ((param_cj0) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(4) }")
    else:
        _lir_capture_model_param_cj0 = 0
    if given_vj:
        if not (((0.2) <= (param_vj)) & ((param_vj) <= (2))):
            _lir_invalid_params.append("Parameter { id: ParamId(5) }")
    else:
        _lir_capture_model_param_vj = 1
    if given_m:
        if not (((0) <= (param_m)) & ((param_m) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(6) }")
    else:
        _lir_capture_model_param_m = 0.5
    if given_rth:
        if not (((0) <= (param_rth)) & ((param_rth) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(7) }")
    else:
        _lir_capture_model_param_rth = 0
    if given_zetarth:
        if not (((-10) <= (param_zetarth)) & ((param_zetarth) <= (10))):
            _lir_invalid_params.append("Parameter { id: ParamId(8) }")
    else:
        _lir_capture_model_param_zetarth = 0
    if given_zetais:
        if not (((-10) <= (param_zetais)) & ((param_zetais) <= (10))):
            _lir_invalid_params.append("Parameter { id: ParamId(9) }")
    else:
        _lir_capture_model_param_zetais = 3
    if given_ea:
        if not (((-10) <= (param_ea)) & ((param_ea) <= (10))):
            _lir_invalid_params.append("Parameter { id: ParamId(10) }")
    else:
        _lir_capture_model_param_ea = 1.11
    if given_tnom:
        if not (((0) <= (param_tnom)) & ((param_tnom) <= (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(11) }")
    else:
        _lir_capture_model_param_tnom = 300
    if given_minr:
        if not (((0) < (param_minr)) & ((param_minr) < (inf))):
            _lir_invalid_params.append("Parameter { id: ParamId(12) }")
        _lir_result = __diode_va_model_rawResult()
        if _lir_capture_model_param_cj0 is not _LIR_ABSENT:
            _lir_result.model_param_cj0 = _lir_capture_model_param_cj0
        if _lir_capture_model_param_ea is not _LIR_ABSENT:
            _lir_result.model_param_ea = _lir_capture_model_param_ea
        if _lir_capture_model_param_is is not _LIR_ABSENT:
            _lir_result.model_param_is = _lir_capture_model_param_is
        if _lir_capture_model_param_m is not _LIR_ABSENT:
            _lir_result.model_param_m = _lir_capture_model_param_m
        if _lir_capture_model_param_minr is not _LIR_ABSENT:
            _lir_result.model_param_minr = _lir_capture_model_param_minr
        if _lir_capture_model_param_n is not _LIR_ABSENT:
            _lir_result.model_param_n = _lir_capture_model_param_n
        if _lir_capture_model_param_rs is not _LIR_ABSENT:
            _lir_result.model_param_rs = _lir_capture_model_param_rs
        if _lir_capture_model_param_rth is not _LIR_ABSENT:
            _lir_result.model_param_rth = _lir_capture_model_param_rth
        if _lir_capture_model_param_tnom is not _LIR_ABSENT:
            _lir_result.model_param_tnom = _lir_capture_model_param_tnom
        if _lir_capture_model_param_vj is not _LIR_ABSENT:
            _lir_result.model_param_vj = _lir_capture_model_param_vj
        if _lir_capture_model_param_zetais is not _LIR_ABSENT:
            _lir_result.model_param_zetais = _lir_capture_model_param_zetais
        if _lir_capture_model_param_zetars is not _LIR_ABSENT:
            _lir_result.model_param_zetars = _lir_capture_model_param_zetars
        if _lir_capture_model_param_zetarth is not _LIR_ABSENT:
            _lir_result.model_param_zetarth = _lir_capture_model_param_zetarth
        _lir_result._flags = 0
        _lir_result._invalid_params = _lir_invalid_params
        return _lir_result
    else:
        simparam_minr = _lir_simparam_opt("minr", 0.001)
        if ((0) < (simparam_minr)) & ((simparam_minr) < (inf)):
            _lir_capture_model_param_minr = simparam_minr
            _lir_result = __diode_va_model_rawResult()
            if _lir_capture_model_param_cj0 is not _LIR_ABSENT:
                _lir_result.model_param_cj0 = _lir_capture_model_param_cj0
            if _lir_capture_model_param_ea is not _LIR_ABSENT:
                _lir_result.model_param_ea = _lir_capture_model_param_ea
            if _lir_capture_model_param_is is not _LIR_ABSENT:
                _lir_result.model_param_is = _lir_capture_model_param_is
            if _lir_capture_model_param_m is not _LIR_ABSENT:
                _lir_result.model_param_m = _lir_capture_model_param_m
            if _lir_capture_model_param_minr is not _LIR_ABSENT:
                _lir_result.model_param_minr = _lir_capture_model_param_minr
            if _lir_capture_model_param_n is not _LIR_ABSENT:
                _lir_result.model_param_n = _lir_capture_model_param_n
            if _lir_capture_model_param_rs is not _LIR_ABSENT:
                _lir_result.model_param_rs = _lir_capture_model_param_rs
            if _lir_capture_model_param_rth is not _LIR_ABSENT:
                _lir_result.model_param_rth = _lir_capture_model_param_rth
            if _lir_capture_model_param_tnom is not _LIR_ABSENT:
                _lir_result.model_param_tnom = _lir_capture_model_param_tnom
            if _lir_capture_model_param_vj is not _LIR_ABSENT:
                _lir_result.model_param_vj = _lir_capture_model_param_vj
            if _lir_capture_model_param_zetais is not _LIR_ABSENT:
                _lir_result.model_param_zetais = _lir_capture_model_param_zetais
            if _lir_capture_model_param_zetars is not _LIR_ABSENT:
                _lir_result.model_param_zetars = _lir_capture_model_param_zetars
            if _lir_capture_model_param_zetarth is not _LIR_ABSENT:
                _lir_result.model_param_zetarth = _lir_capture_model_param_zetarth
            _lir_result._flags = 0
            _lir_result._invalid_params = _lir_invalid_params
            return _lir_result
        else:
            _lir_invalid_params.append("Parameter { id: ParamId(12) }")
            _lir_capture_model_param_minr = simparam_minr
            _lir_result = __diode_va_model_rawResult()
            if _lir_capture_model_param_cj0 is not _LIR_ABSENT:
                _lir_result.model_param_cj0 = _lir_capture_model_param_cj0
            if _lir_capture_model_param_ea is not _LIR_ABSENT:
                _lir_result.model_param_ea = _lir_capture_model_param_ea
            if _lir_capture_model_param_is is not _LIR_ABSENT:
                _lir_result.model_param_is = _lir_capture_model_param_is
            if _lir_capture_model_param_m is not _LIR_ABSENT:
                _lir_result.model_param_m = _lir_capture_model_param_m
            if _lir_capture_model_param_minr is not _LIR_ABSENT:
                _lir_result.model_param_minr = _lir_capture_model_param_minr
            if _lir_capture_model_param_n is not _LIR_ABSENT:
                _lir_result.model_param_n = _lir_capture_model_param_n
            if _lir_capture_model_param_rs is not _LIR_ABSENT:
                _lir_result.model_param_rs = _lir_capture_model_param_rs
            if _lir_capture_model_param_rth is not _LIR_ABSENT:
                _lir_result.model_param_rth = _lir_capture_model_param_rth
            if _lir_capture_model_param_tnom is not _LIR_ABSENT:
                _lir_result.model_param_tnom = _lir_capture_model_param_tnom
            if _lir_capture_model_param_vj is not _LIR_ABSENT:
                _lir_result.model_param_vj = _lir_capture_model_param_vj
            if _lir_capture_model_param_zetais is not _LIR_ABSENT:
                _lir_result.model_param_zetais = _lir_capture_model_param_zetais
            if _lir_capture_model_param_zetars is not _LIR_ABSENT:
                _lir_result.model_param_zetars = _lir_capture_model_param_zetars
            if _lir_capture_model_param_zetarth is not _LIR_ABSENT:
                _lir_result.model_param_zetarth = _lir_capture_model_param_zetarth
            _lir_result._flags = 0
            _lir_result._invalid_params = _lir_invalid_params
            return _lir_result

def _diode_va_model_raw(param_is, given_is, param_rs, given_rs, param_zetars, given_zetars, param_n, given_n, param_cj0, given_cj0, param_vj, given_vj, param_m, given_m, param_rth, given_rth, param_zetarth, given_zetarth, param_zetais, given_zetais, param_ea, given_ea, param_tnom, given_tnom, param_minr, given_minr):
    _lir_invalid_params = []
    return __diode_va_model_raw_entry(_LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, _lir_invalid_params, param_is, given_is, param_rs, given_rs, param_zetars, given_zetars, param_n, given_n, param_cj0, given_cj0, param_vj, given_vj, param_m, given_m, param_rth, given_rth, param_zetarth, given_zetarth, param_zetais, given_zetais, param_ea, given_ea, param_tnom, given_tnom, param_minr, given_minr)


from dataclasses import dataclass
from typing import List, Union

_LIR_UNDEF = object()
class _LirAbsent:
    __slots__ = ()
_LIR_ABSENT = _LirAbsent()

def _lir_result_getattr(self, name):
    if name in type(self)._lir_absent_fields:
        return _LIR_ABSENT
    raise AttributeError(name)

@dataclass(init=False)
class __diode_va_init_rawResult:
    __slots__ = ["cache_0", "cache_1", "cache_2"]
    _lir_absent_fields = frozenset(("cache_0", "cache_1", "cache_2"))
    __getattr__ = _lir_result_getattr
    cache_0: Union[float, _LirAbsent]
    cache_1: Union[float, _LirAbsent]
    cache_2: Union[float, _LirAbsent]

def __diode_va_init_raw_entry(_lir_capture_cache_0, _lir_capture_cache_1, _lir_capture_cache_2, param_minr, param_rs, param_vj, param_m, builtin_mfactor):
    _lir_capture_cache_0 = (param_vj) * ((1) - (math.pow(3, (-1) / (param_m))))
    if (param_rs) > (param_minr):
        v49 = 1
    else:
        v49 = 0
    p52 = math.sqrt(builtin_mfactor)
    _lir_capture_cache_1 = p52
    _lir_capture_cache_2 = (v49) * (p52)
    _lir_result = __diode_va_init_rawResult()
    if _lir_capture_cache_0 is not _LIR_ABSENT:
        _lir_result.cache_0 = _lir_capture_cache_0
    if _lir_capture_cache_1 is not _LIR_ABSENT:
        _lir_result.cache_1 = _lir_capture_cache_1
    if _lir_capture_cache_2 is not _LIR_ABSENT:
        _lir_result.cache_2 = _lir_capture_cache_2
    return _lir_result

def _diode_va_init_raw(param_rth, param_minr, param_tnom, param_n, param_ea, param_rs, param_vj, param_m, param_cj0, builtin_mfactor):
    return __diode_va_init_raw_entry(_LIR_ABSENT, _LIR_ABSENT, _LIR_ABSENT, param_minr, param_rs, param_vj, param_m, builtin_mfactor)


from dataclasses import dataclass
from typing import List, Union

_LIR_UNDEF = object()
class _LirAbsent:
    __slots__ = ()
_LIR_ABSENT = _LirAbsent()

def _lir_result_getattr(self, name):
    if name in type(self)._lir_absent_fields:
        return _LIR_ABSENT
    raise AttributeError(name)

@dataclass(init=False)
class __diode_va_eval_rawResult:
    __slots__ = ["hidden_cd", "hidden_gd", "jacobian_react_0", "jacobian_react_1", "jacobian_react_12", "jacobian_react_2", "jacobian_resist_0", "jacobian_resist_1", "jacobian_resist_12", "jacobian_resist_13", "jacobian_resist_2", "jacobian_resist_3", "jacobian_resist_4", "jacobian_resist_5", "jacobian_resist_6", "jacobian_resist_7", "jacobian_resist_8", "jacobian_resist_9", "residual_react_0", "residual_react_3", "residual_resist_0", "residual_resist_1", "residual_resist_2", "residual_resist_3"]
    _lir_absent_fields = frozenset(("hidden_cd", "hidden_gd", "jacobian_react_0", "jacobian_react_1", "jacobian_react_12", "jacobian_react_2", "jacobian_resist_0", "jacobian_resist_1", "jacobian_resist_12", "jacobian_resist_13", "jacobian_resist_2", "jacobian_resist_3", "jacobian_resist_4", "jacobian_resist_5", "jacobian_resist_6", "jacobian_resist_7", "jacobian_resist_8", "jacobian_resist_9", "residual_react_0", "residual_react_3", "residual_resist_0", "residual_resist_1", "residual_resist_2", "residual_resist_3"))
    __getattr__ = _lir_result_getattr
    hidden_cd: Union[float, _LirAbsent]
    hidden_gd: Union[float, _LirAbsent]
    jacobian_react_0: Union[float, _LirAbsent]
    jacobian_react_1: Union[float, _LirAbsent]
    jacobian_react_12: Union[float, _LirAbsent]
    jacobian_react_2: Union[float, _LirAbsent]
    jacobian_resist_0: Union[float, _LirAbsent]
    jacobian_resist_1: Union[float, _LirAbsent]
    jacobian_resist_12: Union[float, _LirAbsent]
    jacobian_resist_13: Union[float, _LirAbsent]
    jacobian_resist_2: Union[float, _LirAbsent]
    jacobian_resist_3: Union[float, _LirAbsent]
    jacobian_resist_4: Union[float, _LirAbsent]
    jacobian_resist_5: Union[float, _LirAbsent]
    jacobian_resist_6: Union[float, _LirAbsent]
    jacobian_resist_7: Union[float, _LirAbsent]
    jacobian_resist_8: Union[float, _LirAbsent]
    jacobian_resist_9: Union[float, _LirAbsent]
    residual_react_0: Union[float, _LirAbsent]
    residual_react_3: Union[float, _LirAbsent]
    residual_resist_0: Union[float, _LirAbsent]
    residual_resist_1: Union[float, _LirAbsent]
    residual_resist_2: Union[float, _LirAbsent]
    residual_resist_3: Union[float, _LirAbsent]

def __diode_va_eval_raw_entry(param_rth, param_minr, v19, v20, param_is, param_tnom, param_zetais, param_n, param_ea, param_rs, param_zetars, param_zetarth, v59, v61, param_vj, param_m, param_cj0, builtin_mfactor, v85):
    p18 = (param_rth) > (param_minr)
    if p18:
        v24 = (v19) + (v20)
        p415 = 1
    else:
        v24 = v19
        p415 = 0
    v27 = ((0.000000000000000000000013806503) * (v24)) / (0.0000000000000000001602176462)
    p418 = ((p415) * (0.000000000000000000000013806503)) / (0.0000000000000000001602176462)
    v31 = (v24) / (param_tnom)
    p420 = (p415) / (param_tnom)
    v41 = ((v31) - (1)) * (param_ea)
    v42 = (v27) * (param_n)
    p427 = (p418) * (param_n)
    v428 = (v42) * (v42)
    v45 = math.exp((((math.log(v31)) * (param_zetais)) / (param_n)) + ((v41) / (v42)))
    v46 = (param_is) * (v45)
    v51 = math.pow(v31, param_zetars)
    v437 = (v31) == (0)
    if v437:
        v442 = 0
    else:
        v442 = ((p420) * ((param_zetars) / (v31))) * (v51)
    v52 = (param_rs) * (v51)
    v443 = (v442) * (param_rs)
    v56 = math.pow(v31, param_zetarth)
    if v437:
        v449 = 0
    else:
        v449 = ((p420) * ((param_zetarth) / (v31))) * (v56)
    v57 = (param_rth) * (v56)
    v64 = (v59) / (v42)
    v454 = (0) - (((p427) * (v59)) / (v428))
    v455 = (1) / (v42)
    if (v64) > (69.07755278982137):
        v72 = (1000000000000000000000000000000) + ((1000000000000000000000000000000) * ((v64) - (69.07755278982137)))
        v465 = (v454) * (1000000000000000000000000000000)
        v466 = (v455) * (1000000000000000000000000000000)
    else:
        v71 = math.exp(v64)
        v72 = v71
        v465 = (v454) * (v71)
        v466 = (v455) * (v71)
    v74 = (v72) - (1)
    v75 = (v46) * (v74)
    v471 = ((((((((p420) / (v31)) * (param_zetais)) / (param_n)) + ((((p420) * (param_ea)) / (v42)) - (((p427) * (v41)) / (v428)))) * (v45)) * (param_is)) * (v74)) + ((v465) * (v46))
    v472 = (v466) * (v46)
    v90 = (v85) - (v59)
    v94 = (v90) / (v27)
    v477 = (0) - (((p418) * (v90)) / ((v27) * (v27)))
    v478 = (-1) / (v27)
    v479 = (v477) * (v94)
    v482 = (v478) * (v94)
    v99 = math.sqrt(((v94) * (v94)) + (1.92))
    v487 = (2) * (v99)
    v101 = (v94) + (v99)
    p109 = (param_cj0) * (param_vj)
    v113 = (1) - (((v85) - (((v27) * (v101)) / (2))) / (param_vj))
    p115 = (1) - (param_m)
    v116 = math.pow(v113, p115)
    if (v113) == (0):
        v513 = 0
        v514 = 0
    else:
        v507 = (p115) / (v113)
        v513 = (((0) - (((0) - ((((p418) * (v101)) + (((v477) + (((v479) + (v479)) / (v487))) * (v27))) / (2))) / (param_vj))) * (v507)) * (v116)
        v514 = (((0) - (((0) - ((((v478) + (((v482) + (v482)) / (v487))) * (v27)) / (2))) / (param_vj))) * (v507)) * (v116)
    v121 = ((p109) * ((1) - (v116))) / (p115)
    v520 = (((0) - (v513)) * (p109)) / (p115)
    v521 = (((0) - (v514)) * (p109)) / (p115)
    simparam_gmin = _lir_simparam_opt("gmin", 0.000000000001)
    v129 = (v75) + ((simparam_gmin) * (v59))
    v525 = (v472) + (simparam_gmin)
    p144 = (param_rs) > (param_minr)
    if p144:
        v345 = (v61) / (v52)
        v535 = (0) - (((v443) * (v61)) / ((v52) * (v52)))
        v536 = (1) / (v52)
    else:
        v345 = 0
        v535 = 0
        v536 = 0
    if p18:
        v200 = (v75) * (v59)
        v537 = (v471) * (v59)
        if p144:
            v208 = math.pow(v61, 2)
            if (v61) == (0):
                v544 = 0
            else:
                v544 = ((2) / (v61)) * (v208)
            v215 = (v200) + ((v208) / (v52))
            v553 = (v537) + ((0) - (((v443) * (v208)) / ((v52) * (v52))))
            v555 = (v544) / (v52)
            v355 = (v215) - ((v20) / (v57))
            v564 = (v553) - (((1) / (v57)) - ((((v449) * (param_rth)) * (v20)) / ((v57) * (v57))))
            v565 = ((v472) * (v59)) + (v75)
            v566 = v555
        else:
            v355 = (v200) - ((v20) / (v57))
            v564 = (v537) - (((1) / (v57)) - ((((v449) * (param_rth)) * (v20)) / ((v57) * (v57))))
            v565 = ((v472) * (v59)) + (v75)
            v566 = 0
    else:
        v355 = 0
        v564 = 0
        v565 = 0
        v566 = 0
    v611 = (builtin_mfactor) * (v521)
    v621 = (builtin_mfactor) * (-(v536))
    v628 = (builtin_mfactor) * (-(v525))
    v629 = (builtin_mfactor) * (-(v521))
    _lir_result = __diode_va_eval_rawResult()
    _lir_result.residual_resist_0 = (builtin_mfactor) * (v129)
    _lir_result.residual_resist_1 = (builtin_mfactor) * (-(v345))
    _lir_result.residual_resist_2 = (builtin_mfactor) * (v355)
    _lir_result.residual_resist_3 = (builtin_mfactor) * ((-(v129)) + (v345))
    _lir_result.residual_react_0 = (builtin_mfactor) * (v121)
    _lir_result.residual_react_3 = (builtin_mfactor) * (-(v121))
    _lir_result.jacobian_resist_0 = (builtin_mfactor) * (v525)
    _lir_result.jacobian_resist_1 = (builtin_mfactor) * (v471)
    _lir_result.jacobian_resist_2 = v628
    _lir_result.jacobian_resist_3 = (builtin_mfactor) * (v536)
    _lir_result.jacobian_resist_4 = (builtin_mfactor) * (-(v535))
    _lir_result.jacobian_resist_5 = v621
    _lir_result.jacobian_resist_6 = (builtin_mfactor) * (v565)
    _lir_result.jacobian_resist_7 = (builtin_mfactor) * (-(v566))
    _lir_result.jacobian_resist_8 = (builtin_mfactor) * (v564)
    _lir_result.jacobian_resist_9 = (builtin_mfactor) * ((-(v565)) + (v566))
    _lir_result.jacobian_resist_12 = (builtin_mfactor) * ((-(v471)) + (v535))
    _lir_result.jacobian_resist_13 = (builtin_mfactor) * ((v525) + (v536))
    _lir_result.jacobian_react_0 = v611
    _lir_result.jacobian_react_1 = (builtin_mfactor) * (v520)
    _lir_result.jacobian_react_2 = v629
    _lir_result.jacobian_react_12 = (builtin_mfactor) * (-(v520))
    _lir_result.hidden_cd = v521
    _lir_result.hidden_gd = v472
    return _lir_result

def _diode_va_eval_raw(param_rth, param_minr, v19, v20, v22, v28, param_is, param_tnom, param_zetais, param_n, param_ea, v47, param_rs, param_zetars, v53, param_zetarth, v58, v59, v60, v61, v62, v76, param_vj, param_m, v86, v95, v100, v107, param_cj0, v122, v201, v274, v276, v283, v361, v362, builtin_mfactor, v85, v404, v410):
    return __diode_va_eval_raw_entry(param_rth, param_minr, v19, v20, param_is, param_tnom, param_zetais, param_n, param_ea, param_rs, param_zetars, param_zetarth, v59, v61, param_vj, param_m, param_cj0, builtin_mfactor, v85)


_PYOSDI_UNSET = object()


class _PyOsdiModel:
    __slots__ = ("module", "raw", "params", "given", "inst_defaults", "builtin_params", "sim_params")

    def __init__(self, module, raw, params, given, inst_defaults, builtin_params, sim_params):
        self.module = module
        self.raw = raw
        self.params = params
        self.given = given
        self.inst_defaults = inst_defaults
        self.builtin_params = builtin_params
        self.sim_params = sim_params


class _PyOsdiInstance:
    __slots__ = (
        "model",
        "temperature",
        "raw",
        "outputs",
        "params",
        "given",
        "builtin_params",
        "sim_params",
        "hidden",
        "state_idx",
        "cache",
    )

    def __init__(
        self,
        model,
        temperature,
        raw,
        outputs,
        params,
        given,
        builtin_params,
        sim_params,
        hidden,
        state_idx,
        cache,
    ):
        self.model = model
        self.temperature = temperature
        self.raw = raw
        self.outputs = outputs
        self.params = params
        self.given = given
        self.builtin_params = builtin_params
        self.sim_params = sim_params
        self.hidden = hidden
        self.state_idx = state_idx
        self.cache = cache


def _pyosdi_unsupported(message):
    raise RuntimeError(message)


def _pyosdi_missing(context, key):
    raise RuntimeError(f"missing {context} {key!r}")


def _pyosdi_get_required(seq, idx, context):
    try:
        return seq[idx]
    except IndexError:
        raise RuntimeError(f"missing {context} at index {idx}") from None
    except TypeError:
        raise RuntimeError(f"{context} is not indexable") from None


def _pyosdi_solve(sim_info, idx):
    if idx is None:
        raise RuntimeError("missing solve index")
    return _pyosdi_get_required(_pyosdi_sim_info(sim_info, "prev_solve"), idx, "prev_solve")


def _pyosdi_dict_get(items, key, context):
    if items is None:
        _pyosdi_missing(context, key)
    if key not in items:
        _pyosdi_missing(context, key)
    val = items[key]
    if val is None:
        _pyosdi_missing(context, key)
    return val


def _pyosdi_attr_get(item, name, context):
    if item is None:
        _pyosdi_missing(context, name)
    try:
        val = getattr(item, name)
    except AttributeError:
        _pyosdi_missing(context, name)
    if val is None:
        _pyosdi_missing(context, name)
    return val


def _pyosdi_effective_given(params, given):
    effective = dict(given or {})
    for key, val in (params or {}).items():
        if key not in effective and val is not None:
            effective[key] = True
    return effective


def _pyosdi_given_value(given, name):
    return bool((given or {}).get(name, False))


def _pyosdi_setup_param(params, given, name, default):
    if _pyosdi_given_value(given, name):
        return _pyosdi_dict_get(params, name, "model setup parameter")
    return default


def _pyosdi_given_params(params, given):
    params = params or {}
    return {
        key: _pyosdi_dict_get(params, key, "parameter")
        for key, is_given in (given or {}).items()
        if is_given
    }


def _pyosdi_merge_given_params(base, params, given):
    merged = dict(base)
    merged.update(_pyosdi_given_params(params, given))
    return merged


def _pyosdi_raw_missing(name):
    raise RuntimeError(f"missing raw output field {name}")


def _pyosdi_raw_absent(value):
    return value is None or value is _PYOSDI_UNSET or value is _LIR_ABSENT


def _pyosdi_raw_present(value):
    return not _pyosdi_raw_absent(value)


def _pyosdi_raw_value(value, name):
    if _pyosdi_raw_absent(value):
        _pyosdi_raw_missing(name)
    return value


_PYOSDI_SIMPARAM_STACK = []


def _lir_simparam_opt(name, default):
    for items in reversed(_PYOSDI_SIMPARAM_STACK):
        if items is None:
            continue
        try:
            present = name in items
        except TypeError:
            raise RuntimeError("sim_params is not a mapping") from None
        if not present:
            continue
        val = items[name]
        if val is None:
            _pyosdi_missing("simulator parameter", name)
        return val
    return default


def _pyosdi_sim_params_from(sim_info=None, instance=None, model=None):
    if sim_info is not None:
        try:
            sim_params = sim_info.get("sim_params")
        except AttributeError:
            sim_params = None
        if sim_params is not None:
            return sim_params
    if instance is not None:
        return _pyosdi_instance_value(instance, "sim_params")
    if model is not None:
        return _pyosdi_model_value(model, "sim_params")
    return {}


def _pyosdi_sim_info(sim_info, key):
    return _pyosdi_dict_get(sim_info, key, "sim_info")


def _pyosdi_instance_value(instance, key):
    return _pyosdi_attr_get(instance, key, "instance")


def _pyosdi_model_value(model, key):
    return _pyosdi_attr_get(model, key, "model")


def _pyosdi_cache(instance, idx):
    val = _pyosdi_get_required(_pyosdi_instance_value(instance, "cache"), idx, "cache")
    if val is _PYOSDI_UNSET or val is None:
        raise RuntimeError(f"missing cache value at index {idx}")
    return val


def _pyosdi_state(sim_info, which, idx):
    return _pyosdi_get_required(_pyosdi_sim_info(sim_info, which), idx, which)


def _pyosdi_state_idx(instance, idx):
    return _pyosdi_get_required(_pyosdi_instance_value(instance, "state_idx"), idx, "state_idx")


def _pyosdi_param(instance, model, name):
    inst_params = _pyosdi_instance_value(instance, "params")
    if name in inst_params and inst_params[name] is not None:
        return inst_params[name]
    if name in inst_params:
        _pyosdi_missing("parameter", name)
    model_params = _pyosdi_model_value(model, "params")
    if name in model_params and model_params[name] is not None:
        return model_params[name]
    if name in model_params:
        _pyosdi_missing("parameter", name)
    _pyosdi_missing("parameter", name)


def _pyosdi_given(instance, model, name):
    inst_given = _pyosdi_instance_value(instance, "given")
    if name in inst_given and inst_given[name]:
        return True
    return bool(_pyosdi_model_value(model, "given").get(name, False))


def _pyosdi_builtin(instance, name, default):
    return _pyosdi_builtin_default(_pyosdi_instance_value(instance, "builtin_params"), name, default)


def _pyosdi_builtin_default(items, name, default):
    if items is None or name not in items:
        return default
    val = items[name]
    if val is None:
        _pyosdi_missing("builtin parameter", name)
    return val


def _pyosdi_connected(sim_info, idx):
    if idx is None:
        raise RuntimeError("missing connected terminal index")
    connected = _pyosdi_sim_info(sim_info, "connected_terminals")
    return idx < connected


def _pyosdi_hidden(instance, idx, name):
    hidden = _pyosdi_instance_value(instance, "hidden")
    val = _pyosdi_get_required(hidden, idx, f"hidden state {name!r}")
    if val is _PYOSDI_UNSET or val is None:
        _pyosdi_missing("hidden state", name)
    return val


def _pyosdi_output(instance, idx, name):
    outputs = _pyosdi_instance_value(instance, "outputs")
    val = _pyosdi_get_required(outputs, idx, f"output {name!r}")
    if val is _PYOSDI_UNSET or val is None:
        _pyosdi_missing("output", name)
    return val


def _pyosdi_return_flags(raw):
    if raw is None:
        _pyosdi_raw_missing("_flags")
    flags = getattr(raw, "_flags", 0)
    invalid_params = getattr(raw, "_invalid_params", [])
    if invalid_params is None or invalid_params is _LIR_ABSENT:
        invalid_params = []
    if invalid_params:
        raise RuntimeError(f"unsupported invalid parameter flag(s): {invalid_params!r}")
    if flags is None or flags is _LIR_ABSENT:
        return 0
    return int(flags)


def _pyosdi_missing_hidden(name):
    raise RuntimeError(f"hidden state {name!r} is required before Python OSDI setup can run")

def diode_va_setup_model(params=None, given=None, builtin_params=None, sim_params=None):
    if params is None:
        params = {}
    if given is None:
        given = {}
    if builtin_params is None:
        builtin_params = {}
    if sim_params is None:
        sim_params = {}
    given = _pyosdi_effective_given(params, given)
    _raw_args = [
        _pyosdi_setup_param(params, given, "is", 0.0),
        _pyosdi_given_value(given, "is"),
        _pyosdi_setup_param(params, given, "rs", 0.0),
        _pyosdi_given_value(given, "rs"),
        _pyosdi_setup_param(params, given, "zetars", 0.0),
        _pyosdi_given_value(given, "zetars"),
        _pyosdi_setup_param(params, given, "n", 0.0),
        _pyosdi_given_value(given, "n"),
        _pyosdi_setup_param(params, given, "cj0", 0.0),
        _pyosdi_given_value(given, "cj0"),
        _pyosdi_setup_param(params, given, "vj", 0.0),
        _pyosdi_given_value(given, "vj"),
        _pyosdi_setup_param(params, given, "m", 0.0),
        _pyosdi_given_value(given, "m"),
        _pyosdi_setup_param(params, given, "rth", 0.0),
        _pyosdi_given_value(given, "rth"),
        _pyosdi_setup_param(params, given, "zetarth", 0.0),
        _pyosdi_given_value(given, "zetarth"),
        _pyosdi_setup_param(params, given, "zetais", 0.0),
        _pyosdi_given_value(given, "zetais"),
        _pyosdi_setup_param(params, given, "ea", 0.0),
        _pyosdi_given_value(given, "ea"),
        _pyosdi_setup_param(params, given, "tnom", 0.0),
        _pyosdi_given_value(given, "tnom"),
        _pyosdi_setup_param(params, given, "minr", 0.0),
        _pyosdi_given_value(given, "minr"),
    ]
    _PYOSDI_SIMPARAM_STACK.append(sim_params)
    try:
        _raw = _diode_va_model_raw(*_raw_args)
    finally:
        _PYOSDI_SIMPARAM_STACK.pop()
    _params = _pyosdi_given_params(params, given)
    _inst_defaults = {}
    if _pyosdi_raw_present(_raw.model_param_is):
        _params["is"] = _pyosdi_raw_value(_raw.model_param_is, "model_param_is")
    if _pyosdi_raw_present(_raw.model_param_rs):
        _params["rs"] = _pyosdi_raw_value(_raw.model_param_rs, "model_param_rs")
    if _pyosdi_raw_present(_raw.model_param_zetars):
        _params["zetars"] = _pyosdi_raw_value(_raw.model_param_zetars, "model_param_zetars")
    if _pyosdi_raw_present(_raw.model_param_n):
        _params["n"] = _pyosdi_raw_value(_raw.model_param_n, "model_param_n")
    if _pyosdi_raw_present(_raw.model_param_cj0):
        _params["cj0"] = _pyosdi_raw_value(_raw.model_param_cj0, "model_param_cj0")
    if _pyosdi_raw_present(_raw.model_param_vj):
        _params["vj"] = _pyosdi_raw_value(_raw.model_param_vj, "model_param_vj")
    if _pyosdi_raw_present(_raw.model_param_m):
        _params["m"] = _pyosdi_raw_value(_raw.model_param_m, "model_param_m")
    if _pyosdi_raw_present(_raw.model_param_rth):
        _params["rth"] = _pyosdi_raw_value(_raw.model_param_rth, "model_param_rth")
    if _pyosdi_raw_present(_raw.model_param_zetarth):
        _params["zetarth"] = _pyosdi_raw_value(_raw.model_param_zetarth, "model_param_zetarth")
    if _pyosdi_raw_present(_raw.model_param_zetais):
        _params["zetais"] = _pyosdi_raw_value(_raw.model_param_zetais, "model_param_zetais")
    if _pyosdi_raw_present(_raw.model_param_ea):
        _params["ea"] = _pyosdi_raw_value(_raw.model_param_ea, "model_param_ea")
    if _pyosdi_raw_present(_raw.model_param_tnom):
        _params["tnom"] = _pyosdi_raw_value(_raw.model_param_tnom, "model_param_tnom")
    if _pyosdi_raw_present(_raw.model_param_minr):
        _params["minr"] = _pyosdi_raw_value(_raw.model_param_minr, "model_param_minr")
    return _PyOsdiModel("diode_va", _raw, _params, dict(given), _inst_defaults, dict(builtin_params), dict(sim_params))


def diode_va_setup_instance(model=None, temperature=300.0, params=None, given=None, builtin_params=None, connected_terminals=None, sim_params=None):
    if model is None:
        model = diode_va_setup_model(sim_params=sim_params)
    if sim_params is None:
        sim_params = _pyosdi_model_value(model, "sim_params")
    if builtin_params is None:
        builtin_params = {}
    _builtin_params = {"mfactor": 1.0}
    _builtin_params.update(builtin_params)
    _given = _pyosdi_effective_given(params, given)
    _params = _pyosdi_merge_given_params(_pyosdi_model_value(model, "inst_defaults"), params, _given)
    _hidden = [0.0] * 16
    instance = _PyOsdiInstance(model, temperature, [], [_PYOSDI_UNSET] * 6, _params, _given, _builtin_params, dict(sim_params), _hidden, list(range(0)), [_PYOSDI_UNSET] * 3)
    _raw_args = [
        _pyosdi_param(instance, model, "rth"),
        _pyosdi_param(instance, model, "minr"),
        _pyosdi_param(instance, model, "tnom"),
        _pyosdi_param(instance, model, "n"),
        _pyosdi_param(instance, model, "ea"),
        _pyosdi_param(instance, model, "rs"),
        _pyosdi_param(instance, model, "vj"),
        _pyosdi_param(instance, model, "m"),
        _pyosdi_param(instance, model, "cj0"),
        _pyosdi_builtin(instance, "mfactor", 1.0),
    ]
    _PYOSDI_SIMPARAM_STACK.append(sim_params)
    try:
        _raw = _diode_va_init_raw(*_raw_args)
    finally:
        _PYOSDI_SIMPARAM_STACK.pop()
    instance.raw = _raw
    _cache = instance.cache
    if _pyosdi_raw_present(_raw.cache_0):
        _cache[0] = _pyosdi_raw_value(_raw.cache_0, "cache_0")
    if _pyosdi_raw_present(_raw.cache_1):
        _cache[1] = _pyosdi_raw_value(_raw.cache_1, "cache_1")
    if _pyosdi_raw_present(_raw.cache_2):
        _cache[2] = _pyosdi_raw_value(_raw.cache_2, "cache_2")
    _hidden = instance.hidden
    return instance


def diode_va_eval(instance=None, model=None, sim_info=None):
    if instance is None:
        instance = diode_va_setup_instance(model)
    if model is None:
        model = _pyosdi_instance_value(instance, "model")
    if sim_info is None:
        sim_info = {}
    _sim_params = _pyosdi_sim_params_from(sim_info, instance, model)
    _raw_args = [
        _pyosdi_param(instance, model, "rth"),
        _pyosdi_param(instance, model, "minr"),
        float(_pyosdi_instance_value(instance, "temperature")),
        _pyosdi_solve(sim_info, 2),
        None,
        None,
        _pyosdi_param(instance, model, "is"),
        _pyosdi_param(instance, model, "tnom"),
        _pyosdi_param(instance, model, "zetais"),
        _pyosdi_param(instance, model, "n"),
        _pyosdi_param(instance, model, "ea"),
        None,
        _pyosdi_param(instance, model, "rs"),
        _pyosdi_param(instance, model, "zetars"),
        None,
        _pyosdi_param(instance, model, "zetarth"),
        None,
        (_pyosdi_solve(sim_info, 0) - _pyosdi_solve(sim_info, 3)),
        None,
        (_pyosdi_solve(sim_info, 3) - _pyosdi_solve(sim_info, 1)),
        None,
        None,
        _pyosdi_param(instance, model, "vj"),
        _pyosdi_param(instance, model, "m"),
        *([None] * 4),
        _pyosdi_param(instance, model, "cj0"),
        *([None] * 7),
        _pyosdi_builtin(instance, "mfactor", 1.0),
        _pyosdi_cache(instance, 0),
        _pyosdi_cache(instance, 1),
        _pyosdi_cache(instance, 2),
    ]
    _PYOSDI_SIMPARAM_STACK.append(_sim_params)
    try:
        _raw = _diode_va_eval_raw(*_raw_args)
    finally:
        _PYOSDI_SIMPARAM_STACK.pop()
    output_residual_resist = [_pyosdi_raw_value(_raw.residual_resist_0, "residual_resist_0"), _pyosdi_raw_value(_raw.residual_resist_1, "residual_resist_1"), _pyosdi_raw_value(_raw.residual_resist_2, "residual_resist_2"), _pyosdi_raw_value(_raw.residual_resist_3, "residual_resist_3")]
    output_residual_react = [_pyosdi_raw_value(_raw.residual_react_0, "residual_react_0"), 0.0, 0.0, _pyosdi_raw_value(_raw.residual_react_3, "residual_react_3")]
    output_limit_rhs_resist = [0.0, 0.0, 0.0, 0.0]
    output_limit_rhs_react = [0.0, 0.0, 0.0, 0.0]
    output_jacobian_resist = [_pyosdi_raw_value(_raw.jacobian_resist_0, "jacobian_resist_0"), _pyosdi_raw_value(_raw.jacobian_resist_1, "jacobian_resist_1"), _pyosdi_raw_value(_raw.jacobian_resist_2, "jacobian_resist_2"), _pyosdi_raw_value(_raw.jacobian_resist_3, "jacobian_resist_3"), _pyosdi_raw_value(_raw.jacobian_resist_4, "jacobian_resist_4"), _pyosdi_raw_value(_raw.jacobian_resist_5, "jacobian_resist_5"), _pyosdi_raw_value(_raw.jacobian_resist_6, "jacobian_resist_6"), _pyosdi_raw_value(_raw.jacobian_resist_7, "jacobian_resist_7"), _pyosdi_raw_value(_raw.jacobian_resist_8, "jacobian_resist_8"), _pyosdi_raw_value(_raw.jacobian_resist_9, "jacobian_resist_9"), _pyosdi_raw_value(_raw.jacobian_resist_2, "jacobian_resist_2"), _pyosdi_raw_value(_raw.jacobian_resist_5, "jacobian_resist_5"), _pyosdi_raw_value(_raw.jacobian_resist_12, "jacobian_resist_12"), _pyosdi_raw_value(_raw.jacobian_resist_13, "jacobian_resist_13")]
    output_jacobian_react = [_pyosdi_raw_value(_raw.jacobian_react_0, "jacobian_react_0"), _pyosdi_raw_value(_raw.jacobian_react_1, "jacobian_react_1"), _pyosdi_raw_value(_raw.jacobian_react_2, "jacobian_react_2"), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, _pyosdi_raw_value(_raw.jacobian_react_2, "jacobian_react_2"), 0.0, _pyosdi_raw_value(_raw.jacobian_react_12, "jacobian_react_12"), _pyosdi_raw_value(_raw.jacobian_react_0, "jacobian_react_0")]
    instance.outputs = [
        output_residual_resist,
        output_residual_react,
        output_limit_rhs_resist,
        output_limit_rhs_react,
        output_jacobian_resist,
        output_jacobian_react,
    ]
    _hidden = instance.hidden
    if _pyosdi_raw_present(_raw.hidden_cd):
        _hidden[0] = _pyosdi_raw_value(_raw.hidden_cd, "hidden_cd")
    if _pyosdi_raw_present(_raw.hidden_gd):
        _hidden[1] = _pyosdi_raw_value(_raw.hidden_gd, "hidden_gd")
    return {
        "flags": _pyosdi_return_flags(_raw),
        "residual_resist": output_residual_resist,
        "residual_react": output_residual_react,
        "limit_rhs_resist": output_limit_rhs_resist,
        "limit_rhs_react": output_limit_rhs_react,
        "jacobian_resist": output_jacobian_resist,
        "jacobian_react": output_jacobian_react,
    }


def diode_va_load_residual_resist(instance):
    return _pyosdi_output(instance, 0, "residual_resist")


def diode_va_load_residual_react(instance):
    return _pyosdi_output(instance, 1, "residual_react")


def diode_va_load_limit_rhs_resist(instance):
    return _pyosdi_output(instance, 2, "limit_rhs_resist")


def diode_va_load_limit_rhs_react(instance):
    return _pyosdi_output(instance, 3, "limit_rhs_react")


def diode_va_load_jacobian_resist(instance):
    return _pyosdi_output(instance, 4, "jacobian_resist")


def diode_va_load_jacobian_react(instance):
    return _pyosdi_output(instance, 5, "jacobian_react")
