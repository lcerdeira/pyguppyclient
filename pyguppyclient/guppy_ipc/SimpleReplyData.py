# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SimpleReplyData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSimpleReplyData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SimpleReplyData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SimpleReplyDataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x30\x30\x30\x31", size_prefixed=size_prefixed)

    # SimpleReplyData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SimpleReplyData
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # SimpleReplyData
    def Data(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # SimpleReplyData
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def SimpleReplyDataStart(builder): builder.StartObject(3)
def SimpleReplyDataAddType(builder, type): builder.PrependUint32Slot(0, type, 0)
def SimpleReplyDataAddData(builder, data): builder.PrependUint32Slot(1, data, 0)
def SimpleReplyDataAddText(builder, text): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def SimpleReplyDataEnd(builder): return builder.EndObject()