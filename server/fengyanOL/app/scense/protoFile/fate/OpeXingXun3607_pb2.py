# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='OpeXingXun3607.proto',
  package='protoFile.fate.OpeXingXun3607',
  serialized_pb='\n\x14OpeXingXun3607.proto\x12\x1dprotoFile.fate.OpeXingXun3607\"_\n\x11OpeXingXunRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05opeId\x18\x02 \x01(\x05\x12\x0f\n\x07opeType\x18\x03 \x02(\x05\x12\x0f\n\x07\x66romPos\x18\x04 \x02(\x05\x12\r\n\x05toPos\x18\x05 \x02(\x05\"D\n\x12OpeXingXunResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\r\n\x05oType\x18\x03 \x01(\x05')




_OPEXINGXUNREQUEST = descriptor.Descriptor(
  name='OpeXingXunRequest',
  full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='opeId', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest.opeId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='opeType', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest.opeType', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fromPos', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest.fromPos', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='toPos', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunRequest.toPos', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=55,
  serialized_end=150,
)


_OPEXINGXUNRESPONSE = descriptor.Descriptor(
  name='OpeXingXunResponse',
  full_name='protoFile.fate.OpeXingXun3607.OpeXingXunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunResponse.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='oType', full_name='protoFile.fate.OpeXingXun3607.OpeXingXunResponse.oType', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=152,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['OpeXingXunRequest'] = _OPEXINGXUNREQUEST
DESCRIPTOR.message_types_by_name['OpeXingXunResponse'] = _OPEXINGXUNRESPONSE

class OpeXingXunRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPEXINGXUNREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.fate.OpeXingXun3607.OpeXingXunRequest)

class OpeXingXunResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPEXINGXUNRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.fate.OpeXingXun3607.OpeXingXunResponse)

# @@protoc_insertion_point(module_scope)
