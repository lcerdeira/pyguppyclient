# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ProtocolVersion(object):
    __slots__ = ['_tab']

    # ProtocolVersion
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProtocolVersion
    def MajorVersion(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # ProtocolVersion
    def MinorVersion(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # ProtocolVersion
    def PatchVersion(self): return self._tab.Get(flatbuffers.number_types.Uint32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))

def CreateProtocolVersion(builder, majorVersion, minorVersion, patchVersion):
    builder.Prep(4, 12)
    builder.PrependUint32(patchVersion)
    builder.PrependUint32(minorVersion)
    builder.PrependUint32(majorVersion)
    return builder.Offset()
