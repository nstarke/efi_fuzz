from qiling.os.uefi.type64 import *

import ctypes

c_int128 = ctypes.c_ubyte*16
c_uint128 = c_int128
void = None
if ctypes.sizeof(ctypes.c_longdouble) == 16:
    c_long_double_t = ctypes.c_longdouble
else:
    c_long_double_t = ctypes.c_ubyte*16

# if local wordsize is same as target, keep ctypes pointer function.
# required to access _ctypes
import _ctypes
# Emulate a pointer class using the approriate c_int32/c_int64 type
# The new class should have :
# ['__module__', 'from_param', '_type_', '__dict__', '__weakref__', '__doc__']
# but the class should be submitted to a unique instance for each base type
# to that if A == B, POINTER_T(A) == POINTER_T(B)
ctypes._pointer_t_type_cache = {}
def POINTER_T(pointee):
    # a pointer should have the same length as LONG
    fake_ptr_base_type = ctypes.c_uint64 
    # specific case for c_void_p
    if pointee is None: # VOID pointer type. c_void_p.
        pointee = type(None) # ctypes.c_void_p # ctypes.c_ulong
        clsname = 'c_void'
    else:
        clsname = pointee.__name__
    if clsname in ctypes._pointer_t_type_cache:
        return ctypes._pointer_t_type_cache[clsname]
    # make template
    _class = type('LP_%d_%s'%(8, clsname), (fake_ptr_base_type,),{}) 
    ctypes._pointer_t_type_cache[clsname] = _class
    return _class



undefined = ctypes.c_ubyte
ImageBaseOffset32 = ctypes.c_uint32
byte = ctypes.c_ubyte
dword = ctypes.c_uint32
longlong = ctypes.c_int64
qword = ctypes.c_uint64
uchar = ctypes.c_ubyte
uint = ctypes.c_uint32
ulonglong = ctypes.c_uint64
undefined1 = ctypes.c_ubyte
undefined2 = ctypes.c_uint16
undefined4 = ctypes.c_uint32
undefined8 = ctypes.c_uint64
ushort = ctypes.c_uint16
word = ctypes.c_uint16


class struct_EFI_SMM_CPU_PROTOCOL(ctypes.Structure):
    pass

EFI_SMM_CPU_READ_SAVE_STATE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_EFI_SMM_CPU_PROTOCOL), POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(None)))
EFI_SMM_CPU_WRITE_SAVE_STATE = POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(struct_EFI_SMM_CPU_PROTOCOL), UINTN, UINTN, UINTN, POINTER_T(None)))

struct_EFI_SMM_CPU_PROTOCOL._pack_ = True # source:False
struct_EFI_SMM_CPU_PROTOCOL._functions_ = []
struct_EFI_SMM_CPU_PROTOCOL._functions_.append(("ReadSaveState",['ctypes.c_uint64', 'POINTER_T(struct__EFI_SMM_SW_DISPATCH2_PROTOCOL)', 'POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))', 'POINTER_T(struct_EFI_SMM_SW_REGISTER_CONTEXT)', 'POINTER_T(POINTER_T(None))']))
struct_EFI_SMM_CPU_PROTOCOL._functions_.append(("WriteSaveState",['ctypes.c_uint64', 'POINTER_T(struct__EFI_SMM_SW_DISPATCH2_PROTOCOL)', 'POINTER_T(ctypes.CFUNCTYPE(ctypes.c_uint64, POINTER_T(None), POINTER_T(None), POINTER_T(None), POINTER_T(ctypes.c_uint64)))', 'POINTER_T(struct_EFI_SMM_SW_REGISTER_CONTEXT)', 'POINTER_T(POINTER_T(None))']))
struct_EFI_SMM_CPU_PROTOCOL._fields_ = [
    ('ReadSaveState', EFI_SMM_CPU_READ_SAVE_STATE),
    ('WriteSaveState', EFI_SMM_CPU_WRITE_SAVE_STATE),
]

_EFI_SMM_CPU_PROTOCOL = struct_EFI_SMM_CPU_PROTOCOL
EFI_SMM_CPU_PROTOCOL = struct_EFI_SMM_CPU_PROTOCOL
P_EFI_SMM_CPU_PROTOCOL = POINTER_T(struct_EFI_SMM_CPU_PROTOCOL)