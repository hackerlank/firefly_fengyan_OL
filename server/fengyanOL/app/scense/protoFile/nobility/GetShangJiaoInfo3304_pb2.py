# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/nobility/GetShangJiaoInfo3304.proto',
  package='protoFile.nobility.GetShangJiaoInfo3304',
  serialized_pb='\n-protoFile/nobility/GetShangJiaoInfo3304.proto\x12\'protoFile.nobility.GetShangJiaoInfo3304\"1\n\x17GetShangJiaoInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\n\n\x02wy\x18\x02 \x02(\t\";\n\x18GetShangJiaoInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_GETSHANGJIAOINFOREQUEST = descriptor.Descriptor(
  name='GetShangJiaoInfoRequest',
  full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wy', full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoRequest.wy', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=90,
  serialized_end=139,
)


_GETSHANGJIAOINFORESPONSE = descriptor.Descriptor(
  name='GetShangJiaoInfoResponse',
  full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=141,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['GetShangJiaoInfoRequest'] = _GETSHANGJIAOINFOREQUEST
DESCRIPTOR.message_types_by_name['GetShangJiaoInfoResponse'] = _GETSHANGJIAOINFORESPONSE

class GetShangJiaoInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSHANGJIAOINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoRequest)

class GetShangJiaoInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSHANGJIAOINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.nobility.GetShangJiaoInfo3304.GetShangJiaoInfoResponse)

# @@protoc_insertion_point(module_scope)
