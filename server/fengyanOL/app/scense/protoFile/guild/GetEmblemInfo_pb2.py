# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/GetEmblemInfo.proto',
  package='protoFile.guild.GetEmblemInfo',
  serialized_pb='\n#protoFile/guild/GetEmblemInfo.proto\x12\x1dprotoFile.guild.GetEmblemInfo\"\"\n\x14GetEmblemInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"q\n\x15GetEmblemInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32).protoFile.guild.GetEmblemInfo.EmblemInfo\"\xf3\x02\n\nEmblemInfo\x12\x14\n\x0c\x63orpsFounder\x18\x01 \x01(\t\x12\x0f\n\x07\x63orpsId\x18\x02 \x01(\x05\x12\x10\n\x08\x63orpsImg\x18\x03 \x01(\x05\x12\x12\n\ncreateData\x18\x04 \x01(\t\x12\x12\n\ncorpsLevel\x18\x05 \x01(\x05\x12\x13\n\x0b\x65mblemLevel\x18\x06 \x01(\x05\x12\x12\n\ncorpsChief\x18\x07 \x01(\t\x12\x43\n\x0bveteranList\x18\x08 \x03(\x0b\x32..protoFile.guild.GetEmblemInfo.ManagermentInfo\x12\x41\n\tstaffInfo\x18\t \x03(\x0b\x32..protoFile.guild.GetEmblemInfo.ManagermentInfo\x12\x41\n\torderInfo\x18\n \x03(\x0b\x32..protoFile.guild.GetEmblemInfo.ManagermentInfo\x12\x10\n\x08\x62ugleTxt\x18\x0b \x01(\x05\"#\n\x0fManagermentInfo\x12\x10\n\x08roleName\x18\x01 \x01(\t')




_GETEMBLEMINFOREQUEST = descriptor.Descriptor(
  name='GetEmblemInfoRequest',
  full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=70,
  serialized_end=104,
)


_GETEMBLEMINFORESPONSE = descriptor.Descriptor(
  name='GetEmblemInfoResponse',
  full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.guild.GetEmblemInfo.GetEmblemInfoResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=106,
  serialized_end=219,
)


_EMBLEMINFO = descriptor.Descriptor(
  name='EmblemInfo',
  full_name='protoFile.guild.GetEmblemInfo.EmblemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='corpsFounder', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.corpsFounder', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsId', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.corpsId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsImg', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.corpsImg', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='createData', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.createData', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsLevel', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.corpsLevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='emblemLevel', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.emblemLevel', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='corpsChief', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.corpsChief', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='veteranList', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.veteranList', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='staffInfo', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.staffInfo', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='orderInfo', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.orderInfo', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bugleTxt', full_name='protoFile.guild.GetEmblemInfo.EmblemInfo.bugleTxt', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=222,
  serialized_end=593,
)


_MANAGERMENTINFO = descriptor.Descriptor(
  name='ManagermentInfo',
  full_name='protoFile.guild.GetEmblemInfo.ManagermentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleName', full_name='protoFile.guild.GetEmblemInfo.ManagermentInfo.roleName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=595,
  serialized_end=630,
)

_GETEMBLEMINFORESPONSE.fields_by_name['data'].message_type = _EMBLEMINFO
_EMBLEMINFO.fields_by_name['veteranList'].message_type = _MANAGERMENTINFO
_EMBLEMINFO.fields_by_name['staffInfo'].message_type = _MANAGERMENTINFO
_EMBLEMINFO.fields_by_name['orderInfo'].message_type = _MANAGERMENTINFO
DESCRIPTOR.message_types_by_name['GetEmblemInfoRequest'] = _GETEMBLEMINFOREQUEST
DESCRIPTOR.message_types_by_name['GetEmblemInfoResponse'] = _GETEMBLEMINFORESPONSE
DESCRIPTOR.message_types_by_name['EmblemInfo'] = _EMBLEMINFO
DESCRIPTOR.message_types_by_name['ManagermentInfo'] = _MANAGERMENTINFO

class GetEmblemInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETEMBLEMINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetEmblemInfo.GetEmblemInfoRequest)

class GetEmblemInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETEMBLEMINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetEmblemInfo.GetEmblemInfoResponse)

class EmblemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EMBLEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetEmblemInfo.EmblemInfo)

class ManagermentInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANAGERMENTINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.GetEmblemInfo.ManagermentInfo)

# @@protoc_insertion_point(module_scope)